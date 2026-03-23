import pandas as pd
import json
from tqdm import tqdm
import numpy as np

pd.set_option('display.max_columns', 500)

# df = pd.read_csv("/Users/yegortrussov/Documents/ml/lending_protocols/dataset_collection/data/markets_raw/eth_cbbtc_usdt.csv")
df = pd.read_csv("/Users/yegortrussov/Documents/ml/lending_protocols/dataset_collection/data/markets_raw/eth_wsteth_usdc.csv")
# df = pd.read_csv("/Users/yegortrussov/Documents/ml/lending_protocols/dataset_collection/data/markets_raw/base_cbbtc_usdc_full.csv")
# df = df[df["datetime"] < "2026-01-01"]
with open("/Users/yegortrussov/Documents/ml/lending_protocols/dataset_collection/data/common/markets_meta.json", 'r') as f:
    markets_meta = json.load(f)
with open("/Users/yegortrussov/Documents/ml/lending_protocols/dataset_collection/data/common/assets_meta.json", 'r') as f:
    assets_meta = json.load(f)
with open("/Users/yegortrussov/Documents/ml/lending_protocols/dataset_collection/data/common/vaults_meta.json", 'r') as f:
    vaults_meta = json.load(f)
market_addr = df["market_address"].unique()[0]
market_meta = markets_meta[market_addr]
asset_meta = assets_meta[market_meta["collateral_asset_address"]]
loan_asset_meta = assets_meta[market_meta["loan_asset_address"]]
loan_asset_meta["decimals"] = 6
all_vaults_addresses = vaults_meta.keys()
asset_price_df = pd.DataFrame(asset_meta["historical_price"], columns=["timestamp", "price"]).dropna()


import numpy as np

def compute_market_rates(market_params, fee=0.0):
    rate_dict = market_params.get('rate_at_target', {})
    if not rate_dict:
        return {}

    SECONDS_PER_YEAR = 365 * 86400
    TARGET = 0.9
    KD = 4.0

    utils = np.arange(0, 1.01, 0.01)
    util_percent = utils * 100

    result = {}
    for ts, rate_wad in rate_dict.items():
        if rate_wad is None:
            continue
        rate_per_sec = rate_wad / 1e18

        # Compute error e and curve for all utilizations
        e = np.where(
            utils <= TARGET,
            (utils - TARGET) / TARGET,
            (utils - TARGET) / (1 - TARGET)
        )
        curve = np.where(
            utils <= TARGET,
            (1 - 1/KD) * e + 1,
            (KD - 1) * e + 1
        )

        # Borrow rate per second
        borrow_rate_ps = rate_per_sec * curve

        # Supply rate per second
        supply_rate_ps = borrow_rate_ps * utils * (1 - fee)

        # Convert to APR percent
        borrow_apr = borrow_rate_ps * SECONDS_PER_YEAR
        supply_apr = supply_rate_ps * SECONDS_PER_YEAR

        # Build list of [util%, borrow%, supply%]
        result[int(ts)] = [
            [util_percent[i], borrow_apr[i], supply_apr[i]]
            for i in range(len(utils))
        ]

    return result
market_irm_rates = compute_market_rates(market_meta)


