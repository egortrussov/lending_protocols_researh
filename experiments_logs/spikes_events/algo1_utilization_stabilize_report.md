# Market Spike Analysis Report

## Combined Analysis Across All Markets

### Action Impact (weighted by volume) – All Markets

| Action Type | Count | Weighted Mean ΔUtil |
|-------------|-------|---------------------|
| MarketBorrow | 2282.0 | 0.0089 |
| MarketLiquidation | 5.0 | -0.0467 |
| MarketRepay | 2391.0 | -0.0728 |
| MarketSupply | 21845.0 | -0.0616 |
| MarketWithdraw | 11455.0 | 0.0128 |

### Weighted Mean ΔUtil by Market and Action Type

| Market | N Spikes | MarketSupply | MarketLiquidation | MarketRepay | MarketBorrow | MarketWithdraw| Address |
|---|---|---|---|---|---|---|---|
| eth_usr_usdc | 763 | **-0.0692** | -0.0125 | -0.0124 | 0.0012 | 0.0213 | 0x8e7cc042d739a365c43d0a52d5f24160fa7ae9b7e7c9a479bd02a56041d4cf77 |
| eth_wsteth_usdc | 0 |  |  |  |  |  | 0xb323495f7e4148be5643a4ea4a8221eef163e4bccfdedc2a6f4696baacbc86cc |
| eth_wbtc_usdc | 14 | **-0.0550** |  | -0.0036 | 0.0032 | 0.0057 | 0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49 |
| base_wbtc_usdc | 243 | **-0.0530** |  | -0.0132 | 0.0008 | 0.0127 | 0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49 |
| eth_cbbtc_usdc | 40 | **-0.0490** |  | -0.0285 | 0.0130 | 0.0077 | 0x64d65c9a2d91c36d56fbc42d69e979335320169b3df63bf92789e2c8883fcc64 |
| eth_rlp_usdc | 466 | -0.0440 | -0.0035 | **-0.0489** | 0.0106 | 0.0089 | 0xe1b65304edd8ceaea9b629df4c3c926a37d1216e27900505c04f14b2ed279f33 |
| base_wbtc_usdt | 138 | **-0.0609** |  | -0.0162 | 0.0028 | 0.0110 | 0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99 |
| eth_wbtc_usdt | 154 | **-0.0655** |  | -0.0190 | 0.0033 | 0.0123 | 0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99 |
| eth_PT-reUSD-25JUN2026_usdc | 8 | **-0.0394** |  | -0.0029 | 0.0004 | 0.0105 | 0x9bc98c2f20ac58287ef2c860eea53a2fdc27c17a7817ff1206c0b7840cc7cd79 |
| eth_mhyper_usdc | 117 | **-0.0614** |  | -0.0164 | 0.0152 | 0.0139 | 0x95c28d447950ca6c8bbfd25fc05b80b1fd7a1cdd17a3610b4b3f1ffc8dc2e2ed |
| eth_wsteth_usdt | 116 | **-0.0668** |  | -0.0536 | -0.0154 | 0.0112 | 0xe7e9694b754c4d4f7e21faf7223f6fa71abaeb10296a4c43a54a7977149687d2 |
| eth_usde_dai | 8 | -0.0039 | **-0.0469** | -0.0257 | 0.0146 | 0.0088 | 0xc581c5f70bd1afa283eed57d1418c6432cbff1d862f94eaf58fdd4e46afbb67f |
| eth_PT-USDe-25SEP2025_usdc | 29 | -0.0291 |  | **-0.0527** | 0.0044 | 0.0121 | 0x7a5d67805cb78fad2596899e0c83719ba89df353b931582eb7d3041fd5a06dc8 |
| PT-reUSD-25JUN2026_usdc | 15 | **-0.0476** |  | -0.0350 | 0.0006 | 0.0115 | 0x9bc98c2f20ac58287ef2c860eea53a2fdc27c17a7817ff1206c0b7840cc7cd79 |
| eth_syrupusdc_usdc | 553 | -0.0705 |  | **-0.1501** | -0.0054 | 0.0131 | 0x729badf297ee9f2f6b3f717b96fd355fc6ec00422284ce1968e76647b258cf44 |
| eth_PT-stcUSD-29JAN2026_usdc | 176 | -0.0597 |  | **-0.0648** | 0.0160 | 0.0141 | 0x03f715ef1ae508ab3e1faf4dffdbf2a077d1f0ad10c5aad42cf4438d5e3328af |
| eth_PT-USDe-27MAR2025_dai | 14 | **-0.0729** |  | -0.0450 | 0.0111 | 0.0478 | 0xab0dcab71e65c05b7f241ea79a33452c87e62db387129e4abe15e458d433e4d8 |
| eth_PT-USDe-25SEP2025_dai | 0 |  |  |  |  |  | 0x45d97c66db5e803b9446802702f087d4293a2f74b370105dc3a88a278bf6bb21 |
| eth_PT-USDe-25SEP2025_usdt | 31 | **-0.0839** |  | -0.0213 | 0.0085 | 0.0268 | 0xb0a9ac81a8c6a5274aa1a8337aed35a2cb2cd4feb5c6d3b39d41f234fbf2955b |
| eth_PT-csUSDL-31JUL2025_usdc | 112 | **-0.1046** |  | -0.0391 | 0.0055 | 0.0126 | 0x544b0a093b130a3fb01b72a1279ab848575f049c73da3b5c9c718f9350a1519c |
| eth_slvlusd_usdc | 146 | **-0.0570** |  | -0.0227 | 0.0008 | 0.0154 | 0x8b1bc4d682b04a16309a8adf77b35de0c42063a7944016cfc37a79ccac0007b6 |
| eth_PT-sNUSD-5MAR2026_usdc | 27 | **-0.0427** |  | -0.0146 | 0.0025 | 0.0173 | 0x2a9a5c436719badcfadbad3ad8e8179a160ded758603eaa03a883f922a1790d3 |
| eth_PT-mHYPER-20NOV2025_usdc | 63 | -0.0518 |  | **-0.2485** | 0.0207 | 0.0142 | 0x1ca75949a91c157183f53282d73c37191e7cd84002310f6632047d874aad4a0f |
| eth_PT-USDe-31JUL2025_dai | 48 | **-0.2626** |  | -0.1314 | 0.0202 | 0.0222 | 0x760b14c9003f08ac4bf0cfb02596ee4d6f0548a4fde5826bfd56befb9ed62ae9 |
| eth_weth_usdt | 66 | **-1.1764** |  | -0.1427 | -0.0082 | 0.0138 | 0xdbffac82c2dc7e8aa781bd05746530b0068d80929f23ac1628580e27810bc0c5 |
| eth_wstusr_usdc | 644 | -0.0760 |  | **-0.4435** | -0.0016 | 0.0161 | 0xd9e34b1eed46d123ac1b69b224de1881dbc88798bc7b70f504920f62f58f28cc |
| eth_fxsave_usdc | 285 | -0.0822 |  | **-0.2272** | 0.0223 | 0.0119 | 0x43e925e52d7873fa8acac90dd5f246087d55b3a34c344b71884a6352491ff459 |
| eth_reusd_usdc | 159 | -0.1022 |  | **-0.2461** | 0.0035 | 0.0144 | 0x4565ac05d38b19374ccbb04c17cca60ca9353cd41824f0803d0fc7704f60eaed |
| eth_siusd_usdc | 90 | **-0.0419** |  | -0.0140 | 0.0115 | 0.0119 | 0xbbf7ce1b40d32d3e3048f5cf27eeaa6de8cb27b80194690aab191a63381d8c99 |
| eth_PT-wstUSR-25SEP2025_usdc | 88 | **-0.0906** |  | -0.0121 | -0.0020 | 0.0138 | 0xeec6c7e2ddb7578f2a7d86fc11cf9da005df34452ad9b9189c51266216f5d71b |
| eth_stcusd_usdc | 224 | -0.0537 |  | -0.0006 | **0.0758** | 0.0160 | 0xeb17955ea422baeddbfb0b8d8c9086c5be7a9cfdefb292119a102e981a30062e |
| eth_PT-RLP-4SEP2025_usdc | 100 | **-0.1311** |  | -0.0652 | 0.0150 | 0.0161 | 0xcc611d3ca8ce8dcc63e4e8c3cd17c9acb2ca1768eeb143b71e2dc8e6a98c3f65 |
| eth_PT-USD0++-27MAR2025_usdc | 58 | -0.1116 |  | **-0.2103** | -0.0564 | 0.0203 | 0x147977320f168afc651b7e5a1849cc1b1e64e329e1bf0212fa49dcb2856074a4 |
| eth_PT-slvlUSD-29MAY2025_usdc | 82 | -0.0574 |  | -0.0541 | **-0.0838** | 0.0123 | 0xeb3e4a68c675d88f5a4378eab966e717bdee6a0f38c5ca6da2560ac5d1534f60 |
| eth_cbbtc_usdt | 22 | **-0.1831** |  | -0.0304 | 0.0210 | 0.0217 | 0x45671fb8d5dea1c4fbca0b8548ad742f6643300eeb8dbd34ad64a658b2b05bca |
| eth_wsrusd_usdc | 30 | **-0.0335** |  | -0.0162 | 0.0087 | 0.0122 | 0x1590cb22d797e226df92ebc6e0153427e207299916e7e4e53461389ad68272fb |
| eth_sdeusd_usdc | 311 | **-0.0704** | 0.0021 | -0.0466 | 0.0005 | 0.0155 | 0x0f9563442d64ab3bd3bcb27058db0b0d4046a4c46f0acd811dacae9551d2b129 |
| eth_PT-syrupUSDC-28AUG2025_usdc | 62 | -0.0796 |  | **-0.5712** |  | 0.0176 | 0x3bdb58058b41bb700458ba3df317e254244ddec7fc35fec93d2d53475cc6ebdc |
| eth_PT-USDe-27NOV2025_usds | 29 | -0.1157 |  | **-0.6831** | 0.0219 | 0.0817 | 0x8cdb63a27a48ac27fadc0f158a732104bcc4e10bb61c9a5095ea7c127204e26c |
| eth_PT-syrupUSDC-30OCT2025_usdc | 119 | **-0.0715** |  | -0.0001 | 0.0045 | 0.0156 | 0xb8afc953c3cc8077b4a4bf459bede8d3f80be45ca1f244e4bca13b7b1030eed5 |
| eth_mapollo_usdc | 11 | -0.0903 |  | **-0.1572** | 0.0147 | 0.0225 | 0x031c7333014af51e4fd18031d14e4eaada58348cde3f6dc6ea8cca16f7387fb2 |
| eth_syrupusdc_pyusd | 5 | -0.0648 |  | **-0.0699** | 0.0054 | 0.0111 | 0xc9629945524f3fde56c7e8854a6c3d48e76b9d97236abbe73c750fcc7aeb8501 |
| PT-siUSD-26MAR2026_usdc | 116 | **-0.0694** |  | -0.0003 | 0.0019 | 0.0164 | 0xaac3ffcdf8a75919657e789fa72ab742a7bbfdf5bb0b87e4bbeb3c29bbbbb05c |
| eth_PT-stcUSD-23JUL2026_usdc | 254 | **-0.0572** |  | -0.0550 |  | 0.0146 | 0x2fb3713487c7812e7309935b034f40228841666f6b048faf31fd2110ae674f20 |
## Summary Across All Markets

