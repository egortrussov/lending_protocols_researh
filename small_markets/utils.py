import matplotlib.pyplot as plt
import numpy as np

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
def create_hourly_user_dataset(df_actions, df_market, n_hours=1, threshold_date=None):
    df_actions = df_actions.sort_values(['user_address', 'timestamp']).copy()
    df_actions = df_actions.drop_duplicates(['user_address', 'timestamp', "hash"])
    df_market = df_market.sort_values('timestamp').copy()
    
    market_timestamps = df_market['timestamp'].values
    
    result_rows = []
    
    for user, user_df in df_actions.groupby('user_address'):
        open_events = user_df[user_df['event_sequence_type'] == 'position_open']
        if open_events.empty:
            continue
        
        position_open_time = open_events.iloc[0]['timestamp']
        
        # Find first position close event after open
        close_events = user_df[(user_df['event_sequence_type'] == 'position_close') & 
                               (user_df['timestamp'] > position_open_time)]
        if user == "0xE08D97e151473A848C3d9CA3f323Cb720472D015":
            print("here")
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
        
        if user == "0xE08D97e151473A848C3d9CA3f323Cb720472D015":
            print(user_df.shape)
        
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
                'drawdown_6h': market_row['drawdown_6h'],
                'apy': 0 if 'apy' not in market_row.keys() else  market_row['apy']
            })
            
            if action_type == 'position_close':
                break
    
    return pd.DataFrame(result_rows).sort_values(["user_address", "timestamp"])


def plot_user_metrics(df, fields, user_address=None):
    """
    Plot time series metrics with action markers using Plotly.
    """
    if user_address:
        plot_df = df[df['user_address'] == user_address].copy()
        if plot_df.empty:
            print(f"No data for user {user_address}")
            return
    else:
        plot_df = df.copy()
    
    plot_df = plot_df.sort_values('timestamp')
    plot_df['datetime'] = pd.to_datetime(plot_df['timestamp'], unit='s')
    
    # Create subplot with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": len(fields) > 1}]])
    
    colors = px.colors.qualitative.Plotly

    plot_df[fields[0]] = plot_df[fields[0]].clip(0, plot_df[fields[0]].max())
    plot_df[fields[1]] = plot_df[fields[1]].clip(0, plot_df[fields[0]].max())
    
    # Add first field
    fig.add_trace(
        go.Scatter(x=plot_df['datetime'], y=plot_df[fields[0]],
                  mode='lines+markers',
                  name=fields[0],
                  line=dict(color=colors[0], width=2),
                  marker=dict(size=4)),
        secondary_y=False
    )
    
    # Add second field if exists
    if len(fields) > 1:
        fig.add_trace(
            go.Scatter(x=plot_df['datetime'], y=plot_df[fields[1]],
                      mode='lines+markers',
                      name=fields[1],
                      line=dict(color=colors[1], width=2),
                      marker=dict(size=4)),
            secondary_y=True
        )
    
    # Add action markers
    action_df = plot_df[plot_df['action'] != 'none'].copy()
    
    # Get y-axis ranges
    
    print(plot_df[fields[0]].min())
    y1_min, y1_max = plot_df[fields[0]].min(), plot_df[fields[0]].max()
    y1_min = max(y1_min,0)
    y1_range = y1_max - y1_min
    print(y1_range)
    
    for i, (idx, row) in enumerate(action_df.iterrows()):
        # Add vertical line
        fig.add_vline(x=row['datetime'], line_dash="dash", 
                     line_color="gray", opacity=0.5, line_width=1)
        
        # Add action label using first y-axis scale
        y_pos = y1_max - (i * y1_range * 0.05)
        fig.add_annotation(
            x=row['datetime'],
            y=y_pos,
            text=row['action'],
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=1,
            arrowcolor="darkgray",
            ax=40,
            ay=-20,
            font=dict(size=10),
            bgcolor="rgba(255, 255, 0, 0.7)",
            bordercolor="black",
            borderwidth=1,
            borderpad=4,
            yref="y"  # Explicitly use left axis
        )
    
    # Update layout
    title = f"User Metrics - {user_address[:10]}..." if user_address else "User Metrics - All Users"
    fig.update_layout(
        title=dict(text=title, x=0.5, font=dict(size=16)),
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="plotly_white"
    )
    
    # Update axes
    fig.update_xaxes(title_text="Time", tickformat="%Y-%m-%d %H:%M")
    fig.update_yaxes(title_text=fields[0], secondary_y=False)
    if len(fields) > 1:
        fig.update_yaxes(title_text=fields[1], secondary_y=True)
    
    fig.show()
