import pandas as pd
import numpy as np

def leave_valid_chains(chains_df, prefix="", len_lim=10, leave_first_k=None, contains_event=None):
    df_prep = chains_df[chains_df["event_chain"].str.startswith(prefix) & (chains_df["total_events"] < len_lim)]
    if contains_event:
        df_prep = df_prep[df_prep["event_chain"].str.contains(contains_event)]
    if leave_first_k is not None:
        df_prep['event_chain'] = df_prep['event_chain'].str.split('→').str[:leave_first_k].str.join('→').str.strip()
    return df_prep

def select_users_by_period(df_actions, start_date, end_date, threshold_date=None):
    start_ts = int(pd.Timestamp(start_date).timestamp())
    end_ts = int(pd.Timestamp(end_date).timestamp())
    
    # Get all position_open events
    open_events = df_actions[df_actions['event_sequence_type'] == 'position_open'].copy()
    users_in_period = open_events[(open_events['timestamp'] >= start_ts) & 
                                   (open_events['timestamp'] <= end_ts)][['user_address', 'timestamp']].copy()
    users_in_period = users_in_period.rename(columns={'timestamp': 'open_time'})
    
    user_actions = df_actions[df_actions['user_address'].isin(users_in_period['user_address'].unique())].copy()
    
    filtered_dfs = []
    for user in users_in_period['user_address'].unique():
        user_open = users_in_period[users_in_period['user_address'] == user]['open_time'].iloc[0]
        user_df = user_actions[user_actions['user_address'] == user].copy()
        
        close_events = user_df[(user_df['event_sequence_type'] == 'position_close') & 
                               (user_df['timestamp'] > user_open)]
        
        if not close_events.empty:
            close_time = close_events.iloc[0]['timestamp']
            # Keep events between open and first close (inclusive)
            user_df = user_df[(user_df['timestamp'] >= user_open) & 
                             (user_df['timestamp'] <= close_time)]
        else:
            # No close, keep all events after open
            user_df = user_df[user_df['timestamp'] >= user_open]
            
            if threshold_date:
                threshold_ts = int(pd.Timestamp(threshold_date).timestamp())
                user_df = user_df[user_df['timestamp'] <= threshold_ts]
        
        filtered_dfs.append(user_df)
    
    result = pd.concat(filtered_dfs, ignore_index=True) if filtered_dfs else pd.DataFrame()
    return result.sort_values(['user_address', 'timestamp'])


def create_hourly_user_dataset(df_actions, df_market, n_hours=1, threshold_date=None, start_with_open=True, additional_action_features=[]):
    df_actions = df_actions.sort_values(['user_address', 'timestamp']).copy()
    df_actions = df_actions.drop_duplicates(['user_address', 'timestamp'])
    df_market = df_market.sort_values('timestamp').copy()
    
    market_timestamps = df_market['timestamp'].values
    
    result_rows = []
    
    for user, user_df in df_actions.groupby('user_address'):
        # Find position open event
        open_events = user_df[user_df['event_sequence_type'] == 'position_open']
        if open_events.empty and start_with_open:
            continue
        
        position_open_time = user_df["timestamp"].min() if len(open_events) == 0 else open_events.iloc[0]['timestamp']
        
        # Find first position close event after open
        close_events = user_df[(user_df['event_sequence_type'] == 'position_close') & 
                               (user_df['timestamp'] > position_open_time)]
        
        if not close_events.empty:
            close_time = close_events.iloc[0]['timestamp']
        else:
            if threshold_date:
                threshold_ts = int(pd.Timestamp(threshold_date).timestamp())
                close_time = threshold_ts
            elif start_with_open:
                continue
            else:
                close_time = user_df["timestamp"].max()
        
        # Get actions between open and close (inclusive)
        user_df = user_df[(user_df['timestamp'] >= position_open_time) & 
                         (user_df['timestamp'] <= close_time)].copy()
        
        if user_df.empty:
            continue
        
        hours_step = n_hours * 3600
        user_hours = np.arange(position_open_time, close_time + hours_step, hours_step)
        
        # Create mapping of timestamp to state after action
        state_map = {}
        for _, action in user_df.iterrows():
            state_map[action['timestamp']] = {
                'collateral': action['collateral_after'],
                'debt': action['debt_after'],
                'supply': action['supply_after'],
                'event_type': action['event_sequence_type'],
                # **{
                #     f: action[f] for f in additional_action_features
                # }
            }
        
        # Initialize with first state
        first_state = state_map[user_df.iloc[0]['timestamp']]
        collateral = first_state['collateral']
        debt = first_state['debt']
        
        for hour_ts in user_hours:
            market_idx = np.searchsorted(market_timestamps, hour_ts, side='right') - 1
            if market_idx < 0:
                continue
            market_row = df_market.iloc[market_idx]

            additional_feats_dict = {}
            
            # Find closest action <= current hour
            actions_before = [ts for ts in state_map.keys() if ts <= hour_ts]
            if actions_before:
                closest_ts = max(actions_before)
                collateral = state_map[closest_ts]['collateral']
                debt = state_map[closest_ts]['debt']
                supply = state_map[closest_ts]['supply']
                current_event = state_map[closest_ts]['event_type']

                # for f in additional_action_features:
                #     additional_feats_dict[f] = state_map[closest_ts][f]
                
                # Check if this is the closing action
                if current_event == 'position_close' and abs(closest_ts - hour_ts) < hours_step:
                    action_type = 'position_close'
                elif abs(closest_ts - hour_ts) < hours_step:
                    action_type = current_event
                else:
                    action_type = 'none'
            else:
                action_type = 'none'
            
            if abs(debt) < 1e-6:
                debt = 0
            if abs(collateral) < 1e-11:
                collateral = 0
            
            collateral_price = market_row['collateral_price']
            loan_price = market_row['loan_asset_price'] if market_row['loan_asset_price'] > 0 else 1
            
            ltv = (debt * loan_price) / (collateral * collateral_price) if collateral * collateral_price > 0 else 0
            
            result_rows.append({
                'user_address': user,
                'timestamp': hour_ts,
                'datetime': pd.to_datetime(hour_ts, unit='s'),
                'collateral': collateral,
                'debt': debt,
                'supply': supply,
                'ltv': ltv,
                'action': action_type,
                'total_supply': market_row['total_supply'],
                'total_borrow': market_row['total_borrow'],
                'market_utilization': market_row['utilization'],
                'borrow_rate': market_row['borrow_rate'],
                'supply_rate': market_row['supply_rate'],
                'borrow_rate_rolling': market_row['borrow_rate_rolling'],
                'supply_rate_rolling': market_row['supply_rate_rolling'],
                'collateral_price': collateral_price,
                'loan_asset_price': loan_price,
                'volatility_6h': market_row['volatility_6h'],
                'drawdown_6h': market_row['drawdown_6h'],

                # **additional_feats_dict
                **{
                    f: market_row[f] for f in additional_action_features
                }
            })
            
            if action_type == 'position_close':
                break
    
    return pd.DataFrame(result_rows).sort_values(["user_address", "timestamp"])


