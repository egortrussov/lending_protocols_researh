# Market Spike Analysis Report

## Combined Analysis Across All Markets

### Action Impact (weighted by volume) – All Markets

| Action Type | Count | Weighted Mean ΔUtil |
|-------------|-------|---------------------|
| MarketBorrow | 211.0 | 0.0099 |
| MarketLiquidation | 9.0 | -0.0000 |
| MarketRepay | 291.0 | -0.0437 |
| MarketSupply | 2975.0 | -0.0682 |
| MarketWithdraw | 1031.0 | 0.0109 |

### Weighted Mean ΔUtil by Market and Action Type

| Market | N Spikes | MarketSupply | MarketRepay | MarketLiquidation | MarketBorrow | MarketWithdraw |
|---|---|---|---|---|---|---|
| base_cbbtc_usdc_full | 45 | **-0.0517** | -0.0001 | -0.0000 | 0.0002 | 0.0119 |
| eth_wsteth_usdc | 18 | **-0.1060** | -0.0347 |  | -0.0007 | 0.0144 |
| eth_wbtc_usdc | 65 | **-0.0656** | -0.0036 |  | 0.0073 | 0.0147 |
| base_wbtc_usdc | 68 | **-0.0761** | -0.0026 |  | 0.0036 | 0.0175 |
| eth_cbbtc_usdc | 27 | **-0.0561** | -0.0260 |  | 0.0162 | 0.0086 |
| eth_rlp_usdc | 141 | **-0.0411** | -0.0247 |  | 0.0000 | 0.0064 |
| base_wbtc_usdt | 26 | **-0.0660** | -0.0186 |  | 0.0006 | 0.0158 |
| eth_wbtc_usdt | 32 | **-0.0735** | -0.0195 |  | 0.0007 | 0.0188 |
| eth_mhyper_usdc | 4 | **-0.0355** | -0.0048 |  |  | 0.0053 |
| eth_wsteth_usdt | 12 | **-0.0720** |  |  | -0.0078 | 0.0312 |
| eth_usde_dai | 0 |  |  |  |  |  |
| eth_syrupusdc_usdc | 239 | **-0.1017** | -0.0485 |  | 0.0000 | 0.0177 |
| eth_weth_usdt | 11 | **-0.7283** | -0.0278 |  |  | 0.2077 |
| eth_wstusr_usdc | 127 | **-1.6309** |  |  |  | 0.9387 |
| eth_fxsave_usdc | 79 | **-0.1128** | -0.0606 |  | 0.0296 | 0.0201 |
| eth_reusd_usdc | 40 | -0.0605 | **-0.2505** |  |  | 0.0054 |
| eth_siusd_usdc | 21 | -0.0489 | **-0.0743** |  | 0.0003 | 0.0242 |
| eth_stcusd_usdc | 43 | **-0.0590** | -0.0353 |  |  | 0.0104 |
| eth_cbbtc_usdt | 13 | **-0.0984** |  |  |  |  |
| eth_wsrusd_usdc | 17 | **-0.0307** | -0.0180 |  | 0.0183 | 0.0227 |
| eth_sdeusd_usdc | 88 | -0.1050 | **-0.1532** | 0.0021 | 0.0005 | 0.0201 |
| eth_mapollo_usdc | 6 | **-0.1188** | -0.0560 |  | 0.0217 |  |
| eth_syrupusdc_pyusd | 4 | -0.0926 | **-0.0950** |  |  |  |
## Summary Across All Markets

| Metric | Value |
|--------|-------|
| Number of markets processed | 23 |
| Total spikes detected | 1126 |
| Total unique users across all markets | 30808 |
| Total events across all markets | 1959181 |

## Per-Market Analysis

## base_cbbtc_usdc_full

- **Max total supply (USD)**: 1,162,816,910.67
- **Total events**: 1,584,000
- **Number of users**: 24,782
- **Number of spikes**: 45

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 679.0 | -0.0517 |
| MarketRepay | 115.0 | -0.0001 |
| MarketLiquidation | 7.0 | -0.0000 |
| MarketBorrow | 132.0 | 0.0002 |
| MarketWithdraw | 169.0 | 0.0119 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 37 |
| MarketSupply | 5 |
| MarketRepay,MarketWithdrawCollateral | 1 |
| MarketBorrow,MarketSupplyCollateral | 1 |
| MarketSupplyCollateral | 1 |


---

## eth_wsteth_usdc

