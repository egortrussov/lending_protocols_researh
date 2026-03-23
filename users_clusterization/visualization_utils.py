import matplotlib.pyplot as plt
import pandas as pd

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
def plot_user_metrics(df, fields, user_address=None, dates_range=None):
    """
    Plot time series metrics with action markers using Plotly.
    """
    if user_address:
        plot_df = df[df['user_address'] == user_address].copy()
        print("User address", {user_address})
        print("MAX DEBT", {plot_df["debt"].max()})
        
        
        if plot_df.empty:
            print(f"No data for user {user_address}")
            return
    else:
        plot_df = df.copy()
    plot_df["ltv"] = plot_df["ltv"].clip(0,1)

    if dates_range is not None:
        plot_df = plot_df[(plot_df["datetime"] >= dates_range[0]) & (plot_df["datetime"] <= dates_range[1])]
    
    plot_df = plot_df.sort_values('timestamp')
    plot_df['datetime'] = pd.to_datetime(plot_df['timestamp'], unit='s')
    
    # Create subplot with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": len(fields) > 1}]])
    
    colors = px.colors.qualitative.Plotly

    plot_df[fields[0]] = plot_df[fields[0]].clip(0, plot_df[fields[0]].max())
    
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
