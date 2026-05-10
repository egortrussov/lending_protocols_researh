The YB clustering result is **good and interpretable**, capturing meaningful behavioral differences primarily driven by debt size, market dominance, sequential vs. concurrent opening, and spike exposure. The large cluster of ultra‑passive long‑term holders is realistic for yield‑bearing assets.

---

### Cluster Interpretation

| Cluster | Size | Label | Key Defining Features (z > 2) |
|---------|------|-------|--------------------------------|
| **0** | 69 (3.4%) | **Whale hyper‑active managers** | `large_max_debt` = 1.0 (+5.1), `mean_actions_per_pos` = 7.7 (+2.9), `mean_repays_per_pos` = 4.4 (+2.8), `mean_borrows_per_pos` = 3.3 (+2.4), `mean_max_share` = 0.072 (+2.5), `max_debt` = $4.0M (+3.4), `debtors_rank_ever` = 0.68 (+2.1) |
| **1** | 108 (5.3%) | **Sequential modest borrowers** | `overlap_ratio` = 0.47 (-4.0), `n_positions` = 4.4 (+3.8), otherwise low activity, no large debt, no dominance |
| **2** | 119 (5.8%) | **Dominant borrowers** | `debtors_rank_ever` = 1.0 (+3.2), `mean_max_share` = 0.049 (+1.6), high spike count (228), moderate actions, medium debt (max ~$233k) |
| **3** | 261 (12.8%) | **Spike‑exposed passive holders** | High `total_spikes` = 318 (+1.5), `mean_effective_close_ltv` = 0.82 (+0.4), very long duration (~2824h), low actions, never dominant |
| **4** | 1,339 (65.9%) | **Ultra‑passive long‑term holders** | Extremely long duration (~7857h, +0.45), minimal actions (0.5/pos), very low debt ($2.6k median), no spikes, no dominance. The default YB strategy. |
---
