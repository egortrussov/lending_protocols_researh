import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
def plot_user_metrics(df, fields, user_address=None, dates_range=None, lookback_hours=None, y_ranges=None):
    """
    Plot time series metrics with action markers using Plotly.
    If lookback_hours is provided, includes extra rows before the user's first timestamp,
    using market data from the same df (lookup by timestamp). Only the fields in `fields`
    are populated from market data; user-specific fields (ltv, debt, collateral) are zero.
    
    y_ranges: optional dict mapping field names to [lower, upper] for y-axis limits.
              Example: {'ltv': [0, 1], 'borrow_rate': [0, 0.1]}
    """
    if user_address:
        plot_df = df[df['user_address'] == user_address].copy()
        if plot_df.empty:
            print(f"No data for user {user_address}")
            return
    else:
        plot_df = df.copy()
    print(f"""
    User {user_address}
    Max debt {plot_df["debt"].max()}
    Max LTV {plot_df["ltv"].max()}
    Position opens {plot_df[plot_df["action"] == "position_open"].shape[0]}
    """)

    # --- Add lookback data if requested ---
    if lookback_hours is not None:
        # Build market lookup: for each timestamp, get values of the fields we need
        market_lookup = {}
        ts_list = sorted(df['timestamp'].unique())
        for ts in ts_list:
            row = df[df['timestamp'] == ts].iloc[0]
            market_lookup[ts] = {field: row[field] for field in fields if field in row.index}

        first_ts = plot_df['timestamp'].min()
        lookback_seconds = lookback_hours * 3600
        start_ts = first_ts - lookback_seconds

        # Determine step size (use existing step or default to 3600)
        if len(plot_df) > 1:
            step = plot_df['timestamp'].iloc[1] - plot_df['timestamp'].iloc[0]
        else:
            step = 3600

        extra_timestamps = np.arange(start_ts, first_ts, step)
        if len(extra_timestamps) == 0:
            extra_timestamps = []

        extra_rows = []
        cols = plot_df.columns.tolist()
        for ts in extra_timestamps:
            # Find nearest market timestamp <= ts
            idx = np.searchsorted(ts_list, ts, side='right') - 1
            if idx < 0:
                continue
            nearest_ts = ts_list[idx]
            market_vals = market_lookup[nearest_ts]

            # Start with a dict of zeros for user fields
            row = {col: 0.0 for col in cols if col not in ['user_address', 'timestamp', 'datetime']}
            # Override with market values for fields
            for field, val in market_vals.items():
                row[field] = val
            # Set required fields
            row['user_address'] = user_address
            row['timestamp'] = ts
            row['datetime'] = pd.to_datetime(ts, unit='s')
            extra_rows.append(row)

        if extra_rows:
            extra_df = pd.DataFrame(extra_rows)
            # Ensure all columns match plot_df
            for col in cols:
                if col not in extra_df.columns:
                    extra_df[col] = 0.0
            plot_df = pd.concat([extra_df[cols], plot_df], ignore_index=True).sort_values('timestamp')

    # --- Rest of the plotting code ---
    if 'ltv' in plot_df.columns:
        plot_df["ltv"] = plot_df["ltv"].clip(0, 1)

    if dates_range is not None:
        plot_df = plot_df[(plot_df["datetime"] >= dates_range[0]) & (plot_df["datetime"] <= dates_range[1])]

    plot_df = plot_df.sort_values('timestamp')
    plot_df['datetime'] = pd.to_datetime(plot_df['timestamp'], unit='s')

    fig = make_subplots(specs=[[{"secondary_y": len(fields) > 1}]])
    colors = px.colors.qualitative.Plotly

    plot_df[fields[0]] = plot_df[fields[0]].clip(0, plot_df[fields[0]].max())

    fig.add_trace(
        go.Scatter(x=plot_df['datetime'], y=plot_df[fields[0]],
                  mode='lines+markers',
                  name=fields[0],
                  line=dict(color=colors[0], width=2),
                  marker=dict(size=4)),
        secondary_y=False
    )

    if len(fields) > 1:
        fig.add_trace(
            go.Scatter(x=plot_df['datetime'], y=plot_df[fields[1]],
                      mode='lines+markers',
                      name=fields[1],
                      line=dict(color=colors[1], width=2),
                      marker=dict(size=4)),
            secondary_y=True
        )

    action_df = plot_df[plot_df['action'] != 'none'].copy()
    if not action_df.empty and fields:
        y1_min, y1_max = plot_df[fields[0]].min(), plot_df[fields[0]].max()
        y1_min = max(y1_min, 0)
        y1_range = y1_max - y1_min

        for i, (idx, row) in enumerate(action_df.iterrows()):
            fig.add_vline(x=row['datetime'], line_dash="dash",
                         line_color="gray", opacity=0.5, line_width=1)
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
                yref="y"
            )

    title = f"User Metrics - {user_address[:10]}..." if user_address else "User Metrics - All Users"
    fig.update_layout(
        title=dict(text=title, x=0.5, font=dict(size=16)),
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="plotly_white"
    )

    fig.update_xaxes(title_text="Time", tickformat="%Y-%m-%d %H:%M")
    
    # Apply y-axis ranges if provided
    if y_ranges:
        if fields[0] in y_ranges:
            fig.update_yaxes(range=y_ranges[fields[0]], secondary_y=False)
        else:
            fig.update_yaxes(title_text=fields[0], secondary_y=False)
    else:
        fig.update_yaxes(title_text=fields[0], secondary_y=False)
        
    if len(fields) > 1:
        if y_ranges and fields[1] in y_ranges:
            fig.update_yaxes(range=y_ranges[fields[1]], secondary_y=True)
        else:
            fig.update_yaxes(title_text=fields[1], secondary_y=True)

    fig.show()