- **Max total supply (USD)**: 181,657,023.47
- **Total events**: 38,403
- **Number of users**: 889
- **Number of spikes**: 18

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 150.0 | -0.1060 |
| MarketRepay | 28.0 | -0.0347 |
| MarketBorrow | 19.0 | -0.0007 |
| MarketWithdraw | 97.0 | 0.0144 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 17 |
| MarketSupply | 1 |


---

## eth_wbtc_usdc

- **Max total supply (USD)**: 277,575,216.81
- **Total events**: 36,916
- **Number of users**: 881
- **Number of spikes**: 65

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 150.0 | -0.0656 |
| MarketRepay | 8.0 | -0.0036 |
| MarketBorrow | 21.0 | 0.0073 |
| MarketWithdraw | 25.0 | 0.0147 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 60 |
| MarketSupply,MarketWithdraw | 3 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## base_wbtc_usdc

- **Max total supply (USD)**: 269,255,896.54
- **Total events**: 26,928
- **Number of users**: 780
- **Number of spikes**: 68

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 141.0 | -0.0761 |
| MarketRepay | 4.0 | -0.0026 |
| MarketBorrow | 5.0 | 0.0036 |
| MarketWithdraw | 22.0 | 0.0175 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 63 |
| MarketSupply,MarketWithdraw | 4 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_cbbtc_usdc

- **Max total supply (USD)**: 607,128,500.34
- **Total events**: 48,487
- **Number of users**: 533
- **Number of spikes**: 27

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 326.0 | -0.0561 |
| MarketRepay | 17.0 | -0.0260 |
| MarketWithdraw | 83.0 | 0.0086 |
| MarketBorrow | 6.0 | 0.0162 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 17 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 7 |
| MarketSupply,MarketWithdraw | 1 |
| MarketBorrow,MarketSupply | 1 |
| MarketSupply | 1 |


---

## eth_rlp_usdc

- **Max total supply (USD)**: 154,288,632.54
- **Total events**: 47,031
- **Number of users**: 445
- **Number of spikes**: 141

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 466.0 | -0.0411 |
| MarketRepay | 42.0 | -0.0247 |
| MarketBorrow | 1.0 | 0.0000 |
| MarketWithdraw | 264.0 | 0.0064 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 132 |
| MarketSupply | 4 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketSupply,MarketWithdraw | 2 |
| MarketBorrow | 1 |


---

## base_wbtc_usdt

- **Max total supply (USD)**: 541,018,474.87
- **Total events**: 22,327
- **Number of users**: 409
- **Number of spikes**: 26

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 161.0 | -0.0660 |
| MarketRepay | 2.0 | -0.0186 |
| MarketBorrow | 9.0 | 0.0006 |
| MarketWithdraw | 59.0 | 0.0158 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 20 |
| MarketSupply,MarketWithdraw | 5 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_wbtc_usdt

- **Max total supply (USD)**: 529,825,941.69
- **Total events**: 22,235
- **Number of users**: 409
- **Number of spikes**: 32

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 175.0 | -0.0735 |
| MarketRepay | 3.0 | -0.0195 |
| MarketBorrow | 11.0 | 0.0007 |
| MarketWithdraw | 64.0 | 0.0188 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 27 |
| MarketSupply,MarketWithdraw | 4 |
| MarketSupply | 1 |


---

## eth_mhyper_usdc

- **Max total supply (USD)**: 142,136,439.88
- **Total events**: 8,698
- **Number of users**: 270
- **Number of spikes**: 4

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 18.0 | -0.0355 |
| MarketRepay | 12.0 | -0.0048 |
| MarketWithdraw | 61.0 | 0.0053 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 3 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_wsteth_usdt

- **Max total supply (USD)**: 339,293,759.74
- **Total events**: 10,993
- **Number of users**: 259
- **Number of spikes**: 12

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 33.0 | -0.0720 |
| MarketBorrow | 1.0 | -0.0078 |
| MarketWithdraw | 25.0 | 0.0312 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 9 |
| MarketSupply | 2 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_usde_dai

- **Max total supply (USD)**: 154,685,204.51
- **Total events**: 4,091
- **Number of users**: 256
- **Number of spikes**: 0

*No spikes detected or insufficient data for action analysis.*

---

## eth_syrupusdc_usdc

- **Max total supply (USD)**: 93,767,984.11
- **Total events**: 27,592
- **Number of users**: 200
- **Number of spikes**: 239

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 332.0 | -0.1017 |
| MarketRepay | 3.0 | -0.0485 |
| MarketBorrow | 2.0 | 0.0000 |
| MarketWithdraw | 64.0 | 0.0177 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 226 |
| MarketSupply,MarketWithdraw | 5 |
| MarketBorrow,MarketSupplyCollateral | 4 |
| MarketSupply | 2 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_weth_usdt

