def get_actions_query(start_timestamp, end_timestamp, market, skip):
    query = """
    query {
    transactions(
        first: 500
        skip: $skip$
        orderBy: Timestamp
        orderDirection: Asc
        where: {
            type_in: [
                MarketWithdraw,
                MarketWithdrawCollateral,
                MarketBorrow,
                MarketRepay, 
                MarketSupply,
                MarketSupplyCollateral,
                MarketLiquidation,
            ],
            marketUniqueKey_in: [
                "market_hash"
            ],
            timestamp_gte: start_timestamp,
            timestamp_lte: end_timestamp,
        }
    ) {
        items {
            hash
            timestamp
            type
            chain {
                id
                network
                currency
            }
            user {
                address
            }
            data {
                ... on VaultTransactionData {
                shares
                assets
                assetsUsd
                vault {
                    address
                    asset {
                    symbol
                    decimals
                    }
                }
                }
                ... on MarketTransferTransactionData {
                shares
                assetsUsd
                assets
                market {
                    uniqueKey
                }
                }
                ... on MarketCollateralTransferTransactionData {
                assets
                assetsUsd
                market {
                    uniqueKey
                    
                }
                }
                ... on MarketLiquidationTransactionData {
                repaidAssets
                repaidAssetsUsd
                seizedAssets
                seizedAssetsUsd
                market {
                    uniqueKey
                }
                }
            }
        }
        }
    }
    """
    query = query.replace("start_timestamp", str(start_timestamp))
    query = query.replace("end_timestamp", str(end_timestamp))
    query = query.replace("market_hash", str(market))
    query = query.replace("$skip$", str(skip))
    
    return query
    

def get_market_historic_params(start_timestamp, end_timestamp, market, skip=0):
    query = """
    query {
    marketByUniqueKey(
        uniqueKey: "market_hash",
    ) {
        historicalState {
            borrowApy(
                options: {
                startTimestamp: start_timestamp
                endTimestamp: end_timestamp
                interval: HOUR,
            }) {
                x,
                y
            }

            supplyApy(
                options: {
                startTimestamp: start_timestamp
                endTimestamp: end_timestamp
                interval: HOUR,
            }) {
                x,
                y
            }
        }
    }
    }
    """
    query = query.replace("start_timestamp", str(start_timestamp))
    query = query.replace("end_timestamp", str(end_timestamp))
    query = query.replace("market_hash", str(market))
    query = query.replace("$skip$", str(skip))
    
    return query
    


def get_vaults_query(start_timestamp, end_timestamp, vault, skip):
    query = """
    query {
    transactions(
        first: 500
        skip: $skip$
        orderBy: Timestamp
        orderDirection: Asc
        where: {
            type_in: [
                MetaMorphoWithdraw,
                MetaMorphoTransfer,
                MetaMorphoDeposit,
                MetaMorphoFee
            ],
            vaultAddress_in: [
                "vault_hash"
            ],
            timestamp_gte: start_timestamp,
            timestamp_lte: end_timestamp,
        }
    ) {
        items {
            blockNumber
            hash
            type
            timestamp
            user {
                address
            }
            data {
                ... on VaultTransactionData {
                    shares
                    assets
                    assetsUsd
                }
            }
        }
    }
    }
    """
    query = query.replace("start_timestamp", str(start_timestamp))
    query = query.replace("end_timestamp", str(end_timestamp))
    query = query.replace("vault_hash", str(vault))
    query = query.replace("$skip$", str(skip))
    
    return query
    