import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

def plot_market_features(market_df, fields, dates_range=None, y_ranges=None):
    """
    Plot hourly market features over time.
    
    Parameters:
    market_df : DataFrame with columns 'datetime' (or 'timestamp') and the fields to plot.
    fields : list of 1 or 2 feature names.
    dates_range : optional tuple (start, end) as strings or datetimes.
    y_ranges : optional dict mapping field names to [lower, upper] for y‑axis limits.
    """
    df = market_df.copy()
    if 'datetime' not in df.columns:
        if 'timestamp' in df.columns:
            df['datetime'] = pd.to_datetime(df['timestamp'], unit='s')
        else:
            raise ValueError("DataFrame must have a 'datetime' or 'timestamp' column.")
    df = df.sort_values('datetime')
    
    if dates_range is not None:
        start, end = pd.to_datetime(dates_range[0]), pd.to_datetime(dates_range[1])
        df = df[(df['datetime'] >= start) & (df['datetime'] <= end)]
    
    fig = make_subplots(specs=[[{"secondary_y": len(fields) > 1}]])
    colors = px.colors.qualitative.Plotly
    
    # First field on left axis
    fig.add_trace(
        go.Scatter(x=df['datetime'], y=df[fields[0]],
                   mode='lines',
                   name=fields[0],
                   line=dict(color=colors[0], width=2)),
        secondary_y=False
    )
    
    # Second field on right axis (if provided)
    if len(fields) > 1:
        fig.add_trace(
            go.Scatter(x=df['datetime'], y=df[fields[1]],
                       mode='lines',
                       name=fields[1],
                       line=dict(color=colors[1], width=2, dash='dot')),
            secondary_y=True
        )
    
    # Layout styling (matching the user metrics function)
    fig.update_layout(
        title=f"Market Features: {', '.join(fields)}",
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="plotly_white"
    )
    
    fig.update_xaxes(title_text="Time", tickformat="%Y-%m-%d %H:%M")
    fig.update_yaxes(title_text=fields[0], secondary_y=False)
    if len(fields) > 1:
        fig.update_yaxes(title_text=fields[1], secondary_y=True)
    
    # Apply manual y‑axis limits if provided
    if y_ranges:
        if fields[0] in y_ranges:
            fig.update_yaxes(range=y_ranges[fields[0]], secondary_y=False)
        if len(fields) > 1 and fields[1] in y_ranges:
            fig.update_yaxes(range=y_ranges[fields[1]], secondary_y=True)
    
    fig.show()
