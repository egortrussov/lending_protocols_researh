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


def create_hourly_user_dataset(df_actions, df_market, n_hours=1, threshold_date=None):
    df_actions = df_actions.sort_values(['user_address', 'timestamp']).copy()
    df_actions = df_actions.drop_duplicates(['user_address', 'timestamp'])
    df_market = df_market.sort_values('timestamp').copy()
    
    market_timestamps = df_market['timestamp'].values
    
    result_rows = []
    
    for user, user_df in df_actions.groupby('user_address'):
        # Find position open event
        open_events = user_df[user_df['event_sequence_type'] == 'position_open']
        if open_events.empty:
            continue
        
        position_open_time = open_events.iloc[0]['timestamp']
        
        # Find first position close event after open
        close_events = user_df[(user_df['event_sequence_type'] == 'position_close') & 
                               (user_df['timestamp'] > position_open_time)]
        
        if not close_events.empty:
            close_time = close_events.iloc[0]['timestamp']
        else:
            if threshold_date:
                threshold_ts = int(pd.Timestamp(threshold_date).timestamp())
                close_time = threshold_ts
            else:
                continue
        
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
                'event_type': action['event_sequence_type']
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
            
            # Find closest action <= current hour
            actions_before = [ts for ts in state_map.keys() if ts <= hour_ts]
            if actions_before:
                closest_ts = max(actions_before)
                collateral = state_map[closest_ts]['collateral']
                debt = state_map[closest_ts]['debt']
                current_event = state_map[closest_ts]['event_type']
                
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
                'ltv': ltv,
                'action': action_type,
                'total_supply': market_row['total_supply'],
                'total_borrow': market_row['total_borrow'],
                'market_utilization': market_row['utilization'],
                'borrow_rate': market_row['borrow_rate'],
                'supply_rate': market_row['supply_rate'],
                'collateral_price': collateral_price,
                'loan_asset_price': loan_price,
                'volatility_6h': market_row['volatility_6h'],
                'drawdown_6h': market_row['drawdown_6h']
            })
            
            if action_type == 'position_close':
                break
    
    return pd.DataFrame(result_rows).sort_values(["user_address", "timestamp"])