def add_interest_rates(df, irm_history):
    """
    Add borrow and supply rates using historical IRM curves.
    For each row, uses the closest IRM curve with timestamp <= row['timestamp'].
    """
    # Preprocess history
    hist_items = []
    for ts, curve_list in irm_history.items():
        curve_arr = np.array(curve_list)
        u_arr = curve_arr[:, 0] / 100.0  # convert percent to decimal utilization
        b_arr = curve_arr[:, 1]           # borrow rate in percent (not divided by 100 yet)
        s_arr = curve_arr[:, 2]           # supply rate in percent
        hist_items.append((ts, (u_arr, b_arr, s_arr)))
    hist_items.sort(key=lambda x: x[0])
    hist_timestamps = np.array([item[0] for item in hist_items])
    hist_curves = [item[1] for item in hist_items]

    df = df.copy()

    # Initialize columns
    df['borrow_rate_before'] = 0.0
    df['supply_rate_before'] = 0.0
    df['borrow_rate_after'] = 0.0
    df['supply_rate_after'] = 0.0

    for idx, row in df.iterrows():
        ts = row['timestamp']
        # Find closest historical timestamp <= ts
        pos = np.searchsorted(hist_timestamps, ts, side='right') - 1
        if pos < 0:
            pos = 0  # fallback to earliest
        u_arr, b_arr, s_arr = hist_curves[pos]

        # Interpolate for before utilization
        util_before = max(0, min(row['utilization_before'], 1))
        df.at[idx, 'borrow_rate_before'] = np.interp(util_before, u_arr, b_arr)
        df.at[idx, 'supply_rate_before'] = np.interp(util_before, u_arr, s_arr)

        # Determine utilization after (may be 'new_utilization' if present)
        if 'new_utilization' in df.columns and pd.notna(row['new_utilization']):
            util_after = max(0, min(row['new_utilization'], 1))
        else:
            util_after = max(0, min(row['utilization_after'], 1))

        df.at[idx, 'borrow_rate_after'] = np.interp(util_after, u_arr, b_arr)
        df.at[idx, 'supply_rate_after'] = np.interp(util_after, u_arr, s_arr)

    return df

def add_collateral_prices(df, price_data, col="collateral_price"):
    timestamps, prices = np.array(price_data).T
    
    df = df.copy()
    
    def find_closest_price(tx_timestamp):
        idx = np.searchsorted(timestamps, tx_timestamp)
        
        if idx == 0:
            return prices[0]
        elif idx == len(timestamps):
            return prices[-1]
        else:
            left_diff = tx_timestamp - timestamps[idx-1]
            right_diff = timestamps[idx] - tx_timestamp
            
            if left_diff <= right_diff:
                return prices[idx-1]
            else:
                return prices[idx]
    
    df[col] = df['timestamp'].apply(find_closest_price)
    
    if 'assets' in df.columns and col == "collateral_price":
        df['collateral_value'] = df['assets'] * df['collateral_price']
    
    return df

def add_rolling_mean_metric(df, metric, hours=6):
    df = df.sort_values('timestamp').copy()
    df_sorted = df.reset_index(drop=True)
    
    result = []
    for i in range(len(df_sorted)):
        current_time = df_sorted.at[i, 'timestamp']
        cutoff = current_time - (hours * 3600)
        mask = (df_sorted['timestamp'] >= cutoff) & (df_sorted['timestamp'] < current_time)
        rolling_mean = df_sorted.loc[mask, metric].mean()
        result.append(rolling_mean)
    
    df_sorted[f'{metric}_rolling'] = result
    return df_sorted