| Metric | Value |
|--------|-------|
| Number of markets processed | 44 |
| Total spikes detected | 6036 |
| Total unique users across all markets | 9460 |
| Total events across all markets | 499412 |

## Per-Market Analysis

## eth_usr_usdc

- **Max total supply (USD)**: 133,737,726.89
- **Total events**: 23,055
- **Number of users**: 1,225
- **Number of spikes**: 763

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 1922.0 | -0.0692 |
| MarketLiquidation | 1.0 | -0.0125 |
| MarketRepay | 181.0 | -0.0124 |
| MarketBorrow | 108.0 | 0.0012 |
| MarketWithdraw | 651.0 | 0.0213 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 746 |
| MarketSupply,MarketWithdraw | 13 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 4 |


---

## eth_wsteth_usdc

- **Max total supply (USD)**: 181,657,023.47
- **Total events**: 38,401
- **Number of users**: 889
- **Number of spikes**: 0

*No spikes detected or insufficient data for action analysis.*

---

## eth_wbtc_usdc

- **Max total supply (USD)**: 277,575,216.81
- **Total events**: 36,914
- **Number of users**: 880
- **Number of spikes**: 14

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 66.0 | -0.0550 |
| MarketRepay | 7.0 | -0.0036 |
| MarketBorrow | 8.0 | 0.0032 |
| MarketWithdraw | 23.0 | 0.0057 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 13 |
| MarketSupply,MarketWithdraw | 1 |