- **Max total supply (USD)**: 614,128.00
- **Total events**: 1,760
- **Number of users**: 99
- **Number of spikes**: 11

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 27.0 | -0.7283 |
| MarketRepay | 4.0 | -0.0278 |
| MarketWithdraw | 5.0 | 0.2077 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 11 |


---

## eth_wstusr_usdc

- **Max total supply (USD)**: 43,945,273.28
- **Total events**: 11,842
- **Number of users**: 92
- **Number of spikes**: 127

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 171.0 | -1.6309 |
| MarketWithdraw | 18.0 | 0.9387 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 112 |
| MarketSupply,MarketWithdraw | 12 |
| MarketSupply | 2 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_fxsave_usdc

- **Max total supply (USD)**: 39,034,562.39
- **Total events**: 9,130
- **Number of users**: 87
- **Number of spikes**: 79

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 119.0 | -0.1128 |
| MarketRepay | 1.0 | -0.0606 |
| MarketWithdraw | 30.0 | 0.0201 |
| MarketBorrow | 1.0 | 0.0296 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 72 |
| MarketBorrow,MarketSupplyCollateral | 4 |
| MarketSupply,MarketWithdraw | 2 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_reusd_usdc

- **Max total supply (USD)**: 13,221,619.01
- **Total events**: 6,101
- **Number of users**: 87
- **Number of spikes**: 40

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 1.0 | -0.2505 |
| MarketSupply | 42.0 | -0.0605 |
| MarketWithdraw | 19.0 | 0.0054 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 39 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_siusd_usdc

- **Max total supply (USD)**: 95,936,123.41
- **Total events**: 17,138
- **Number of users**: 80
- **Number of spikes**: 21

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 12.0 | -0.0743 |
| MarketSupply | 91.0 | -0.0489 |
| MarketBorrow | 1.0 | 0.0003 |
| MarketWithdraw | 67.0 | 0.0242 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 20 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_stcusd_usdc

- **Max total supply (USD)**: 71,069,966.39
- **Total events**: 11,778
- **Number of users**: 66
- **Number of spikes**: 43

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 91.0 | -0.0590 |
| MarketRepay | 3.0 | -0.0353 |
| MarketWithdraw | 27.0 | 0.0104 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 28 |
| MarketSupply,MarketWithdraw | 7 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 6 |
| MarketBorrow,MarketSupplyCollateral | 2 |


---

## eth_cbbtc_usdt

- **Max total supply (USD)**: 239,531,763.80
- **Total events**: 972
- **Number of users**: 45
- **Number of spikes**: 13

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 15.0 | -0.0984 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 11 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |
| MarketSupply,MarketWithdraw | 1 |


---

## eth_wsrusd_usdc

- **Max total supply (USD)**: 100,015,819.43
- **Total events**: 7,348
- **Number of users**: 44
- **Number of spikes**: 17

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 18.0 | -0.0307 |
| MarketRepay | 34.0 | -0.0180 |
| MarketBorrow | 18.0 | 0.0183 |
| MarketWithdraw | 8.0 | 0.0227 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 12 |
| MarketBorrow,MarketSupplyCollateral | 4 |
| MarketSupply | 1 |


---

## eth_sdeusd_usdc

- **Max total supply (USD)**: 82,421,369.96
- **Total events**: 14,602
- **Number of users**: 43
- **Number of spikes**: 88

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 9.0 | -0.1532 |
| MarketSupply | 126.0 | -0.1050 |
| MarketBorrow | 3.0 | 0.0005 |
| MarketLiquidation | 2.0 | 0.0021 |
| MarketWithdraw | 52.0 | 0.0201 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 84 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 4 |


---

## eth_mapollo_usdc

- **Max total supply (USD)**: 5,370,054.71
- **Total events**: 470
- **Number of users**: 27
- **Number of spikes**: 6

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 5.0 | -0.1188 |
| MarketRepay | 1.0 | -0.0560 |
| MarketBorrow | 1.0 | 0.0217 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 4 |
| MarketBorrow,MarketSupplyCollateral | 2 |


---

## eth_syrupusdc_pyusd

- **Max total supply (USD)**: 30,014,924.86
- **Total events**: 339
- **Number of users**: 25
- **Number of spikes**: 4

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 1.0 | -0.0950 |
| MarketSupply | 2.0 | -0.0926 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 2 |
| MarketBorrow,MarketSupplyCollateral | 1 |
| MarketBorrow | 1 |


---

