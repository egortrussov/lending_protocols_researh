
### Cluster Interpretation

| Cluster | Size | Label | Defining Characteristics (z > 2) |
|---------|------|-------|-----------------------------------|
| **0** | 188 | **Multi‑asset/multi‑market active traders** | `n_loan_asset_types` (+12.4), `n_markets` (+11.6), `n_collateral_types` (+8.8), `max_concurrent_positions` (+3.4), `was_active_during_spike` (+3.7) – operate across many markets and asset types simultaneously, frequently active during spikes. |
| **1** | 191 | **Ultra‑short‑term high‑concurrency flippers** | `max_concurrent_positions` (+11.7), `n_positions` (+9.0), `avg_leverage_factor` (+4.4), `overlap_ratio` (–2.0) – open/close dozens of positions very quickly (average duration ~0.4 h), highly leveraged, within a single market. |
| **2** | 177 | **Dominant whale borrowers** | `debtors_rank_ever` (+12.8), `mean_max_share` (+8.7), `was_active_during_spike` (+4.2), `total_spikes` (+3.8), high debt ($222k median) – consistently top borrowers, heavily involved in spikes, control a large share of debt in their markets. |
| **3** | 544 | **High‑LTV spike responders** | `prop_high_ltv_open` (+3.9), `was_active_during_spike` (+4.2), `total_spikes` (+2.6), `median_max_ltv` (+1.6) – open most positions at high LTV (>0.8) and react to nearly every spike. |
| **4** | 1,133 | **Set‑and‑forget long‑term high‑LTV borrowers** | `prop_high_ltv_open` (+3.9), `mean_duration_hours` (+2.6), `mean_avg_borrow_rate` (+2.7), tiny debt (~$14) – open high‑LTV positions and hold them for extremely long periods (median ~8,500 h) without closing. |
| **5** | 681 | **Spike‑sensitive moderate borrowers** | `was_active_during_spike` (+4.2), `total_spikes` (+1.8) – always present during spikes, moderate LTV (~0.68), most positions closed. |
| **6** | 4,086 | **Sequential single‑market borrowers** | `overlap_ratio` (–2.3), moderate positions (~5.7) – open positions one after another (low concurrency), not spike‑active, conservative LTV. |
| **7** | 6,448 | **One‑shot conservative repayers** | `prop_closed` (+1.3), low LTV (~0.55), exactly 2 positions, never see spikes – open two positions, close both, minimal activity. |
| **8** | 15,818 | **Passive long‑term retail holders** | `prop_closed` (–0.8), moderate LTV (~0.61), ~2 positions, never spike‑exposed – the default “buy‑and‑hold” borrower. |

---


---


| Cluster | Dominant Market(s) | Interpretation |
|---------|--------------------|----------------|
| **−1 (Noise)** | Crypto 58%, YB 28%, PT 14% | HDBSCAN noise mirrors the overall market distribution — no bias. Healthy. |
| **0** | Crypto 83%, YB 13% | **Multi‑asset traders** mainly on Crypto, some YB diversification. |
| **1** | PT 55%, YB 37%, Crypto 8% | **Ultra‑short flippers** concentrate on PT & YB, avoiding Crypto. PT's expiry structure may encourage rapid position cycling. |
| **2** | Crypto **100%** | **Whale borrowers** exist *only* on Crypto markets. Dominant borrowers do not appear on PT/YB — suggests different market structures. |
| **3** | PT 53%, YB 46%, Crypto 1% | **High‑LTV spike responders** split almost evenly between PT & YB, absent from Crypto. Spikes on PT/YB have different mechanics. |
| **4** | YB **95%**, Crypto 4%, PT 1% | **Set‑and‑forget long‑term** is overwhelmingly a YB phenomenon. Fixed‑yield assets may encourage passive holding. |
| **5** | Crypto 51%, YB 34%, PT 15% | **Spike‑sensitive moderates** are the most evenly distributed across markets. |
| **6** | Crypto **99%**, YB 0.3%, PT 0.02% | **Sequential borrowers** are almost exclusively Crypto. |
| **7** | Crypto **98%**, YB 1.4%, PT 0.06% | **One‑shot repayers** are almost exclusively Crypto. |
| **8** | Crypto 97%, YB 2.9%, PT 0.2% | **Passive retail holders** are overwhelmingly Crypto. |

---




## Cluster Summaries

---

### Cluster 0 — Multi-Asset, Multi-Market Active Traders
**n = 188**

