import pandas as pd
import numpy as np


def detect_market_spikes(
    df,
    start_date=None,
    baseline_window_hours=24,
    baseline_gap_seconds=300,
    spike_util_threshold=0.90,
    min_spike_delta=0.03,
    recovery_buffer=0.02,
    max_followup_events=200,
    actions_limit=1000,
    min_episode_events=1,           # NEW: filter short episodes
    sustained_recovery_events=1,     # NEW: require N consecutive events below threshold
    min_actions_in_spike=1,
):
    """
    Detect utilization spike episodes in Morpho market event logs.
    (Full docstring omitted for brevity – same as before plus new parameters)

    New Parameters
    --------------
    min_episode_events : int
        Minimum number of events an episode must contain to be included.
    sustained_recovery_events : int
        Number of consecutive events where utilization must stay ≤ baseline+buffer
        before recovery is confirmed (prevents false recovery from a single small action).
    """
    # Ensure datetime column exists
    if 'datetime' not in df.columns and 'timestamp' in df.columns:
        df['datetime'] = pd.to_datetime(df['timestamp'], unit='s')
    
    if start_date is not None:
        start_ts = pd.Timestamp(start_date).timestamp()
        df = df[df['timestamp'] >= start_ts].copy()
        if df.empty:
            return []
    
    df = df.sort_values('timestamp').reset_index(drop=True)
    df['delta_util'] = df['utilization_after'] - df['utilization_before']
    
    # Precompute baseline utilization
    timestamps = df['timestamp'].values
    util_after = df['utilization_after'].values
    baseline_util = np.full(len(df), np.nan)
    baseline_sec = baseline_window_hours * 3600
    
    for i in range(len(df)):
        t_i = timestamps[i]
        window_start = t_i - baseline_sec
        window_end = t_i - baseline_gap_seconds
        mask = (timestamps >= window_start) & (timestamps <= window_end)
        if mask.any():
            baseline_util[i] = np.median(util_after[mask])
        else:
            earlier = df['utilization_after'][timestamps < t_i]
            if not earlier.empty:
                baseline_util[i] = earlier.iloc[-1]
            else:
                baseline_util[i] = util_after[i]
    df['baseline_utilization'] = baseline_util
    
    spikes = []
    i = 0
    n = len(df)
    in_episode = False
    episode_start_idx = None
    episode_baseline = None
    episode_peak_util = None
    
    while i < n and len(spikes) < actions_limit:
        row = df.iloc[i]
        
        is_spike_onset = (
            row['utilization_after'] >= spike_util_threshold and
            row['delta_util'] >= min_spike_delta and
            not in_episode
        )
        
        if is_spike_onset:
            episode_start_idx = i
            episode_baseline = row['baseline_utilization']
            episode_peak_util = row['utilization_after']
            in_episode = True
            
            onset_tx_hash = row['hash']
            onset_timestamp = row['timestamp']
            tx_rows = df[(df['timestamp'] == onset_timestamp) & (df['hash'] == onset_tx_hash)]
            trigger_event_types = ','.join(sorted(tx_rows['type'].unique()))
            
            market_state = {
                'total_borrow': row.get('total_borrow_before', np.nan),
                'total_supply': row.get('total_supply_before', np.nan),
                'collateral_price': row.get('collateral_price', np.nan),
                'loan_asset_price': row.get('loan_asset_price', np.nan),
                'debt_before': row.get('debt_before', np.nan),
                'supply_before': row.get('supply_before', np.nan),
                'utilization_before': row.get('utilization_before', np.nan)
            }
            
            recovery_idx = None
            censoring_reason = None
            end_idx = None
            sustained_count = 0  # NEW: counter for sustained recovery
            
            for j in range(i, min(i + max_followup_events, n)):
                current_row = df.iloc[j]
                
                if current_row['utilization_after'] > episode_peak_util:
                    episode_peak_util = current_row['utilization_after']
                
                # Check recovery condition (with sustained requirement)
                if current_row['utilization_after'] <= episode_baseline + recovery_buffer:
                    sustained_count += 1
                else:
                    sustained_count = 0
                
                if sustained_count >= sustained_recovery_events:
                    recovery_idx = j
                    end_idx = j
                    censoring_reason = None
                    break
                
                # Check for new spike onset (only after the first event)
                if j > i:
                    new_onset = (
                        current_row['utilization_after'] >= spike_util_threshold and
                        current_row['delta_util'] >= min_spike_delta
                    )
                    if new_onset:
                        end_idx = j - 1
                        censoring_reason = 'new_spike_onset'
                        break
            
            if recovery_idx is None and censoring_reason is None:
                end_idx = min(i + max_followup_events - 1, n - 1)
                censoring_reason = 'max_events_reached'
            
            episode_df = df.iloc[i:end_idx+1].copy()
            
            # Apply minimum episode length filter
            if len(episode_df) < min_episode_events:
                i = end_idx + 1
                in_episode = False
                continue
            
            if recovery_idx is not None:
                recovery_datetime = df.iloc[recovery_idx]['datetime']
                recovery_time_seconds = df.iloc[recovery_idx]['timestamp'] - row['timestamp']
                event = 1
            else:
                recovery_datetime = None
                recovery_time_seconds = None
                event = 0
            
            spike_info = {
                'trigger_datetime': row['datetime'],
                'recovery_datetime': recovery_datetime,
                'recovery_time_seconds': recovery_time_seconds,
                'event': event,
                'spike_magnitudes': {
                    'utilization_delta': row['delta_util'],
                    'peak_utilization': episode_peak_util
                },
                'trigger_event_types': trigger_event_types,
                'market_state': market_state,
                'actions_df': episode_df,
                'baseline_utilization': episode_baseline,
                'spike_duration_events': len(episode_df)
            }
            if censoring_reason:
                spike_info['censoring_reason'] = censoring_reason
            
            spikes.append(spike_info)
            
            i = end_idx + 1
            in_episode = False
        else:
            i += 1
    spikes_cleaned = []
    for s in spikes:
        if s["actions_df"].shape[0] >= min_actions_in_spike:
            spikes_cleaned.append(s)
    
    return spikes_cleaned