---

## base_wbtc_usdc

- **Max total supply (USD)**: 269,255,896.54
- **Total events**: 26,926
- **Number of users**: 780
- **Number of spikes**: 243

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 1086.0 | -0.0530 |
| MarketRepay | 175.0 | -0.0132 |
| MarketBorrow | 404.0 | 0.0008 |
| MarketWithdraw | 681.0 | 0.0127 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 206 |
| MarketSupply,MarketWithdraw | 32 |
| MarketBorrow,MarketSupplyCollateral | 3 |
| MarketBorrow | 1 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_cbbtc_usdc

- **Max total supply (USD)**: 607,128,500.34
- **Total events**: 48,485
- **Number of users**: 533
- **Number of spikes**: 40

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 861.0 | -0.0490 |
| MarketRepay | 64.0 | -0.0285 |
| MarketWithdraw | 529.0 | 0.0077 |
| MarketBorrow | 105.0 | 0.0130 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 28 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 8 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketSupply,MarketWithdraw | 1 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_rlp_usdc

- **Max total supply (USD)**: 154,288,632.54
- **Total events**: 47,028
- **Number of users**: 445
- **Number of spikes**: 466

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 174.0 | -0.0489 |
| MarketSupply | 2384.0 | -0.0440 |
| MarketLiquidation | 1.0 | -0.0035 |
| MarketWithdraw | 1712.0 | 0.0089 |
| MarketBorrow | 104.0 | 0.0106 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 443 |
| MarketSupply,MarketWithdraw | 8 |
| MarketBorrow,MarketSupplyCollateral | 6 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 5 |
| MarketBorrow | 2 |