import numpy as np
import pandas as pd


def compute_position_metrics(hourly_df, user_address):
    """
    Compute yield, interest, and net profit for a user's position from hourly data.
    Collateral is PT (Principal Token) – its USD value grows at implied_apy.
    Debt is in USD and grows at borrow_rate (APR).
    """
    user_hourly_df = hourly_df[hourly_df["user_address"] == user_address]
    df = user_hourly_df.sort_values('timestamp').copy()
    
    total_yield_usd = 0.0
    total_interest_usd = 0.0
    total_collateral_usd_time = 0.0
    total_debt_usd_time = 0.0
    total_time = 0.0
    
    for i in range(1, len(df)):
        prev = df.iloc[i-1]
        curr = df.iloc[i]
        
        dt = (curr['timestamp'] - prev['timestamp']) / (365 * 24 * 3600)  # years
        
        # Collateral and debt in USD at start of interval
        coll_usd_prev = prev['collateral']
        debt_usd_prev = prev['debt']
        
        # Continuous rates from annual percentages
        r_collateral = np.log(1 + prev['implied_apy'])
        r_borrow = np.log(1 + prev['borrow_rate'])
        
        # Growth factors
        yield_factor = np.exp(r_collateral * dt) - 1
        interest_factor = np.exp(r_borrow * dt) - 1
        
        yield_usd = coll_usd_prev * yield_factor
        interest_usd = debt_usd_prev * interest_factor
        
        total_yield_usd += yield_usd
        total_interest_usd += interest_usd
        
        # Accumulate time-weighted USD for averages
        total_collateral_usd_time += coll_usd_prev * dt
        total_debt_usd_time += debt_usd_prev * dt
        total_time += dt
    
    # Effective annualized rates (as decimals)
    if total_collateral_usd_time > 0 and total_time > 0:
        effective_yield_rate = total_yield_usd / total_collateral_usd_time / total_time
    else:
        effective_yield_rate = 0.0
    if total_debt_usd_time > 0 and total_time > 0:
        effective_borrow_rate = total_interest_usd / total_debt_usd_time / total_time
    else:
        effective_borrow_rate = 0.0
    
    # Convert to percentages
    effective_yield_apy = effective_yield_rate * 100
    effective_borrow_apr = effective_borrow_rate * 100
    
    # Initial and final USD values
    first = df.iloc[0]
    last = df.iloc[-1]
    initial_collateral_usd = first['collateral']
    final_collateral_usd = last['collateral']
    initial_debt_usd = first['debt']
    final_debt_usd = last['debt']
    
    # Average USD over the period
    avg_collateral_usd = total_collateral_usd_time / total_time if total_time > 0 else 0
    avg_debt_usd = total_debt_usd_time / total_time if total_time > 0 else 0
    
    return {
        'total_yield_usd': total_yield_usd,
        'total_interest_usd': total_interest_usd,
        'net_profit_usd': total_yield_usd - total_interest_usd,
        'avg_collateral_usd': avg_collateral_usd,
        'avg_debt_usd': avg_debt_usd,
        'effective_yield_apy': effective_yield_apy,
        'effective_borrow_apr': effective_borrow_apr,
        'position_days': total_time * 365,
        'initial_collateral_usd': initial_collateral_usd,
        'final_collateral_usd': final_collateral_usd,
        'initial_debt_usd': initial_debt_usd,
        'final_debt_usd': final_debt_usd,
        'open_timestamp': first['timestamp'],
        'close_timestamp': last['timestamp']
    }