**Identifying features:**
- `n_loan_asset_types` = 2.0 (z = +12.4)
- `n_markets` = 2.8 (z = +11.6)
- `n_collateral_types` = 1.5 (z = +8.8)
- `max_concurrent_positions` = 4.7 (z = +3.4)
- `was_active_during_spike_any` = 89% (z = +3.7)
- `total_spikes` = 90.7 (z = +2.1)

**Dominant markets:** Crypto (83%), YB (13%), PT (4%)

---

### Cluster 1 — Ultra-Short-Term High-Concurrency Flippers
**n = 191**

**Identifying features:**
- `max_concurrent_positions` = 11.0 (z = +11.7)
- `n_positions` = 54.0 (z = +9.0)
- `avg_leverage_factor` = 1.74 (z = +4.4)
- `overlap_ratio` = 0.48 (z = –2.0)
- Mean duration = 0.39 hours

**Dominant markets:** PT (55%), YB (37%), Crypto (8%)

---

### Cluster 2 — Dominant Whale Borrowers
**n = 177**

**Identifying features:**
- `debtors_rank_ever` = 1.0 (z = +12.8)
- `mean_max_share` = 0.038 (z = +8.7)
- `was_active_during_spike_any` = 1.0 (z = +4.2)
- `total_spikes` = 164.0 (z = +3.8)
- `prop_high_ltv_open` = 62% (z = +2.3)
- `median_max_debt` = $222k (z = +1.9)
- `median_open_debt` = $148k (z = +2.1)

**Dominant markets:** Crypto (100%)

---

### Cluster 3 — High-LTV Spike Responders
**n = 544**

**Identifying features:**
- `was_active_during_spike_any` = 1.0 (z = +4.2)
- `prop_high_ltv_open` = 1.0 (z = +3.9)
- `total_spikes` = 114.0 (z = +2.6)
- `median_max_ltv` = 0.86 (z = +1.6)
- `mean_effective_close_ltv` = 0.84 (z = +1.5)

**Dominant markets:** PT (53%), YB (46%), Crypto (1%)

---

### Cluster 4 — Set-and-Forget Long-Term High-LTV Holders
**n = 1,133**

**Identifying features:**
- `prop_high_ltv_open` = 1.0 (z = +3.9)
- `mean_avg_borrow_rate` = 0.098 (z = +2.7)
- `mean_duration_hours` = 8,516 (z = +2.6)
- `prop_closed` = 1.6% (z = –0.8)
- Median debt = ~$14 (very small)

**Dominant markets:** YB (95%), Crypto (4%), PT (1%)

---

### Cluster 5 — Spike-Sensitive Moderate Borrowers
**n = 681**

**Identifying features:**
- `was_active_during_spike_any` = 1.0 (z = +4.2)
- `total_spikes` = 79.3 (z = +1.8)
- `prop_closed` = 79% (z = +0.9)
- Moderate LTV (~0.68), moderate duration (~2,600h)

**Dominant markets:** Crypto (51%), YB (34%), PT (15%)

---

### Cluster 6 — Sequential Single-Market Borrowers
**n = 4,086**

**Identifying features:**
- `overlap_ratio` = 0.41 (z = –2.3)
- `prop_closed` = 74% (z = +0.8)
- `n_positions` = 5.7 (z = +0.5)
- Conservative LTV (~0.57), no spike activity

**Dominant markets:** Crypto (99%), YB (0.3%), PT (0.02%)

---

### Cluster 7 — One-Shot Conservative Repayers
**n = 6,448**

**Identifying features:**
- `prop_closed` = 1.0 (z = +1.3)
- `n_positions` = 2.0 (z = –0.2)
- Low LTV (~0.55), no spike activity, ~888 hours duration

**Dominant markets:** Crypto (98%), YB (1.4%), PT (0.06%)

---

### Cluster 8 — Passive Long-Term Retail Holders
**n = 15,818**

**Identifying features:**
- `prop_closed` = 0.0 (z = –0.8)
- `n_positions` = 2.0 (z = –0.2)
- Moderate LTV (~0.61), no spike activity, ~2,869 hours duration

**Dominant markets:** Crypto (97%), YB (2.9%), PT (0.2%)

---

### Cluster –1 — Noise (Idiosyncratic Users)
**n = Not clustered**

**Characteristics:** Users with no consistent behavioral pattern. Evenly distributed across markets (Crypto 58%, YB 28%, PT 14%) — mirrors the overall dataset distribution. Excluded from structured analysis, noted as a methodological transparency feature of HDBSCAN.