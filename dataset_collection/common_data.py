from queries import (
    get_vaults_query,
)
from utils import (
    send_morpho_request
)
import json
import requests
import pandas as pd 
from datetime import datetime, timedelta
import time

MORPHO_GRAPHQL_API = "https://api.morpho.org/graphql"

def query_aave_graphql(query):
    headers = {
        'Content-Type': 'application/json',
    }
    
    response = requests.post(
        MORPHO_GRAPHQL_API,
        json={'query': query},
        headers=headers
    )
    
    if response.status_code == 200:
        # print(response.json())
        return response.json()
    else:
        raise Exception(f"Query failed with status {response.status_code}: {response.text}")

VALUTS_QUERY = """
query {
  vaults(first: 500, skip: $skip$, where: {
    chainId_in: [1, 8453],
    listed: true,
  }) {
    items {
      address
      symbol
      name
      asset {
        id
        address
        decimals
        symbol
      }
      chain {
        id
        network
      }
    }
  }
}

"""

# valuts_data = {
#     "address": [],
#     "symbol": [],
#     "name": [],
#     "asset_address": [],
#     "asset_symbol": [],
#     "asset_decimals": [],
#     "network": [],
# }

# skip=0
# while 1:
#     res = query_aave_graphql(VALUTS_QUERY.replace("$skip$", str(skip)))["data"]["vaults"]["items"]
#     if len(res) == 0:
#         break
#     skip += len(res)
#     print("processing", skip)

#     for item in res:
#         valuts_data["address"].append(item["address"])
#         valuts_data["symbol"].append(item["symbol"])
#         valuts_data["name"].append(item["name"])
#         valuts_data["network"].append("eth" if item["chain"]["id"] == 1 else "base")
#         valuts_data["asset_address"].append(item["asset"]["id"])
#         valuts_data["asset_symbol"].append(item["asset"]["symbol"])
#         valuts_data["asset_decimals"].append(item["asset"]["decimals"])


# valuts_data = pd.DataFrame(valuts_data)
# print("PROCESSED VAULTS")
# valuts_data.to_csv("./data/common/vaults_meta.csv", index=False)

import pandas as pd
import os
markets_list = []
raw_path = "/Users/yegortrussov/Documents/ml/lending_protocols/dataset_collection/data/markets_raw"

for file in os.listdir(raw_path):
    markets_list.append(
        pd.read_csv(raw_path + "/" + file)["market_address"].unique()[0]
    )

MARKETS_QUERY = """
query {
  markets(first: 1, skip: $skip$, where: {
    chainId_in: [1, 8453],
    listed: true,
    uniqueKey_in: $market_ids$
  }) {
    items {
      uniqueKey
      lltv
      creationTimestamp,
      oracle {
        address
      }
      irmAddress
      historicalState {
        rateAtTarget(options: {
          interval: HOUR
        }) {
          x
          y
        }
      }
      currentIrmCurve {
        utilization
        borrowApy
        supplyApy
      }
      loanAsset {
        address
        symbol
        decimals
        chain {
            id
        }
      }
      collateralAsset {
        address
        symbol
        decimals
      }
    }
  }
}
""".replace("$market_ids$", str(markets_list)).replace("'", '"')

def get_data_as_json(query, dest):

    
    skip=0
    all_markets_data = {}
    while 1:
        res = query_aave_graphql(query.replace("$skip$", str(skip)))["data"]["markets"]["items"]
        if len(res) == 0:
            break
        skip += len(res)
        print("processing", skip)
        
        for item in res:
            if item["collateralAsset"] is None or item["oracle"] is None:
                continue
            current_market = {}
            current_market["address"] = (item["uniqueKey"])
            current_market["lltv"] = (item["lltv"])
            current_market["oracle_address"] = (item["oracle"]["address"])
            current_market["creation_datetime"] = (item["creationTimestamp"])
            current_market["network"] = ("eth" if item["loanAsset"]["chain"]["id"] == 1 else "base")

            current_market["loan_asset_address"] = (item["loanAsset"]["address"])
            current_market["loan_asset_symbol"] = (item["loanAsset"]["symbol"])
            current_market["loan_asset_decimals"] = (item["loanAsset"]["decimals"])
            
            current_market["collateral_asset_address"] = (item["collateralAsset"]["address"])
            current_market["collateral_asset_symbol"] = (item["collateralAsset"]["symbol"])
            current_market["collateral_asset_decimals"] = (item["collateralAsset"]["decimals"])

            current_market["rate_at_target"] = {
              x["x"]: x["y"] for x in item["historicalState"]["rateAtTarget"]
            }

            
            irm_curve_data = []
            for i in item["currentIrmCurve"]:
                irm_curve_data.append([
                    i["utilization"],
                    i["borrowApy"],
                    i["supplyApy"],
                ])
            current_market["irm_curve"] = irm_curve_data

            all_markets_data[current_market["address"]] = current_market

    with open(dest, 'w') as f:
        json.dump(all_markets_data, f, indent=4)


get_data_as_json(MARKETS_QUERY, dest="./data/common/markets_meta.json")

# get_data_as_json(MARKETS_QUERY, dest="./data/common/markets_meta.json")



# VALUTS_QUERY = """
# query {
#   vaults(first: 500, skip: $skip$, where: {
#     chainId_in: [1, 8453],
#     listed: true,
#   }) {
#     items {
#       address
#       symbol
#       name
#       asset {
#         id
#         address
#         decimals
#         symbol
#       }
#       chain {
#         id
#         network
#       }
#     }
#   }
# }
# """


# def get_vaults_data_as_json(query, dest):

    
#     skip=0
#     all_vaults_data = {}
#     while 1:
#         res = send_morpho_request(query.replace("$skip$", str(skip)))["data"]["vaults"]["items"]
#         if len(res) == 0:
#             break
#         skip += len(res)
#         print("processing", skip)
        
#         for item in res:
#             # if item["collateralAsset"] is None or item["oracle"] is None:
#             #     continue
#             current_vault = {}

#             current_vault["address"] = item["address"]
#             current_vault["symbol"] = item["symbol"]
#             current_vault["name"] = item["name"]
#             current_vault["network"] = "eth" if item["chain"]["id"] == 1 else "base"
#             current_vault["asset_address"] = item["asset"]["id"]
#             current_vault["asset_symbol"] = item["asset"]["symbol"]
#             current_vault["asset_decimals"] = item["asset"]["decimals"]
            
#             all_vaults_data[current_vault["address"]] = current_vault

#     with open(dest, 'w') as f:
#         json.dump(all_vaults_data, f, indent=4)

# get_vaults_data_as_json(VALUTS_QUERY, dest="./data/common/vaults_meta.json")