def calculate_metrics(df, irm_history, asset_data, loan_asset_data, use_collateral=False, use_usd_assets=False):
    df = df.fillna(0).sort_values(['timestamp', 'hash'])
    df = df.reset_index(drop=True)
    
    metrics_rows = []
    last_timestamp = df.iloc[0]['timestamp'] if len(df) > 0 else 0
    borrow_rate = 0.0
    supply_rate = 0.0
    total_supply = 0.0
    total_borrow = 0.0
    
    i = 0
    n = len(df)
    
    # Prepare historical IRM data for fast lookup
    hist_items = []
    for ts, curve_list in irm_history.items():
        curve_arr = np.array(curve_list)
        u_arr = curve_arr[:, 0] / 100.0  # convert percent to decimal
        b_arr = curve_arr[:, 1]           # borrow percent
        s_arr = curve_arr[:, 2]           # supply percent
        hist_items.append((ts, (u_arr, b_arr, s_arr)))
    hist_items.sort(key=lambda x: x[0])
    hist_timestamps = np.array([item[0] for item in hist_items])
    hist_curves = [item[1] for item in hist_items]

    
    def get_rates_at_time(ts, util):
        # Find closest historical timestamp <= ts
        idx = np.searchsorted(hist_timestamps, ts, side='right') - 1
        if idx < 0:
            idx = 0  # fallback to earliest available
        
        u_arr, b_arr, s_arr = hist_curves[idx]
        
        # Ensure util is within bounds (0-1)
        util_clipped = np.clip(util, 0, 1)
        
        # Interpolate borrow and supply percentages
        borrow_pct = np.interp(util_clipped, u_arr, b_arr)
        supply_pct = np.interp(util_clipped, u_arr, s_arr)
        
        return borrow_pct, supply_pct

    
    while i < n:
        current_hash = df.iloc[i]['hash']
        tx_start_idx = i
        
        before_supply = total_supply
        before_borrow = total_borrow
        
        while i < n and df.iloc[i]['hash'] == current_hash:
            row = df.iloc[i]
            current_timestamp = row['timestamp']
            time_diff = (current_timestamp - last_timestamp) / (365 * 24 * 3600)  # in years

            current_util = total_borrow / total_supply if total_supply > 0 else 0
            borrow_rate, supply_rate = get_rates_at_time(current_timestamp, current_util)

            total_borrow += total_borrow * (borrow_rate * time_diff)   # Borrowers owe more
            total_supply += total_supply * (supply_rate * time_diff)   # Lenders earn more

            
            last_timestamp = current_timestamp
            
            amount = abs(0 if row['assets'] is None else float(row['assets']) / (10**loan_asset_data["decimals"]))
            if use_usd_assets:
                amount = float(row['assets']) / (10**loan_asset_data["decimals"]) if row['assets_usd'] is None else float(row["assets_usd"])
            
            if row['type'] in ['MarketSupply']:
                total_supply += amount
            elif row['type'] in ['MarketWithdraw']:
                total_supply -= amount
            if row['type'] == 'MarketBorrow':
                total_borrow += amount
            elif row['type'] == 'MarketRepay':
                total_borrow -= amount
            elif row['type'] == 'MarketLiquidation':
                total_borrow -= amount
                total_supply += amount
            
            i += 1
        
        after_supply = total_supply
        after_borrow = total_borrow
        
        before_util = before_borrow / before_supply if before_supply > 0 else 0
        after_util = after_borrow / after_supply if after_supply > 0 else 0
        
        metrics_rows.append({
            'hash': current_hash,
            'timestamp': df.iloc[tx_start_idx]['timestamp'],
            'datetime': df.iloc[tx_start_idx]['datetime'],
            'total_supply_before': before_supply,
            'total_borrow_before': before_borrow,
            'total_supply_after': after_supply,
            'total_borrow_after': after_borrow,
            'utilization_before': before_util,
            'utilization_after': after_util,
            'tx_actions': i - tx_start_idx
        })
    
    # The rest of the function remains unchanged
    res = add_interest_rates(pd.DataFrame(metrics_rows), irm_history) 
    
    print("Added interest rates")
    res = add_collateral_prices(res, asset_data["historical_price"])
    print("Added coll price")
    res = add_collateral_prices(res, loan_asset_data["historical_price"], col="loan_asset_price")
    print("Added loan asset price")
    
    return res

from tqdm import tqdm

def classify_event(start_coll, start_debt, end_coll, end_debt, types_in_tx):
    # Epsilon for zero detection (use same as in your code)
    epsilon = 1e-6
    
    # Extract event types in this transaction
    tx_types = list(set(types_in_tx))
    
    # Liquidation events
    if 'MarketLiquidation' in tx_types:
        return 'liquidation'
    
    # Calculate changes
    delta_coll = end_coll - start_coll
    delta_debt = end_debt - start_debt
    
    # Check for opening position (from near-zero to positive)
    if start_coll < epsilon and start_debt < epsilon and end_coll > epsilon and end_debt > epsilon:
        return 'position_open'
    
    # Check for closing position (to near-zero)
    if end_coll < epsilon and end_debt < epsilon and (start_coll > epsilon or start_debt > epsilon):
        return 'position_close'
    
    # Full repay (debt goes to zero, collateral may or may not change)
    if end_debt < epsilon and abs(start_debt) > epsilon:
        return 'repay_full'
    
    # Partial repay (debt decreases but not to zero)
    if delta_debt < -epsilon and end_debt > epsilon:
        return 'repay_partial'
    
    # Add collateral only
    if delta_coll > epsilon and abs(delta_debt) < epsilon:
        return 'collateral_add'
    
    # Borrow more only
    if delta_debt > epsilon and abs(delta_coll) < epsilon:
        return 'borrow_more'
    
    # Withdraw collateral only
    if delta_coll < -epsilon and abs(delta_debt) < epsilon:
        return 'collateral_withdraw'
    
    if delta_coll > epsilon and delta_debt > epsilon:
        return 'borrow_more_w_collateral'
    
    # Both collateral and debt change significantly
    if abs(delta_coll) > epsilon and abs(delta_debt) > epsilon:
        return 'position_adjust'
    
    if start_coll < epsilon and start_debt < epsilon and end_coll < epsilon and end_debt < epsilon and 'MarketSupply' in tx_types:
        return 'loan_position_supply'
    if start_coll < epsilon and start_debt < epsilon and end_coll < epsilon and end_debt < epsilon and 'MarketWithdraw' in tx_types:
        return 'loan_position_withdraw'
    
    
    return 'other'