---

## base_wbtc_usdt

- **Max total supply (USD)**: 541,018,474.87
- **Total events**: 22,324
- **Number of users**: 409
- **Number of spikes**: 138

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 1913.0 | -0.0609 |
| MarketRepay | 194.0 | -0.0162 |
| MarketBorrow | 278.0 | 0.0028 |
| MarketWithdraw | 952.0 | 0.0110 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 92 |
| MarketSupply,MarketWithdraw | 41 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_wbtc_usdt

- **Max total supply (USD)**: 529,825,941.69
- **Total events**: 22,233
- **Number of users**: 409
- **Number of spikes**: 154

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 2042.0 | -0.0655 |
| MarketRepay | 199.0 | -0.0190 |
| MarketBorrow | 301.0 | 0.0033 |
| MarketWithdraw | 1027.0 | 0.0123 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 101 |
| MarketSupply,MarketWithdraw | 48 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_mhyper_usdc

- **Max total supply (USD)**: 142,136,439.88
- **Total events**: 8,665
- **Number of users**: 270
- **Number of spikes**: 117

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 410.0 | -0.0614 |
| MarketRepay | 127.0 | -0.0164 |
| MarketWithdraw | 380.0 | 0.0139 |
| MarketBorrow | 34.0 | 0.0152 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 91 |
| MarketBorrow | 18 |
| MarketBorrow,MarketSupplyCollateral | 7 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_wsteth_usdt

- **Max total supply (USD)**: 339,293,759.74
- **Total events**: 10,720
- **Number of users**: 256
- **Number of spikes**: 116

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 772.0 | -0.0668 |
| MarketRepay | 60.0 | -0.0536 |
| MarketBorrow | 90.0 | -0.0154 |
| MarketWithdraw | 447.0 | 0.0112 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 90 |
| MarketSupply,MarketWithdraw | 13 |
| MarketBorrow,MarketSupplyCollateral | 5 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 4 |
| MarketBorrow | 3 |


---

## eth_usde_dai

