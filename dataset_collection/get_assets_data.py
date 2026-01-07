from queries import (
    get_vaults_query,
)
import json
import requests
import pandas as pd 
from datetime import datetime, timedelta
import time
from tqdm import tqdm

from utils import send_morpho_request


assets_address_list = [
    "0xcbB7C0000aB88B473b1f5aFd9ef808440eed33Bf",
    "0xdAC17F958D2ee523a2206206994597C13D831ec7",
]
assets_data = {}

ASSETS_QUERY = """
query {
  assetByAddress(
    address: "$address$"
  ) {
    symbol
    decimals
    historicalPriceUsd(
      options: {
        startTimestamp: 1704067200
        endTimestamp: 1767225600
        interval: HOUR
      }
    ) {
      x
      y
    }
  }
}"""


def get_data_as_json(address):
    skip=0
    asset_data = {}

    # print(ASSETS_QUERY.replace("$address$", str(address)))
    
    while 1:
        res = send_morpho_request(ASSETS_QUERY.replace("$address$", str(address)))["data"]["assetByAddress"]
        asset_data["asset_assress"] = address
        asset_data["decimals"] = res["decimals"]
        asset_data["symbol"] = res["symbol"]
        asset_data["historical_price"] = sorted([[x["x"], x["y"]] for x in res["historicalPriceUsd"]])
        return asset_data
        
        

all_assets_data = {}
for asset_address in tqdm(assets_address_list):
    all_assets_data[asset_address] = get_data_as_json(asset_address)

with open("/Users/yegortrussov/Documents/ml/lending_protocols/dataset_collection/data/common/assets_meta.json", 'w') as f:
    json.dump(all_assets_data, f, indent=4)