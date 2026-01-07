"""
Aave V3 Data Collector using Official Aave GraphQL API
Direct access to https://api.v3.aave.com/graphql
Chain ID 1 = Ethereum Mainnet
"""

import requests
import pandas as pd
from datetime import datetime
import json

# Aave Official GraphQL API
# AAVE_GRAPHQL_API = "https://api.v3.aave.com/graphql"
AAVE_GRAPHQL_API = "https://api.morpho.org/graphql"

# Chain IDs
CHAIN_IDS = {
    'ethereum': 1,
    'polygon': 137,
    'avalanche': 43114,
    'arbitrum': 42161,
    'optimism': 10,
    'base': 8453,
}

def query_aave_graphql(query):
    """Send GraphQL query to Aave API"""
    headers = {
        'Content-Type': 'application/json',
    }
    
    response = requests.post(
        AAVE_GRAPHQL_API,
        json={'query': query},
        headers=headers
    )
    
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        raise Exception(f"Query failed with status {response.status_code}: {response.text}")

def get_market_data(chain_id=1):
    """
    Get market data for a specific chain
    Returns reserves (assets), rates, liquidity, etc.
    """
    
    query = """
    query {
        transactions(
            where: {
            marketUniqueKey_in: [
                "0x49bb2d114be9041a787432952927f6f144f05ad3e83196a7d062f374ee11d0ee"
                "0x093d5b432aace8bf6c4d67494f4ac2542a499571ff7a1bcc9f8778f3200d457d"
            ]
            type_in: [MarketLiquidation]
            }
        ) {
            items {
            blockNumber
            hash
            type
            user {
                address
            }
            data {
                ... on MarketLiquidationTransactionData {
                seizedAssets
                repaidAssets
                seizedAssetsUsd
                repaidAssetsUsd
                badDebtAssetsUsd
                liquidator
                market {
                    uniqueKey
                }
                }
            }
            }
        }
        }
    """

    query = """
    query {
  userByAddress(
    chainId: 1
    address: "0x821880a3E2bac432d67E5155e72BB655Ef65fa5E"
  ) {
    address
    marketPositions {
      market {
        uniqueKey
      }
      borrowAssets
      borrowAssetsUsd
      supplyAssets
      supplyAssetsUsd
    }
    vaultPositions {
      vault {
        address
        name
      }
      assets
      assetsUsd
      shares
    }
    transactions {
      hash
      timestamp
      type
    }
  }
}
    """
    
    print(f"Querying Aave API for Chain ID: {chain_id} (Ethereum)")
    print(f"API Endpoint: {AAVE_GRAPHQL_API}")
    print("-" * 70)
    
    result = query_aave_graphql(query)
    return result

def get_user_reserves(user_address, chain_id=1):
    """
    Get user's reserve data (deposits, borrows, health factor)
    """
    
    query = f"""
    {{
      userReserves(
        user: "{user_address}"
        chainId: {chain_id}
      ) {{
        reserve {{
          symbol
          name
          underlyingAsset
        }}
        scaledATokenBalance
        usageAsCollateralEnabledOnUser
        scaledVariableDebt
        principalStableDebt
        stableBorrowRate
      }}
    }}
    """
    
    result = query_aave_graphql(query)
    return result

def get_reserve_incentives(chain_id=1):
    """
    Get incentive data for reserves (rewards, emissions)
    """
    
    query = f"""
    {{
      reserveIncentives(chainId: {chain_id}) {{
        id
        underlyingAsset
        symbol
        aIncentiveData {{
          tokenAddress
          incentiveControllerAddress
          rewardsTokenInformation {{
            rewardTokenSymbol
            rewardTokenAddress
            emissionPerSecond
          }}
        }}
        vIncentiveData {{
          tokenAddress
          incentiveControllerAddress
          rewardsTokenInformation {{
            rewardTokenSymbol
            rewardTokenAddress
            emissionPerSecond
          }}
        }}
      }}
    }}
    """
    
    result = query_aave_graphql(query)
    return result

def process_market_data(data):
    """Convert market data to pandas DataFrame"""
    
    if 'data' not in data or 'markets' not in data['data']:
        print("Error: No market data found")
        return pd.DataFrame()
    
    markets = data['data']['markets']
    
    if not markets or len(markets) == 0:
        print("Error: Markets list is empty")
        return pd.DataFrame()
    
    # Get reserves from first market (Ethereum)
    reserves = markets[0]['reserves']
    
    processed_reserves = []
    
    for reserve in reserves:
        processed_reserve = {
            'symbol': reserve['symbol'],
            'name': reserve['name'],
            'underlying_asset': reserve['underlyingAsset'],
            'is_active': reserve['isActive'],
            'is_frozen': reserve['isFrozen'],
            'can_be_collateral': reserve['usageAsCollateralEnabled'],
            'borrowing_enabled': reserve['borrowingEnabled'],
            
            # Liquidity data
            'total_liquidity': float(reserve['totalLiquidity']),
            'available_liquidity': float(reserve['availableLiquidity']),
            'utilization_rate': float(reserve['utilizationRate']) * 100,
            
            # Debt data
            'total_variable_debt': float(reserve['totalVariableDebt']),
            'total_stable_debt': float(reserve['totalStableDebt']),
            
            # APY/Rates (converted to percentage)
            'supply_apy': float(reserve['supplyAPY']) * 100,
            'variable_borrow_apy': float(reserve['variableBorrowAPY']) * 100,
            'stable_borrow_apy': float(reserve['stableBorrowAPY']) * 100,
            
            # Price
            'price_usd': float(reserve['priceInUSD']) if reserve['priceInUSD'] else 0,
            
            # Risk parameters
            'liquidation_threshold': float(reserve['reserveLiquidationThreshold']) / 100,
            'liquidation_bonus': float(reserve['reserveLiquidationBonus']) / 100,
            'max_ltv': float(reserve['baseLTVasCollateral']) / 100,
        }
        
        processed_reserves.append(processed_reserve)
    
    return pd.DataFrame(processed_reserves)