- **Max total supply (USD)**: 154,685,204.51
- **Total events**: 3,578
- **Number of users**: 253
- **Number of spikes**: 8

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketLiquidation | 1.0 | -0.0469 |
| MarketRepay | 154.0 | -0.0257 |
| MarketSupply | 1.0 | -0.0039 |
| MarketWithdraw | 5.0 | 0.0088 |
| MarketBorrow | 37.0 | 0.0146 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 4 |
| MarketBorrow,MarketSupplyCollateral | 3 |
| MarketBorrow | 1 |


---

## eth_syrupusdc_usdc

- **Max total supply (USD)**: 93,767,984.11
- **Total events**: 27,590
- **Number of users**: 200
- **Number of spikes**: 553

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 15.0 | -0.1501 |
| MarketSupply | 1376.0 | -0.0705 |
| MarketBorrow | 12.0 | -0.0054 |
| MarketWithdraw | 629.0 | 0.0131 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 517 |
| MarketSupply,MarketWithdraw | 23 |
| MarketBorrow,MarketSupplyCollateral | 7 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 4 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_slvlusd_usdc

- **Max total supply (USD)**: 67,373,880.68
- **Total events**: 9,574
- **Number of users**: 114
- **Number of spikes**: 146

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 338.0 | -0.0570 |
| MarketRepay | 16.0 | -0.0227 |
| MarketBorrow | 1.0 | 0.0008 |
| MarketWithdraw | 171.0 | 0.0154 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 127 |
| MarketSupply,MarketWithdraw | 10 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketBorrow | 2 |


---

## eth_weth_usdt

- **Max total supply (USD)**: 614,128.00
- **Total events**: 1,758
- **Number of users**: 99
- **Number of spikes**: 66

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 136.0 | -1.1764 |
| MarketRepay | 152.0 | -0.1427 |
| MarketBorrow | 210.0 | -0.0082 |
| MarketWithdraw | 33.0 | 0.0138 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 54 |
| MarketBorrow,MarketSupplyCollateral | 7 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |
| MarketBorrow,MarketRepay,MarketSupplyCollateral | 1 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_wstusr_usdc

- **Max total supply (USD)**: 43,945,273.28
- **Total events**: 11,159
- **Number of users**: 92
- **Number of spikes**: 644

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 6.0 | -0.4435 |
| MarketSupply | 974.0 | -0.0760 |
| MarketBorrow | 11.0 | -0.0016 |
| MarketWithdraw | 179.0 | 0.0161 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 576 |
| MarketSupply,MarketWithdraw | 46 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 15 |
| MarketBorrow,MarketSupplyCollateral | 4 |
| MarketBorrow,MarketSupply | 3 |


---

## eth_fxsave_usdc

- **Max total supply (USD)**: 39,034,562.39
- **Total events**: 9,128
- **Number of users**: 87
- **Number of spikes**: 285

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 15.0 | -0.2272 |
| MarketSupply | 713.0 | -0.0822 |
| MarketWithdraw | 331.0 | 0.0119 |
| MarketBorrow | 10.0 | 0.0223 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 261 |
| MarketBorrow,MarketSupplyCollateral | 8 |
| MarketSupply,MarketWithdraw | 7 |
| MarketBorrow | 5 |
| MarketBorrow,MarketSupply | 3 |


---

## eth_reusd_usdc

- **Max total supply (USD)**: 13,221,619.01
- **Total events**: 6,099
- **Number of users**: 87
- **Number of spikes**: 159

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 2.0 | -0.2461 |
| MarketSupply | 488.0 | -0.1022 |
| MarketBorrow | 10.0 | 0.0035 |
| MarketWithdraw | 325.0 | 0.0144 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 158 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_siusd_usdc

- **Max total supply (USD)**: 95,936,123.41
- **Total events**: 17,135
- **Number of users**: 80
- **Number of spikes**: 90

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 530.0 | -0.0419 |
| MarketRepay | 46.0 | -0.0140 |
| MarketBorrow | 54.0 | 0.0115 |
| MarketWithdraw | 411.0 | 0.0119 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 71 |
| MarketSupply,MarketWithdraw | 14 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |
| MarketBorrow,MarketSupplyCollateral | 2 |