def add_user_ltv(df, market_data):
    df = df.sort_values(['user_address', 'timestamp', 'hash'])
    
    result_rows = []
    
    for address in tqdm(df['user_address'].unique()):
        user_df = df[df['user_address'] == address].copy()
        
        collateral = 0.0
        debt = 0.0
        supply = 0.0
        
        current_hash = None
        hash_data = []
        
        for idx, row in user_df.iterrows():
            if row['hash'] != current_hash:
                if current_hash is not None and hash_data:
                    first_row = hash_data[0]
                    last_row = hash_data[-1]
                    types_in_tx = [row_dict['type'] for row_dict in hash_data]
                    event_type = classify_event(
                        start_collateral, start_debt, collateral, debt, types_in_tx
                    )
                    
                    price = first_row['collateral_price'] if 'collateral_price' in df.columns else 1.0
                    loan_asset_price = first_row['loan_asset_price']
                    if loan_asset_price is None:
                        loan_asset_price = 1
                    
                    before_ltv = start_debt / (start_collateral * price) if start_collateral * price > 0 else 0
                    after_ltv = debt / (collateral * price) if collateral * price > 0 else 0
                    
                    if (start_debt * loan_asset_price) == 0:
                        health_factor_before = 0
                    else:
                        health_factor_before = (start_collateral * price / loan_asset_price) * (float(market_data["lltv"]) / 10**18) / (start_debt * loan_asset_price)
                    
                    if (debt * loan_asset_price) == 0:
                        health_factor_after = 0
                    else:
                        health_factor_after = (collateral * price / loan_asset_price) * (float(market_data["lltv"]) / 10**18) / (debt * loan_asset_price)

                    for h_row in hash_data:
                        h_row['collateral_before'] = start_collateral
                        h_row['collateral_value_before'] = start_collateral * price
                        h_row['debt_before'] = start_debt  * loan_asset_price
                        h_row['supply_before'] = start_supply  * loan_asset_price
                        h_row['ltv_before'] = before_ltv
                        h_row['collateral_after'] = collateral
                        h_row['collateral_value_after'] = collateral * price
                        h_row['debt_after'] = debt * loan_asset_price
                        h_row['supply_after'] = supply  * loan_asset_price
                        h_row['ltv_after'] = after_ltv
                        h_row['health_factor_before'] = health_factor_before
                        h_row['health_factor_after'] = health_factor_after
                        h_row['event_type'] = event_type
                        
                        result_rows.append(h_row)
                
                current_hash = row['hash']
                hash_data = []
                start_collateral = collateral
                start_debt = debt
                start_supply = supply
            
            row_dict = row.to_dict()
            
            amount = abs(float(row['assets']))
            
            if row['type'] in ['MarketSupplyCollateral']:
                collateral += amount / (10**asset_meta["decimals"])
            elif row['type'] in ['MarketWithdrawCollateral']:
                collateral -= amount / (10**asset_meta["decimals"])
            elif row['type'] == 'MarketBorrow':
                debt += amount / (10**loan_asset_meta["decimals"])
            elif row['type'] == 'MarketRepay':
                debt -= amount / (10**loan_asset_meta["decimals"])
            elif row['type'] == 'MarketSupply':
                supply += amount / (10**loan_asset_meta["decimals"])
            elif row['type'] == 'MarketWithdraw':
                supply -= amount / (10**loan_asset_meta["decimals"])

            if abs(debt) < 1e-6:
                debt = 0 
            if abs(collateral) < 1e-11:
                collateral = 0 
            
            
            hash_data.append(row_dict)
        
        if current_hash is not None and hash_data:
            first_row = hash_data[0]
            last_row = hash_data[-1]

            types_in_tx = [row_dict['type'] for row_dict in hash_data]
            event_type = classify_event(
                start_collateral, start_debt, collateral, debt, types_in_tx
            )
            
            price = first_row['collateral_price']
            loan_asset_price = first_row['loan_asset_price']
            if loan_asset_price is None:
                loan_asset_price = 1
            
            before_ltv = (start_debt * loan_asset_price) / (start_collateral * price) if start_collateral * price > 0 else 0
            after_ltv = (debt * loan_asset_price) / (collateral * price) if collateral * price > 0 else 0
            
            if (start_debt) == 0:
                health_factor_before = 0
            else:
                health_factor_before = (start_collateral * price) * (float(market_data["lltv"]) / 10**18) / (start_debt)
            
            if (debt) == 0:
                health_factor_after = 0
            else:
                health_factor_after = (collateral * price) * (float(market_data["lltv"]) / 10**18) / (debt)

            for h_row in hash_data:
                h_row['collateral_before'] = start_collateral
                h_row['collateral_value_before'] = start_collateral * price
                h_row['debt_before'] = start_debt * loan_asset_price
                h_row['supply_before'] = start_supply  * loan_asset_price
                h_row['ltv_before'] = before_ltv
                h_row['collateral_after'] = collateral
                h_row['collateral_value_after'] = collateral * price
                h_row['debt_after'] = debt * loan_asset_price
                h_row['supply_after'] = supply  * loan_asset_price
                h_row['ltv_after'] = after_ltv
                h_row['health_factor_before'] = health_factor_before
                h_row['health_factor_after'] = health_factor_after
                h_row["event_type"] = event_type
                
                result_rows.append(h_row)
    
    result_df = pd.DataFrame(result_rows)
    result_df["health_factor_before"] = result_df["health_factor_before"].fillna(0)
    result_df["health_factor_after"] = result_df["health_factor_after"].fillna(0)
    result_df["health_factor_before"] = result_df["health_factor_before"].clip(0,1000)
    result_df["health_factor_after"] = result_df["health_factor_after"].clip(0,1000)
    
    result_df["vault_flg"] = result_df["user_address"].isin(all_vaults_addresses)

    return result_df.sort_values(["timestamp", "hash"])


