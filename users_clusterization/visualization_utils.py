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






import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
import statsmodels.api as sm

def plot_user_metrics_with_predictions(hourly_df, model_df, user_address, model, scaler, feature_names,
                                        fields, dates_range=None, prob_threshold=0.5):
    """
    Plot time series metrics for a user with model prediction probabilities overlaid.
    
    Parameters:
    hourly_df : DataFrame with raw metrics (must contain 'user_address', 'timestamp', 'datetime', 'action', and the fields to plot)
    model_df : DataFrame with feature columns (same user_address and timestamp as hourly_df)
    user_address : str
    model : statsmodels result object (fitted Logit)
    scaler : StandardScaler fitted on training data
    feature_names : list of feature column names in the order used during training (without 'const')
    fields : list of field names from hourly_df to plot (first on left axis, second on right axis if two provided)
    dates_range : optional tuple (start, end) of datetime-like to restrict plot
    prob_threshold : float, threshold for horizontal line on probability axis
    """
    # Extract user data
    plot_df = hourly_df[hourly_df['user_address'] == user_address].copy()
    if plot_df.empty:
        print(f"No data for user {user_address}")
        return

    # Extract user features from model_df
    user_features = model_df[model_df['user_address'] == user_address].copy()
    if user_features.empty:
        print(f"No feature data for user {user_address}")
        return

    # Merge to align timestamps (keep all rows from plot_df)
    merged = plot_df.merge(user_features[['timestamp'] + feature_names], on='timestamp', how='left')
    # Check for missing features
    missing = merged[feature_names].isna().any(axis=1).sum()
    if missing > 0:
        print(f"Warning: {missing} rows have missing features. Predictions will be NaN for those rows.")
        # Fill missing with median (fallback)
        for col in feature_names:
            merged[col].fillna(merged[col].median(), inplace=True)

    # Prepare feature matrix for prediction
    X = merged[feature_names].copy()
    X = X.replace([np.inf, -np.inf], np.nan)
    for col in feature_names:
        if X[col].isna().any():
            X[col].fillna(X[col].median(), inplace=True)
    X_scaled = scaler.transform(X)
    X_sm = sm.add_constant(X_scaled)
    probs = model.predict(X_sm)
    merged['prediction_prob'] = probs

    # Restrict dates if requested
    if dates_range is not None:
        merged = merged[(merged['datetime'] >= dates_range[0]) & (merged['datetime'] <= dates_range[1])]

    # Ensure datetime column exists and sort
    if 'datetime' not in merged.columns:
        merged['datetime'] = pd.to_datetime(merged['timestamp'], unit='s')
    merged = merged.sort_values('timestamp')

    # Create figure with secondary y‑axis for probability
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    colors = px.colors.qualitative.Plotly

    # Plot first field (left axis)
    merged[fields[0]] = merged[fields[0]].clip(0, merged[fields[0]].max())
    fig.add_trace(
        go.Scatter(x=merged['datetime'], y=merged[fields[0]],
                   mode='lines+markers',
                   name=fields[0],
                   line=dict(color=colors[0], width=2),
                   marker=dict(size=4)),
        secondary_y=False
    )

    # Plot second field if given (right axis)
    if len(fields) > 1:
        fig.add_trace(
            go.Scatter(x=merged['datetime'], y=merged[fields[1]],
                       mode='lines+markers',
                       name=fields[1],
                       line=dict(color=colors[1], width=2),
                       marker=dict(size=4)),
            secondary_y=True
        )

    # Add prediction probability trace (right axis)
    fig.add_trace(
        go.Scatter(x=merged['datetime'], y=merged['prediction_prob'],
                   mode='lines',
                   name='Prediction Probability',
                   line=dict(color='red', width=2, dash='dot')),
        secondary_y=True
    )

    # Add horizontal line at threshold
    fig.add_hline(y=prob_threshold, line_dash="dash", line_color="gray", opacity=0.5,
                  secondary_y=True, annotation_text=f"Threshold ({prob_threshold})")

    # Add action markers (vertical lines and annotations)
    action_df = merged[merged['action'] != 'none'].copy()
    if not action_df.empty:
        y1_min, y1_max = merged[fields[0]].min(), merged[fields[0]].max()
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

    # Update layout
    title = f"User Metrics with Predictions - {user_address[:10]}..."
    fig.update_layout(
        title=dict(text=title, x=0.5, font=dict(size=16)),
        hovermode='x unified',
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        template="plotly_white"
    )

    fig.update_xaxes(title_text="Time", tickformat="%Y-%m-%d %H:%M")
    fig.update_yaxes(title_text=fields[0], secondary_y=False)
    if len(fields) > 1:
        fig.update_yaxes(title_text=fields[1], secondary_y=True, range=[0, merged[fields[1]].max()])
    else:
        fig.update_yaxes(title_text="Probability", secondary_y=True, range=[0, 1])

    fig.show()