---

## eth_stcusd_usdc

- **Max total supply (USD)**: 71,069,966.39
- **Total events**: 11,776
- **Number of users**: 66
- **Number of spikes**: 224

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 988.0 | -0.0537 |
| MarketRepay | 17.0 | -0.0006 |
| MarketWithdraw | 615.0 | 0.0160 |
| MarketBorrow | 7.0 | 0.0758 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 182 |
| MarketSupply,MarketWithdraw | 33 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 7 |
| MarketBorrow,MarketSupplyCollateral | 2 |


---

## eth_cbbtc_usdt

- **Max total supply (USD)**: 239,531,763.80
- **Total events**: 970
- **Number of users**: 45
- **Number of spikes**: 22

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 45.0 | -0.1831 |
| MarketRepay | 7.0 | -0.0304 |
| MarketBorrow | 5.0 | 0.0210 |
| MarketWithdraw | 12.0 | 0.0217 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 18 |
| MarketSupply,MarketWithdraw | 2 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_wsrusd_usdc

- **Max total supply (USD)**: 100,015,387.35
- **Total events**: 7,345
- **Number of users**: 44
- **Number of spikes**: 30

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 162.0 | -0.0335 |
| MarketRepay | 127.0 | -0.0162 |
| MarketBorrow | 76.0 | 0.0087 |
| MarketWithdraw | 58.0 | 0.0122 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 25 |
| MarketBorrow,MarketSupplyCollateral | 5 |


---

## eth_sdeusd_usdc

- **Max total supply (USD)**: 82,421,369.96
- **Total events**: 14,600
- **Number of users**: 43
- **Number of spikes**: 311

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 630.0 | -0.0704 |
| MarketRepay | 11.0 | -0.0466 |
| MarketBorrow | 4.0 | 0.0005 |
| MarketLiquidation | 2.0 | 0.0021 |
| MarketWithdraw | 236.0 | 0.0155 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 304 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 5 |
| MarketSupply,MarketWithdraw | 1 |
| MarketBorrow | 1 |


---

## eth_mapollo_usdc

- **Max total supply (USD)**: 5,370,054.71
- **Total events**: 468
- **Number of users**: 27
- **Number of spikes**: 11

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 20.0 | -0.1572 |
| MarketSupply | 29.0 | -0.0903 |
| MarketBorrow | 13.0 | 0.0147 |
| MarketWithdraw | 19.0 | 0.0225 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 7 |
| MarketBorrow | 2 |
| MarketBorrow,MarketSupplyCollateral | 2 |


---

## eth_syrupusdc_pyusd

- **Max total supply (USD)**: 30,014,681.10
- **Total events**: 336
- **Number of users**: 25
- **Number of spikes**: 5

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 3.0 | -0.0699 |
| MarketSupply | 4.0 | -0.0648 |
| MarketBorrow | 3.0 | 0.0054 |
| MarketWithdraw | 1.0 | 0.0111 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 3 |
| MarketWithdraw | 2 |


---

## eth_PT-reUSD-25JUN2026_usdc

- **Max total supply (USD)**: 53,867,791.40
- **Total events**: 15,181
- **Number of users**: 300
- **Number of spikes**: 8

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 143.0 | -0.0394 |
| MarketRepay | 29.0 | -0.0029 |
| MarketBorrow | 135.0 | 0.0004 |
| MarketWithdraw | 64.0 | 0.0105 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 8 |


---

## eth_PT-USDe-25SEP2025_usdc

- **Max total supply (USD)**: 418,822,963.58
- **Total events**: 14,256
- **Number of users**: 252
- **Number of spikes**: 29

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 42.0 | -0.0527 |
| MarketSupply | 264.0 | -0.0291 |
| MarketBorrow | 6.0 | 0.0044 |
| MarketWithdraw | 139.0 | 0.0121 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 27 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |


---

## PT-reUSD-25JUN2026_usdc

- **Max total supply (USD)**: 54,243,591.24
- **Total events**: 10,595
- **Number of users**: 202
- **Number of spikes**: 15

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 180.0 | -0.0476 |
| MarketRepay | 18.0 | -0.0350 |
| MarketBorrow | 67.0 | 0.0006 |
| MarketWithdraw | 72.0 | 0.0115 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 13 |
| MarketBorrow | 1 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_PT-stcUSD-29JAN2026_usdc

