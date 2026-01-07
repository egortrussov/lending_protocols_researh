import requests
import pandas as pd
from datetime import datetime, timedelta
import json
import time

# Free RPC Endpoints (choose one)
RPC_ENDPOINTS = {
    'alchemy': 'https://eth-mainnet.g.alchemy.com/v2/demo',  # Free demo endpoint
    'infura': 'https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161',  # Public endpoint
    'cloudflare': 'https://cloudflare-eth.com',  # Cloudflare's free endpoint
}

# Aave V3 Pool Contract Address (Ethereum Mainnet)
AAVE_V3_POOL = '0x87870Bca3F3fD6335C3F4ce8392D69350B4fA4E2'

# Event signatures for Aave V3
EVENT_SIGNATURES = {
    'Supply': '0x2b627736bca15cd5381dcf80b0bf11fd197d01a037c52b927a881a10fb73ba61',
    'Withdraw': '0x3115d1449a7b732c986cba18244e897a450f61e1bb8d589cd2e69e6c8924f9f7',
    'Borrow': '0xb3d084820fb1a9decffb176436bd02558d15fac9b0ddfed8c465bc7359d7dce0',
    'Repay': '0xa534c8dbe71f871f9f3530e97a74601fea17b426cae02e1c5aee42c96c784051',
}

def query_events_via_rpc(event_signature, from_block, to_block, rpc_url):
    """Query events from Ethereum using RPC"""
    
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getLogs",
        "params": [{
            "address": AAVE_V3_POOL,
            "topics": [event_signature],
            "fromBlock": hex(from_block),
            "toBlock": hex(to_block)
        }],
        "id": 1
    }
    
    response = requests.post(rpc_url, json=payload)
    if response.status_code == 200:
        result = response.json()
        if 'result' in result:
            return result['result']
    return []

def get_latest_block(rpc_url):
    """Get the latest block number"""
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }
    response = requests.post(rpc_url, json=payload)
    if response.status_code == 200:
        print(response.json())
        return int(response.json()['result'], 16)
    return None

def decode_supply_event(log):
    """Decode Supply event data"""
    try:
        # Topics: [signature, reserve (indexed), user (indexed), onBehalfOf (indexed)]
        reserve = '0x' + log['topics'][1][-40:]  # Last 40 chars = address
        user = '0x' + log['topics'][2][-40:]
        on_behalf_of = '0x' + log['topics'][3][-40:]
        
        # Data contains: amount, referralCode
        data = log['data'][2:]  # Remove '0x'
        amount = int(data[:64], 16)  # First 32 bytes
        
        return {
            'action_type': 'deposit',
            'tx_hash': log['transactionHash'],
            'block_number': int(log['blockNumber'], 16),
            'reserve': reserve,
            'user': user,
            'on_behalf_of': on_behalf_of,
            'amount': amount / 1e18,  # Convert from Wei
        }
    except Exception as e:
        return None

def decode_borrow_event(log):
    """Decode Borrow event data"""
    try:
        reserve = '0x' + log['topics'][1][-40:]
        user = '0x' + log['topics'][2][-40:]
        on_behalf_of = '0x' + log['topics'][3][-40:]
        
        data = log['data'][2:]
        amount = int(data[:64], 16)
        
        return {
            'action_type': 'borrow',
            'tx_hash': log['transactionHash'],
            'block_number': int(log['blockNumber'], 16),
            'reserve': reserve,
            'user': user,
            'on_behalf_of': on_behalf_of,
            'amount': amount / 1e18,
        }
    except Exception as e:
        return None

def collect_rpc_data(days_back=1, rpc_provider='cloudflare'):
    """
    Collect Aave data using direct RPC calls
    This is FREE and RELIABLE - no API keys needed!
    """
    
    rpc_url = RPC_ENDPOINTS[rpc_provider]
    print(f"Using RPC endpoint: {rpc_provider}")
    print(f"Collecting data from last {days_back} days...\n")
    
    # Get latest block
    latest_block = get_latest_block(rpc_url)
    if not latest_block:
        print("Error: Could not fetch latest block")
        return pd.DataFrame()
    
    print(f"Latest block: {latest_block}")
    
    # Estimate blocks for time period (1 block ≈ 12 seconds)
    blocks_per_day = 7200  # Approximately
    from_block = latest_block - (blocks_per_day * days_back)
    
    print(f"Scanning from block {from_block} to {latest_block}")
    print(f"Estimated block range: {latest_block - from_block} blocks\n")
    
    all_events = []
    
    # Collect Supply (Deposit) events
    print("Collecting Supply events...")
    supply_logs = query_events_via_rpc(
        EVENT_SIGNATURES['Supply'], 
        from_block, 
        latest_block, 
        rpc_url
    )
    print(f"Found {len(supply_logs)} supply events")
    
    for log in supply_logs[:100]:  # Limit to 100 for POC
        event = decode_supply_event(log)
        if event:
            all_events.append(event)
    
    time.sleep(1)  # Be nice to the API
    
    # Collect Borrow events
    print("Collecting Borrow events...")
    borrow_logs = query_events_via_rpc(
        EVENT_SIGNATURES['Borrow'], 
        from_block, 
        latest_block, 
        rpc_url
    )
    print(f"Found {len(borrow_logs)} borrow events")
    
    for log in borrow_logs[:100]:  # Limit to 100 for POC
        event = decode_borrow_event(log)
        if event:
            all_events.append(event)
    
    if not all_events:
        print("\nNo events found. Try increasing days_back parameter.")
        return pd.DataFrame()
    
    df = pd.DataFrame(all_events)
    return df

print(collect_rpc_data())