def add_price_features(df, price_df, lookback_hours=[6, 24]):
    df = df.sort_values('timestamp').copy()
    price_df = price_df.sort_values('timestamp').copy()
    
    results = []
    price_values = price_df['price'].values
    price_times = price_df['timestamp'].values
    
    for _, row in df.iterrows():
        action_time = row['timestamp']
        features = {}

        zero = 0
        
        for hours in lookback_hours:
            lookback_seconds = hours * 3600
            start_time = action_time - lookback_seconds
            
            # Find indices in price data within window
            mask = (price_times >= start_time) & (price_times < action_time)
            window_prices = price_values[mask]
            
            if len(window_prices) >= 2:
                # Calculate returns
                returns = np.diff(window_prices) / window_prices[:-1]
                
                features[f'volatility_{hours}h'] = returns.std() if len(returns) > 0 else 0
                features[f'drawdown_{hours}h'] = (window_prices.min() - window_prices[-1]) / window_prices[-1]
                features[f'trend_{hours}h'] = (window_prices[-1] - window_prices[0]) / window_prices[0] if window_prices[0] != 0 else 0
            else:
                features[f'volatility_{hours}h'] = 0
                features[f'drawdown_{hours}h'] = 0
                features[f'trend_{hours}h'] = 0
        
        results.append(features)
    
    price_features_df = pd.DataFrame(results, index=df.index)
    return pd.concat([df, price_features_df], axis=1)

import os 