- **Max total supply (USD)**: 60,017,452.09
- **Total events**: 8,831
- **Number of users**: 141
- **Number of spikes**: 176

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 105.0 | -0.0648 |
| MarketSupply | 674.0 | -0.0597 |
| MarketWithdraw | 468.0 | 0.0141 |
| MarketBorrow | 15.0 | 0.0160 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 161 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 7 |
| MarketSupply,MarketWithdraw | 7 |
| MarketBorrow | 1 |


---

## eth_PT-USDe-27MAR2025_dai

- **Max total supply (USD)**: 126,211,463.34
- **Total events**: 2,339
- **Number of users**: 135
- **Number of spikes**: 14

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 90.0 | -0.0729 |
| MarketRepay | 101.0 | -0.0450 |
| MarketBorrow | 65.0 | 0.0111 |
| MarketWithdraw | 43.0 | 0.0478 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 10 |
| MarketBorrow,MarketSupplyCollateral | 3 |
| MarketBorrow | 1 |


---

## eth_PT-USDe-25SEP2025_dai

- **Max total supply (USD)**: 504,042,081.14
- **Total events**: 3,267
- **Number of users**: 133
- **Number of spikes**: 0

*No spikes detected or insufficient data for action analysis.*

---

## eth_PT-USDe-25SEP2025_usdt

- **Max total supply (USD)**: 58,360,881.73
- **Total events**: 3,954
- **Number of users**: 123
- **Number of spikes**: 31

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 160.0 | -0.0839 |
| MarketRepay | 68.0 | -0.0213 |
| MarketBorrow | 10.0 | 0.0085 |
| MarketWithdraw | 76.0 | 0.0268 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 28 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |


---

## eth_PT-csUSDL-31JUL2025_usdc

- **Max total supply (USD)**: 31,582,576.18
- **Total events**: 5,483
- **Number of users**: 115
- **Number of spikes**: 112

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 211.0 | -0.1046 |
| MarketRepay | 14.0 | -0.0391 |
| MarketBorrow | 4.0 | 0.0055 |
| MarketWithdraw | 98.0 | 0.0126 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 71 |
| MarketSupply,MarketWithdraw | 37 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |
| MarketBorrow | 1 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_PT-sNUSD-5MAR2026_usdc

- **Max total supply (USD)**: 11,460,920.52
- **Total events**: 2,811
- **Number of users**: 111
- **Number of spikes**: 27

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 145.0 | -0.0427 |
| MarketRepay | 25.0 | -0.0146 |
| MarketBorrow | 25.0 | 0.0025 |
| MarketWithdraw | 68.0 | 0.0173 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 24 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_PT-mHYPER-20NOV2025_usdc

- **Max total supply (USD)**: 38,891,074.29
- **Total events**: 2,701
- **Number of users**: 106
- **Number of spikes**: 63

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 60.0 | -0.2485 |
| MarketSupply | 155.0 | -0.0518 |
| MarketWithdraw | 169.0 | 0.0142 |
| MarketBorrow | 8.0 | 0.0207 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 35 |
| MarketBorrow,MarketSupplyCollateral | 13 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 8 |
| MarketBorrow | 7 |


---

## eth_PT-USDe-31JUL2025_dai

- **Max total supply (USD)**: 10,439,187.23
- **Total events**: 1,835
- **Number of users**: 104
- **Number of spikes**: 48

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 64.0 | -0.2626 |
| MarketRepay | 60.0 | -0.1314 |
| MarketBorrow | 10.0 | 0.0202 |
| MarketWithdraw | 35.0 | 0.0222 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 31 |
| MarketBorrow | 9 |
| MarketBorrow,MarketSupplyCollateral | 8 |


---

## eth_PT-wstUSR-25SEP2025_usdc

- **Max total supply (USD)**: 17,812,907.25
- **Total events**: 3,406
- **Number of users**: 67
- **Number of spikes**: 88

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 102.0 | -0.0906 |
| MarketRepay | 3.0 | -0.0121 |
| MarketBorrow | 2.0 | -0.0020 |
| MarketWithdraw | 13.0 | 0.0138 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 83 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |
| MarketBorrow,MarketSupplyCollateral | 1 |
| MarketBorrow | 1 |


