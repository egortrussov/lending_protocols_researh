from queries import (
    get_actions_query,
)
import requests
import pandas as pd 
from datetime import datetime, timedelta
import time

BATCH_SIZE = 100
MORPHO_GRAPHQL_API = "https://api.morpho.org/graphql"
MARKETS_HASHES = {
    "eth_cbbtc_usdc": "0x64d65c9a2d91c36d56fbc42d69e979335320169b3df63bf92789e2c8883fcc64",
    # "eth_cbbtc_usdt": "0x45671fb8d5dea1c4fbca0b8548ad742f6643300eeb8dbd34ad64a658b2b05bca",

    # "eth_wbtc_usdc": "0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49",
    # "eth_wbtc_usdt": "0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99",

    # "eth_wsteth_usdt": "0xe7e9694b754c4d4f7e21faf7223f6fa71abaeb10296a4c43a54a7977149687d2",
    # "eth_wsteth_usdc": "0xb323495f7e4148be5643a4ea4a8221eef163e4bccfdedc2a6f4696baacbc86cc",

    # "eth_weth_usdt": "0xdbffac82c2dc7e8aa781bd05746530b0068d80929f23ac1628580e27810bc0c5",
}

# MARKETS_HASHES = {
    # "base_cbbtc_usdc": "0x9103c3b4e834476c9a62ea009ba2c884ee42e94e6e314a26f04d312434191836",
    # "base_wbtc_usdc": "0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49",
    # "base_cbbtc_usdt": "0x45671fb8d5dea1c4fbca0b8548ad742f6643300eeb8dbd34ad64a658b2b05bca",
    # "base_wbtc_usdt": "0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99",

    # "base_wsteth_usdt": "0xe7e9694b754c4d4f7e21faf7223f6fa71abaeb10296a4c43a54a7977149687d2",
    # "base_wsteth_usdc": "0xb323495f7e4148be5643a4ea4a8221eef163e4bccfdedc2a6f4696baacbc86cc",

    # "base_weth_usdt": "0xdbffac82c2dc7e8aa781bd05746530b0068d80929f23ac1628580e27810bc0c5",
# }



def query_aave_graphql(query):
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': 'https://sandbox.embed.apollographql.com',
        'Access-Control-Allow-Credentials': 'true'
    }

    # print(query)
    
    response = requests.post(
        MORPHO_GRAPHQL_API,
        json={'query': query},
        headers=headers,
        timeout=100,
    )


    
    if response.status_code == 200:
        # print(response.json())
        return response.json()
    else:
        raise Exception(f"Query failed with status {response.status_code}: {response.text}")


def get_result_df(result, market):
    df = pd.DataFrame({
        "hash": [],
        "type": [],
        "timestamp": [],
        "user_address": [],
        "assets": [],
        "assets_usd": [],
        "liquidated_assets": [],
        "liquidated_assets_usd": [],
    })
    for transaction in result["data"]["transactions"]["items"]:
        if transaction["type"] == "MarketLiquidation":
            new_row = {
                "hash": transaction["hash"],
                "type": transaction["type"],
                "timestamp": transaction["timestamp"],
                "user_address": transaction["user"]["address"],
                "assets": transaction["data"]["repaidAssets"],
                "assets_usd": transaction["data"]["repaidAssetsUsd"],
                "liquidated_assets": transaction["data"]["seizedAssets"],
                "liquidated_assets_usd": transaction["data"]["seizedAssetsUsd"],
                
            }
        else:
            new_row = {
                "hash": transaction["hash"],
                "type": transaction["type"],
                "timestamp": transaction["timestamp"],
                "user_address": transaction["user"]["address"],
                "assets": transaction["data"]["assets"],
                "assets_usd": transaction["data"]["assetsUsd"],
                "liquidated_assets": 0,
                "liquidated_assets_usd": 0,
            }
        df.loc[len(df)] = new_row
    df["market"] = market
    return df


def get_actions_history(
        start_timestamp,
        end_timestamp,
        market,
        skip=0,
):
    """
    Get market data for a specific chain
    Returns reserves (assets), rates, liquidity, etc.
    """
    
    query = get_actions_query(
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        market=MARKETS_HASHES[market],
        skip=skip,
    )
    result = query_aave_graphql(query)

    result_df = get_result_df(result, market=market)
    return result_df

# hist = get_actions_history()


def process_date_range(start_date_str, end_date_str, market, csv_file_path):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")
    
    all_data = []
    current_end = end_date
    
    print(f"Processing {market} from {start_date_str} to {end_date_str}")
    
    current_start = start_date
    
    start_ts = int(current_start.timestamp())
    end_ts = int(current_end.timestamp())
    skip = 0
    pages = 0
    
    while 1:
        pages += 1
        
        daily_df = get_actions_history(start_ts, end_ts, market, skip)
        if daily_df is not None and not daily_df.empty:
            all_data.append(daily_df)
        print(f"Page {pages}, cnt = {len(daily_df)} max date {pd.to_datetime(daily_df['timestamp'].max(), unit='s')}")
        if len(daily_df) == 0 or len(daily_df) < BATCH_SIZE:
            break
        skip += len(daily_df)

        if pages % 30 == 0:
            combined_df = pd.concat(all_data, ignore_index=True)
            combined_df['datetime'] = pd.to_datetime(combined_df['timestamp'], unit='s').dt.strftime('%Y-%m-%d %H:%M:%S')
            combined_df["market_address"] = MARKETS_HASHES[market]
            combined_df.to_csv(csv_file_path, index=False)
            print(f"Saved CHECKPOINT {len(combined_df)} total events to {csv_file_path}")

    print(f"  {current_start.strftime('%Y-%m-%d')}: {len(daily_df)} events in {pages} pages")
    
    current_end = current_start
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        combined_df['datetime'] = pd.to_datetime(combined_df['timestamp'], unit='s').dt.strftime('%Y-%m-%d %H:%M:%S')
        combined_df["market_address"] = MARKETS_HASHES[market]
        combined_df.to_csv(csv_file_path, index=False)
        print(f"Saved {len(combined_df)} total events to {csv_file_path}")
        return combined_df
    
    print("No data found for the period")
    return pd.DataFrame()


def save_to_csv(dataframe, file_path):
    dataframe.to_csv(file_path, index=False)


def save_partial_data(dataframes, file_path):
    """Save partial data in case of errors"""
    if dataframes:
        partial_df = pd.concat(dataframes, ignore_index=True)
        backup_path = file_path.replace('.csv', f'_partial_{int(time.time())}.csv')
        partial_df.to_csv(backup_path, index=False)
        print(f"Partial data saved to: {backup_path}")


def get_file_size(file_path):
    """Get file size in human readable format"""
    try:
        import os
        size_bytes = os.path.getsize(file_path)
        
        # Convert to human readable format
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"
    except:
        return "Unknown"

for market in MARKETS_HASHES.keys():
    process_date_range(
        start_date_str="2023-03-31 17:26:24",
        end_date_str="2026-02-01 00:00:00",
        market=market,
        csv_file_path=f"./data/markets_raw/{market}.csv",
    )
    # break