def compute_market_rates(market_params, fee=0.0):
    rate_dict = market_params.get('rate_at_target', {})
    if not rate_dict:
        return {}

    SECONDS_PER_YEAR = 365 * 86400
    TARGET = 0.9
    KD = 4.0

    utils = np.arange(0, 1.01, 0.01)
    util_percent = utils * 100

    result = {}
    for ts, rate_wad in rate_dict.items():
        if rate_wad is None:
            continue
        rate_per_sec = rate_wad / 1e18
        e = np.where(
            utils <= TARGET,
            (utils - TARGET) / TARGET,
            (utils - TARGET) / (1 - TARGET)
        )
        curve = np.where(
            utils <= TARGET,
            (1 - 1/KD) * e + 1,
            (KD - 1) * e + 1
        )
        borrow_rate_ps = rate_per_sec * curve
        supply_rate_ps = borrow_rate_ps * utils * (1 - fee)
        borrow_apr = borrow_rate_ps * SECONDS_PER_YEAR
        supply_apr = supply_rate_ps * SECONDS_PER_YEAR
        result[int(ts)] = [
            [util_percent[i], borrow_apr[i], supply_apr[i]]
            for i in range(len(utils))
        ]

    return result


def label_transaction_sequences(df, time_threshold_seconds=300):
    df = df.sort_values(['user_address', 'timestamp']).copy()
    df['event_sequence_type'] = df['event_type'].copy()
    inx = 0
    
    for i in tqdm(range(1, len(df))):
        # Check if same user
        if df.iloc[i]['user_address'] != df.iloc[i-1]['user_address']:
            inx = 0
            continue
        inx += 1
        addr = df.iloc[i]['user_address']
            
        # Check time difference
        time_diff = df.iloc[i]['timestamp'] - df.iloc[i-1]['timestamp']
        if time_diff > time_threshold_seconds:
            continue
        
        
        # Check for collateral + borrow sequence
        if (df.iloc[i-1]['event_type'] == 'collateral_add' and 
            df.iloc[i]['event_type'] == 'borrow_more' and inx > 1):
            df.at[df.index[i-1], 'event_sequence_type'] = 'borrow_more_w_collateral'
            df.at[df.index[i], 'event_sequence_type'] = 'borrow_more_w_collateral'
        if (df.iloc[i-1]['event_type'] == 'repay_full' and 
            df.iloc[i]['event_type'] == 'position_close'):
            df.at[df.index[i-1], 'event_sequence_type'] = 'position_close'
            df.at[df.index[i], 'event_sequence_type'] = 'position_close'
        if (df.iloc[i-1]['event_type'] == 'collateral_add' and 
            df.iloc[i]['event_type'] == 'borrow_more' and inx == 1):
            df.at[df.index[i-1], 'event_sequence_type'] = 'position_open'
            df.at[df.index[i], 'event_sequence_type'] = 'position_open'
    
    return df

def build_enriched_df(name, raw_df, market_meta, asset_data, loan_asset_data, market_irm_rates):
    metrics = calculate_metrics(
        raw_df[raw_df["datetime"].astype(str) < "2027-01-01"],
        use_collateral=False,
        # irm_data=market_meta["irm_curve"],
        irm_history=market_irm_rates,
        asset_data=asset_data,
        loan_asset_data=loan_asset_data
    )

    enriched = raw_df.merge(metrics.drop(columns=["timestamp", "datetime"]))
    print("Min date", raw_df["datetime"].min())
    asset_price_df = pd.DataFrame(asset_meta["historical_price"], columns=["timestamp", "price"]).dropna()
    enriched = add_user_ltv(enriched, market_data=market_meta)
    enriched = add_price_features(enriched, asset_price_df)
    enriched = label_transaction_sequences(enriched, 60*10)
    enriched["collateral_asset_symbol"] = asset_data["symbol"]
    enriched["loan_asset_symbol"] = loan_asset_data["symbol"]
    enriched = enriched.sort_values("timestamp")


    enriched.to_csv(f"/Users/yegortrussov/Documents/ml/lending_protocols/dataset_collection/data/markets_enriched/{name}.csv", index=False)

    return enriched