def analyze_market_data(df):
    """Generate insights from market data"""
    
    print("\n" + "=" * 70)
    print("AAVE V3 ETHEREUM MARKET ANALYSIS")
    print("=" * 70)
    
    # Filter active reserves
    active = df[df['is_active'] == True]
    
    print(f"\n📊 Market Overview:")
    print(f"   Total Assets: {len(df)}")
    print(f"   Active Assets: {len(active)}")
    print(f"   Frozen Assets: {len(df[df['is_frozen'] == True])}")
    
    # Top by liquidity
    print(f"\n💰 Top 5 Assets by Total Liquidity:")
    top_liquidity = active.nlargest(5, 'total_liquidity')[['symbol', 'total_liquidity', 'available_liquidity']]
    for idx, row in top_liquidity.iterrows():
        print(f"   {row['symbol']:8} - Total: ${row['total_liquidity']:,.2f} | Available: ${row['available_liquidity']:,.2f}")
    
    # Top by supply APY
    print(f"\n📈 Top 5 Supply APY:")
    top_supply = active.nlargest(5, 'supply_apy')[['symbol', 'supply_apy', 'total_liquidity']]
    for idx, row in top_supply.iterrows():
        print(f"   {row['symbol']:8} - {row['supply_apy']:.2f}% APY | Liquidity: ${row['total_liquidity']:,.2f}")
    
    # Top by borrow APY (lowest is best for borrowers)
    print(f"\n📉 Lowest 5 Variable Borrow APY (Best for Borrowers):")
    top_borrow = active[active['borrowing_enabled'] == True].nsmallest(5, 'variable_borrow_apy')[['symbol', 'variable_borrow_apy', 'total_variable_debt']]
    for idx, row in top_borrow.iterrows():
        print(f"   {row['symbol']:8} - {row['variable_borrow_apy']:.2f}% APY | Total Debt: ${row['total_variable_debt']:,.2f}")
    
    # Utilization rates
    print(f"\n⚡ Top 5 Utilization Rates:")
    top_util = active.nlargest(5, 'utilization_rate')[['symbol', 'utilization_rate', 'available_liquidity']]
    for idx, row in top_util.iterrows():
        print(f"   {row['symbol']:8} - {row['utilization_rate']:.2f}% | Available: ${row['available_liquidity']:,.2f}")
    
    # Total Value Locked
    total_liquidity = active['total_liquidity'].sum()
    total_debt = (active['total_variable_debt'] + active['total_stable_debt']).sum()
    
    print(f"\n💎 Total Value Locked (TVL):")
    print(f"   Total Liquidity: ${total_liquidity:,.2f}")
    print(f"   Total Debt: ${total_debt:,.2f}")
    print(f"   Net TVL: ${total_liquidity - total_debt:,.2f}")
    
    # Collateral assets
    collateral_assets = active[active['can_be_collateral'] == True]
    print(f"\n🔒 Collateral Assets: {len(collateral_assets)}")
    print("   Top 3 by LTV:")
    top_ltv = collateral_assets.nlargest(3, 'max_ltv')[['symbol', 'max_ltv', 'liquidation_threshold']]
    for idx, row in top_ltv.iterrows():
        print(f"   {row['symbol']:8} - Max LTV: {row['max_ltv']:.1f}% | Liq Threshold: {row['liquidation_threshold']:.1f}%")

def main():
    """Main execution function"""
    
    print("=" * 70)
    print("Aave V3 Official API - Market Data Collection")
    print("=" * 70)
    print()
    
    try:
        # Get market data for Ethereum (Chain ID 1)
        data = get_market_data(chain_id=1)
        
        # Process into DataFrame
        df = process_market_data(data)

        print(df)
        
        # if df.empty:
        #     print("No data received. Please check the API.")
        #     return
        
        # # Analyze the data
        # analyze_market_data(df)
        
        # # Save to CSV
        # filename = f"aave_v3_ethereum_market_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        # df.to_csv(filename, index=False)
        # print(f"\n✅ Full market data saved to: {filename}")
        
        # # Show sample data
        # print("\n" + "=" * 70)
        # print("SAMPLE DATA (First 10 Assets)")
        # print("=" * 70)
        # print(df[['symbol', 'supply_apy', 'variable_borrow_apy', 'total_liquidity', 'utilization_rate']].head(10).to_string())
        
        # print("\n" + "=" * 70)
        # print("💡 NEXT STEPS:")
        # print("=" * 70)
        # print("1. Check other chains: get_market_data(chain_id=137)  # Polygon")
        # print("2. Query user data: get_user_reserves('0x...', chain_id=1)")
        # print("3. Get incentives: get_reserve_incentives(chain_id=1)")
        # print("4. Analyze the CSV file for deeper insights")
        
        return df
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nPossible issues:")
        print("- API might be temporarily unavailable")
        print("- Network connection issue")
        print("- Query format might need adjustment")
        return None

if __name__ == "__main__":
    df = main()