---

## eth_PT-RLP-4SEP2025_usdc

- **Max total supply (USD)**: 16,632,337.06
- **Total events**: 3,235
- **Number of users**: 66
- **Number of spikes**: 100

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 212.0 | -0.1311 |
| MarketRepay | 23.0 | -0.0652 |
| MarketBorrow | 7.0 | 0.0150 |
| MarketWithdraw | 101.0 | 0.0161 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 94 |
| MarketBorrow,MarketSupplyCollateral | 3 |
| MarketRepay,MarketWithdraw,MarketWithdrawCollateral | 2 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_PT-USD0++-27MAR2025_usdc

- **Max total supply (USD)**: 29,862,840.94
- **Total events**: 2,052
- **Number of users**: 66
- **Number of spikes**: 58

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 23.0 | -0.2103 |
| MarketSupply | 258.0 | -0.1116 |
| MarketBorrow | 4.0 | -0.0564 |
| MarketWithdraw | 202.0 | 0.0203 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 54 |
| MarketBorrow,MarketSupply | 3 |
| MarketBorrow | 1 |


---

## eth_PT-slvlUSD-29MAY2025_usdc

- **Max total supply (USD)**: 21,369,077.19
- **Total events**: 2,235
- **Number of users**: 52
- **Number of spikes**: 82

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketBorrow | 2.0 | -0.0838 |
| MarketSupply | 237.0 | -0.0574 |
| MarketRepay | 16.0 | -0.0541 |
| MarketWithdraw | 151.0 | 0.0123 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 69 |
| MarketBorrow,MarketSupplyCollateral | 12 |
| MarketBorrow | 1 |


---

## eth_PT-syrupUSDC-28AUG2025_usdc

- **Max total supply (USD)**: 11,775,168.69
- **Total events**: 1,407
- **Number of users**: 39
- **Number of spikes**: 62

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 3.0 | -0.5712 |
| MarketSupply | 149.0 | -0.0796 |
| MarketWithdraw | 70.0 | 0.0176 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 62 |


---

## eth_PT-USDe-27NOV2025_usds

- **Max total supply (USD)**: 265,788,041.17
- **Total events**: 931
- **Number of users**: 35
- **Number of spikes**: 29

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 25.0 | -0.6831 |
| MarketSupply | 28.0 | -0.1157 |
| MarketBorrow | 28.0 | 0.0219 |
| MarketWithdraw | 9.0 | 0.0817 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 21 |
| MarketBorrow | 4 |
| MarketWithdraw | 4 |


---

## eth_PT-syrupUSDC-30OCT2025_usdc

- **Max total supply (USD)**: 38,130,515.89
- **Total events**: 3,819
- **Number of users**: 27
- **Number of spikes**: 119

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 253.0 | -0.0715 |
| MarketRepay | 1.0 | -0.0001 |
| MarketBorrow | 1.0 | 0.0045 |
| MarketWithdraw | 94.0 | 0.0156 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 108 |
| MarketSupply,MarketWithdraw | 6 |
| MarketBorrow,MarketSupply | 3 |
| MarketBorrow | 1 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## PT-siUSD-26MAR2026_usdc

- **Max total supply (USD)**: 2,258,353.08
- **Total events**: 1,718
- **Number of users**: 16
- **Number of spikes**: 116

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 192.0 | -0.0694 |
| MarketRepay | 2.0 | -0.0003 |
| MarketBorrow | 8.0 | 0.0019 |
| MarketWithdraw | 74.0 | 0.0164 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 111 |
| MarketSupply,MarketWithdraw | 4 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_PT-stcUSD-23JUL2026_usdc

- **Max total supply (USD)**: 3,114,579.50
- **Total events**: 3,089
- **Number of users**: 12
- **Number of spikes**: 254

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 458.0 | -0.0572 |
| MarketRepay | 1.0 | -0.0550 |
| MarketWithdraw | 82.0 | 0.0146 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 249 |
| MarketSupply,MarketWithdraw | 5 |


---