def create_market_hourly_dataset(df, asset_meta):
    # Generate hourly timestamps
    min_time = df['timestamp'].min()
    max_time = df['timestamp'].max()
    
    start_hour = (min_time // 3600) * 3600
    end_hour = ((max_time // 3600) + 1) * 3600
    
    hourly_ts = np.arange(start_hour, end_hour + 3600, 3600)
    
    # Sort events
    df_sorted = df.sort_values('timestamp')
    events_ts = df_sorted['timestamp'].values
    
    # Find last event index for each hour using searchsorted
    idx = np.searchsorted(events_ts, hourly_ts, side='right') - 1
    
    # Extract values
    result_data = []
    for i, hour_ts in tqdm(enumerate(hourly_ts)):
        if idx[i] >= 0:
            last_row = df_sorted.iloc[idx[i]]
            row_data = {
                'timestamp': hour_ts,
                'datetime': pd.to_datetime(hour_ts, unit='s'),
                'total_supply': last_row['total_supply_after'],
                'total_borrow': last_row['total_borrow_after'],
                'utilization': last_row['utilization_after'],
                'borrow_rate': last_row['borrow_rate_after'],
                'supply_rate': last_row['supply_rate_after'],
                'volatility_1h': last_row.get('volatility_1h', 0),
                'drawdown_1h': last_row.get('drawdown_1h', 0),
                'volatility_6h': last_row.get('volatility_6h', 0),
                'drawdown_6h': last_row.get('drawdown_6h', 0),
                'collateral_price': last_row.get('collateral_price', 0),
                'loan_asset_price': last_row.get('loan_asset_price', 0),
                'avg_health_factor': last_row.get('health_factor_after', 0)
            }
        else:
            row_data = {
                'timestamp': hour_ts,
                'datetime': pd.to_datetime(hour_ts, unit='s'),
                'total_supply': 0,
                'total_borrow': 0,
                'utilization': 0,
                'borrow_rate': 0,
                'supply_rate': 0,
                'volatility_1h': 0,
                'drawdown_1h': 0,
                'volatility_6h': 0,
                'drawdown_6h': 0,
                'collateral_price': 0,
                'loan_asset_price': 0,
                'avg_health_factor': 0
            }
        result_data.append(row_data)
    
    result_df = pd.DataFrame(result_data)
    
    result_df = result_df.ffill().fillna(0)
    
    result_df['borrow_rate_rolling'] = result_df['borrow_rate'].rolling(6, min_periods=1).mean()
    result_df['supply_rate_rolling'] = result_df['supply_rate'].rolling(6, min_periods=1).mean()
    
    # Add asset price
    if 'historical_price' in asset_meta and asset_meta['historical_price']:
        price_df = pd.DataFrame(asset_meta['historical_price'], columns=['timestamp', 'price'])
        price_df = price_df.dropna()
        if not price_df.empty:
            result_df = result_df.merge(price_df, on='timestamp', how='left')
            result_df['asset_price'] = result_df['price'].ffill().fillna(0)
            result_df = result_df.drop(columns=['price'])
    
    return result_df



raw_path = "/Users/yegortrussov/Documents/ml/lending_protocols/dataset_collection/data/markets_raw"

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--markets', nargs='+', help='List of items')
args = parser.parse_args()

print(args.markets)  # List of strings


# exit(0)

for file in tqdm(args.markets[0].split(' ')):
    print("processing file", file)
    # if "base" in file:
    #     continue
    raw_df = pd.read_csv(raw_path + "/" + file + ".csv")
    print(raw_df.shape)
    address = raw_df["market_address"].unique()[0]
    market_meta = markets_meta[address]
    market_irm_rates = compute_market_rates(market_meta)
    print(address)
    asset_meta = assets_meta[market_meta["collateral_asset_address"]]
    loan_asset_meta = assets_meta[market_meta["loan_asset_address"]]
    # loan_asset_meta["decimals"] = 6
    res = build_enriched_df(
        file.split(".")[0],
        raw_df,
        market_meta,
        asset_meta,
        loan_asset_meta,
        market_irm_rates,
    )

    print("creating time series df...")

    hourly_df = create_market_hourly_dataset(
        res,
        asset_meta,
    )

    hourly_df.to_csv(f"/Users/yegortrussov/Documents/ml/lending_protocols/dataset_collection/data/markets_hourly_data/{file}.csv",index=False)




