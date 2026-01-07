from queries import (
    get_vaults_query,
)
import requests
import pandas as pd 
from datetime import datetime, timedelta
import time

BATCH_SIZE = 500
MORPHO_GRAPHQL_API = "https://api.morpho.org/graphql"
VAULTS_HASHES = {
    "steakhouse_usdc": "0xBEEF01735c132Ada46AA9aA4c54623cAA92A64CB",
    # "smokehouse_usdc": "0xBEeFFF209270748ddd194831b3fa287a5386f5bC",
}

def query_aave_graphql(query):
    headers = {
        'Content-Type': 'application/json',
    }
    
    response = requests.post(
        MORPHO_GRAPHQL_API,
        json={'query': query},
        headers=headers,
    )
    
    if response.status_code == 200:
        # print(response.json())
        return response.json()
    else:
        raise Exception(f"Query failed with status {response.status_code}: {response.text}")


def get_result_df(result, vault):
    df = pd.DataFrame({
        "hash": [],
        "type": [],
        "timestamp": [],
        "user_address": [],
        "assets": [],
        "assets_usd": [],
    })
    for transaction in result["data"]["transactions"]["items"]:
        new_row = {
            "hash": transaction["hash"],
            "type": transaction["type"],
            "timestamp": transaction["timestamp"],
            "user_address": transaction["user"]["address"],
            "assets": transaction["data"]["assets"],
            "assets_usd": transaction["data"]["assetsUsd"],
        }
        df.loc[len(df)] = new_row
    df["vault"] = vault
    return df


def get_actions_history(
        start_timestamp,
        end_timestamp,
        vault,
        skip=0,
):
    """
    Get vault data for a specific chain
    Returns reserves (assets), rates, liquidity, etc.
    """
    
    query = get_vaults_query(
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        vault=VAULTS_HASHES[vault],
        skip=skip,
    )
    result = query_aave_graphql(query)

    result_df = get_result_df(result, vault=vault)
    return result_df

# hist = get_actions_history()


def process_date_range(start_date_str, end_date_str, vault, csv_file_path):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    all_data = []
    current_end = end_date
    
    print(f"Processing {vault} from {start_date_str} to {end_date_str}")
    
    current_start = start_date
    
    start_ts = int(current_start.timestamp())
    end_ts = int(current_end.timestamp())
    skip = 0
    pages = 0
    
    while 1:
        pages += 1
        
        daily_df = get_actions_history(start_ts, end_ts, vault, skip)
        if daily_df is not None and not daily_df.empty:
            all_data.append(daily_df)
        print(f"Page {pages}, cnt = {len(daily_df)} max date {pd.to_datetime(daily_df['timestamp'].max(), unit='s')}")
        if len(daily_df) == 0 or len(daily_df) < BATCH_SIZE:
            break
        skip += BATCH_SIZE

        if pages % 50 == 0:
            combined_df = pd.concat(all_data, ignore_index=True)
            combined_df['datetime'] = pd.to_datetime(combined_df['timestamp'], unit='s').dt.strftime('%Y-%m-%d %H:%M:%S')
            combined_df["vault_address"] = VAULTS_HASHES[vault]
            combined_df.to_csv(csv_file_path, index=False)
            print(f"Saved CHECKPOINT {len(combined_df)} total events to {csv_file_path}")
    print(f"  {current_start.strftime('%Y-%m-%d')}: {len(daily_df)} events in {pages} pages")
    
    current_end = current_start
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        combined_df['datetime'] = pd.to_datetime(combined_df['timestamp'], unit='s').dt.strftime('%Y-%m-%d %H:%M:%S')
        combined_df["vault_address"] = VAULTS_HASHES[vault]
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

for vault in VAULTS_HASHES.keys():
    process_date_range(
        start_date_str="2023-01-01",
        end_date_str="2026-01-01",
        vault=vault,
        csv_file_path=f"./data/vaults_raw/{vault}.csv",
    )
    # break
