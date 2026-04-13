# Market Spike Analysis Report

## Combined Analysis Across All Markets

### Action Impact (weighted by volume) – All Markets

| Action Type | Count | Weighted Mean ΔUtil |
|-------------|-------|---------------------|
| MarketBorrow | 332.0 | 0.0211 |
| MarketLiquidation | 2.0 | -0.0121 |
| MarketRepay | 563.0 | -0.0485 |
| MarketSupply | 6619.0 | -0.0653 |
| MarketWithdraw | 3860.0 | 0.0338 |

### Weighted Mean ΔUtil by Market and Action Type

| Market | N Spikes | MarketSupply | MarketBorrow | MarketRepay | MarketWithdraw | MarketLiquidation| Address |
|---|---|---|---|---|---|---|---|
| base_cbbtc_usdc_full | 6 | **-0.0280** | 0.0000 | -0.0000 | 0.0252 |  | 0x9103c3b4e834476c9a62ea009ba2c884ee42e94e6e314a26f04d312434191836 |
| eth_wbtc_usdc | 65 | **-0.0929** |  | -0.0023 | 0.0077 |  | 0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49 |
| base_wbtc_usdc | 60 | **-0.0627** | 0.0329 | -0.0249 | 0.0444 |  | 0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49 |
| eth_usr_usdc | 235 | **-0.0926** | 0.0265 | -0.0284 | 0.0316 | -0.0125 | 0x8e7cc042d739a365c43d0a52d5f24160fa7ae9b7e7c9a479bd02a56041d4cf77 |
| eth_cbbtc_usdc | 19 | **-0.0513** | 0.0159 | -0.0128 | 0.0074 | -0.0000 | 0x64d65c9a2d91c36d56fbc42d69e979335320169b3df63bf92789e2c8883fcc64 |
| base_wbtc_usdt | 14 | -0.0783 | 0.0008 | -0.0015 | **0.0787** |  | 0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99 |
| eth_wbtc_usdt | 15 | **-0.0880** | 0.0016 | -0.0018 | 0.0857 |  | 0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99 |
| eth_rlp_usdc | 88 | **-0.0422** | -0.0087 | -0.0225 | 0.0107 |  | 0xe1b65304edd8ceaea9b629df4c3c926a37d1216e27900505c04f14b2ed279f33 |
| eth_PT-reUSD-25JUN2026_usdc | 6 | -0.0136 | 0.0004 | -0.0025 | **0.0147** |  | 0x9bc98c2f20ac58287ef2c860eea53a2fdc27c17a7817ff1206c0b7840cc7cd79 |
| eth_mhyper_usdc | 1 | **-0.0308** |  | -0.0008 | 0.0152 |  | 0x95c28d447950ca6c8bbfd25fc05b80b1fd7a1cdd17a3610b4b3f1ffc8dc2e2ed |
| eth_usde_dai | 1 |  | 0.0002 | **-0.0675** |  |  | 0xc581c5f70bd1afa283eed57d1418c6432cbff1d862f94eaf58fdd4e46afbb67f |
| eth_wsteth_usdt | 24 | -0.0640 | **-0.1079** | -0.0681 | 0.0167 |  | 0xe7e9694b754c4d4f7e21faf7223f6fa71abaeb10296a4c43a54a7977149687d2 |
| eth_PT-USDe-25SEP2025_usdc | 13 | -0.0310 |  | **-0.0454** | 0.0396 |  | 0x7a5d67805cb78fad2596899e0c83719ba89df353b931582eb7d3041fd5a06dc8 |
| eth_syrupusdc_usdc | 176 | -0.0683 | -0.0000 | **-0.0823** | 0.0318 |  | 0x729badf297ee9f2f6b3f717b96fd355fc6ec00422284ce1968e76647b258cf44 |
| PT-reUSD-25JUN2026_usdc | 0 |  |  |  |  |  | 0x9bc98c2f20ac58287ef2c860eea53a2fdc27c17a7817ff1206c0b7840cc7cd79 |
| eth_PT-USDe-27MAR2025_dai | 7 | **-0.1095** | 0.0107 | -0.0608 | 0.0071 |  | 0xab0dcab71e65c05b7f241ea79a33452c87e62db387129e4abe15e458d433e4d8 |
| eth_PT-USDe-25SEP2025_dai | 0 |  |  |  |  |  | 0x45d97c66db5e803b9446802702f087d4293a2f74b370105dc3a88a278bf6bb21 |
| eth_PT-USDe-25SEP2025_usdt | 11 | **-0.0983** | 0.0000 | -0.0216 | 0.0502 |  | 0xb0a9ac81a8c6a5274aa1a8337aed35a2cb2cd4feb5c6d3b39d41f234fbf2955b |
| eth_PT-csUSDL-31JUL2025_usdc | 23 | **-0.1038** | 0.0624 | -0.0003 | 0.0212 |  | 0x544b0a093b130a3fb01b72a1279ab848575f049c73da3b5c9c718f9350a1519c |
| eth_PT-sNUSD-5MAR2026_usdc | 11 | **-0.0547** | -0.0015 | -0.0201 | 0.0545 |  | 0x2a9a5c436719badcfadbad3ad8e8179a160ded758603eaa03a883f922a1790d3 |
| eth_csusdl_usdc | 37 | **-0.0994** | 0.0378 | -0.0135 | 0.0359 |  | 0x83b7ad16905809ea36482f4fbf6cfee9c9f316d128de9a5da1952607d5e4df5e |
| eth_slvlusd_usdc | 32 | **-0.0761** | 0.0008 | -0.0068 | 0.0199 |  | 0x8b1bc4d682b04a16309a8adf77b35de0c42063a7944016cfc37a79ccac0007b6 |
| eth_PT-mHYPER-20NOV2025_usdc | 4 | -0.0356 |  | **-0.2069** | 0.0108 |  | 0x1ca75949a91c157183f53282d73c37191e7cd84002310f6632047d874aad4a0f |
| eth_PT-stcUSD-29JAN2026_usdc | 14 | **-0.0528** | -0.0010 | -0.0248 | 0.0179 |  | 0x03f715ef1ae508ab3e1faf4dffdbf2a077d1f0ad10c5aad42cf4438d5e3328af |
| eth_weth_usdt | 4 | -0.6621 | 0.0122 | -0.0247 | **0.6760** |  | 0xdbffac82c2dc7e8aa781bd05746530b0068d80929f23ac1628580e27810bc0c5 |
| eth_PT-USDe-31JUL2025_dai | 14 | **-0.4832** | 0.0003 | -0.0325 | 0.0468 |  | 0x760b14c9003f08ac4bf0cfb02596ee4d6f0548a4fde5826bfd56befb9ed62ae9 |
| eth_reusd_usdc | 29 | **-0.0748** |  |  | 0.0293 |  | 0x4565ac05d38b19374ccbb04c17cca60ca9353cd41824f0803d0fc7704f60eaed |
| eth_fxsave_usdc | 61 | **-0.0904** | 0.0434 | -0.0655 | 0.0267 |  | 0x43e925e52d7873fa8acac90dd5f246087d55b3a34c344b71884a6352491ff459 |
| eth_wstusr_usdc | 14 | -1.4083 |  |  | **1.9235** |  | 0xd9e34b1eed46d123ac1b69b224de1881dbc88798bc7b70f504920f62f58f28cc |
| eth_siusd_usdc | 20 | -0.0362 | -0.0011 | **-0.0558** | 0.0169 |  | 0xbbf7ce1b40d32d3e3048f5cf27eeaa6de8cb27b80194690aab191a63381d8c99 |
| eth_PT-RLP-4SEP2025_usdc | 24 | **-0.0625** |  | -0.0001 | 0.0310 |  | 0xcc611d3ca8ce8dcc63e4e8c3cd17c9acb2ca1768eeb143b71e2dc8e6a98c3f65 |
| eth_PT-wstUSR-25SEP2025_usdc | 37 | **-0.0966** |  | -0.0005 | 0.0117 |  | 0xeec6c7e2ddb7578f2a7d86fc11cf9da005df34452ad9b9189c51266216f5d71b |
| eth_PT-USD0++-27MAR2025_usdc | 12 | **-0.1684** |  | -0.1461 | 0.0475 |  | 0x147977320f168afc651b7e5a1849cc1b1e64e329e1bf0212fa49dcb2856074a4 |
| eth_stcusd_usdc | 29 | **-0.0385** |  | -0.0269 | 0.0142 |  | 0xeb17955ea422baeddbfb0b8d8c9086c5be7a9cfdefb292119a102e981a30062e |
| eth_PT-slvlUSD-29MAY2025_usdc | 20 | **-0.0667** | -0.0481 |  | 0.0602 |  | 0xeb3e4a68c675d88f5a4378eab966e717bdee6a0f38c5ca6da2560ac5d1534f60 |
| eth_cbbtc_usdt | 10 | **-0.0851** | 0.0003 |  | 0.0284 |  | 0x45671fb8d5dea1c4fbca0b8548ad742f6643300eeb8dbd34ad64a658b2b05bca |
| eth_wsrusd_usdc | 9 | **-0.0324** | 0.0036 | -0.0163 | 0.0313 |  | 0x1590cb22d797e226df92ebc6e0153427e207299916e7e4e53461389ad68272fb |
| eth_sdeusd_usdc | 50 | **-0.0958** | 0.0743 | -0.0543 | 0.0550 |  | 0x0f9563442d64ab3bd3bcb27058db0b0d4046a4c46f0acd811dacae9551d2b129 |
| eth_PT-syrupUSDC-28AUG2025_usdc | 22 | -0.0974 |  | **-0.4521** | 0.0223 |  | 0x3bdb58058b41bb700458ba3df317e254244ddec7fc35fec93d2d53475cc6ebdc |
| eth_PT-USDe-27NOV2025_usds | 10 | **-0.0706** |  |  |  |  | 0x8cdb63a27a48ac27fadc0f158a732104bcc4e10bb61c9a5095ea7c127204e26c |
| eth_PT-syrupUSDC-30OCT2025_usdc | 20 | **-0.0643** | 0.0607 |  | 0.0428 |  | 0xb8afc953c3cc8077b4a4bf459bede8d3f80be45ca1f244e4bca13b7b1030eed5 |
| eth_mapollo_usdc | 4 | **-0.1244** | 0.0217 |  |  |  | 0x031c7333014af51e4fd18031d14e4eaada58348cde3f6dc6ea8cca16f7387fb2 |
| eth_syrupusdc_pyusd | 3 | **-0.0897** | 0.0854 | -0.0861 |  |  | 0xc9629945524f3fde56c7e8854a6c3d48e76b9d97236abbe73c750fcc7aeb8501 |
| PT-siUSD-26MAR2026_usdc | 26 | -0.0723 |  |  | **0.0742** |  | 0xaac3ffcdf8a75919657e789fa72ab742a7bbfdf5bb0b87e4bbeb3c29bbbbb05c |
| eth_PT-stcUSD-23JUL2026_usdc | 41 | -0.0536 |  | **-0.0550** | 0.0392 |  | 0x2fb3713487c7812e7309935b034f40228841666f6b048faf31fd2110ae674f20 |
## Summary Across All Markets

| Metric | Value |
|--------|-------|
| Number of markets processed | 45 |
| Total spikes detected | 1321 |
| Total unique users across all markets | 30741 |
| Total events across all markets | 1795072 |

## Per-Market Analysis

## base_cbbtc_usdc_full

- **Max total supply (USD)**: 1,162,816,910.67
- **Total events**: 1,383,485
- **Number of users**: 23,218
- **Number of spikes**: 6

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 293.0 | -0.0280 |
| MarketBorrow | 29.0 | 0.0000 |
| MarketRepay | 16.0 | -0.0000 |
| MarketWithdraw | 96.0 | 0.0252 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 4 |
| MarketSupply | 1 |
| MarketSupplyCollateral | 1 |


---

## eth_wbtc_usdc

- **Max total supply (USD)**: 277,575,216.81
- **Total events**: 32,265
- **Number of users**: 841
- **Number of spikes**: 65

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 19.0 | -0.0929 |
| MarketRepay | 1.0 | -0.0023 |
| MarketWithdraw | 3.0 | 0.0077 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 37 |
| MarketSupply | 11 |
| MarketSupply,MarketWithdraw | 8 |
| MarketRepay,MarketWithdrawCollateral | 4 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |


---

## base_wbtc_usdc

- **Max total supply (USD)**: 269,255,896.54
- **Total events**: 23,527
- **Number of users**: 739
- **Number of spikes**: 60

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 451.0 | -0.0627 |
| MarketRepay | 40.0 | -0.0249 |
| MarketBorrow | 84.0 | 0.0329 |
| MarketWithdraw | 318.0 | 0.0444 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 57 |
| MarketSupply,MarketWithdraw | 3 |


---

## eth_usr_usdc

- **Max total supply (USD)**: 133,737,726.89
- **Total events**: 20,849
- **Number of users**: 570
- **Number of spikes**: 235

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 568.0 | -0.0926 |
| MarketRepay | 24.0 | -0.0284 |
| MarketLiquidation | 1.0 | -0.0125 |
| MarketBorrow | 8.0 | 0.0265 |
| MarketWithdraw | 198.0 | 0.0316 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 230 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |
| MarketSupply | 2 |
| MarketSupply,MarketWithdraw | 1 |


---

## eth_cbbtc_usdc

- **Max total supply (USD)**: 607,128,500.34
- **Total events**: 42,227
- **Number of users**: 495
- **Number of spikes**: 19

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 295.0 | -0.0513 |
| MarketRepay | 24.0 | -0.0128 |
| MarketLiquidation | 1.0 | -0.0000 |
| MarketWithdraw | 148.0 | 0.0074 |
| MarketBorrow | 11.0 | 0.0159 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 14 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |
| MarketSupply,MarketWithdraw | 1 |
| MarketBorrow,MarketSupply | 1 |


---

## base_wbtc_usdt

- **Max total supply (USD)**: 541,018,474.87
- **Total events**: 19,435
- **Number of users**: 384
- **Number of spikes**: 14

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 336.0 | -0.0783 |
| MarketRepay | 15.0 | -0.0015 |
| MarketBorrow | 34.0 | 0.0008 |
| MarketWithdraw | 221.0 | 0.0787 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 12 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |
| MarketSupply | 1 |


---

## eth_wbtc_usdt

- **Max total supply (USD)**: 529,825,941.69
- **Total events**: 19,355
- **Number of users**: 383
- **Number of spikes**: 15

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 370.0 | -0.0880 |
| MarketRepay | 15.0 | -0.0018 |
| MarketBorrow | 33.0 | 0.0016 |
| MarketWithdraw | 231.0 | 0.0857 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 11 |
| MarketSupply | 2 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |
| MarketSupply,MarketWithdraw | 1 |


---

## eth_rlp_usdc

- **Max total supply (USD)**: 116,092,979.43
- **Total events**: 41,097
- **Number of users**: 374
- **Number of spikes**: 88

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 770.0 | -0.0422 |
| MarketRepay | 66.0 | -0.0225 |
| MarketBorrow | 4.0 | -0.0087 |
| MarketWithdraw | 583.0 | 0.0107 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 82 |
| MarketSupply,MarketWithdraw | 3 |
| MarketSupply | 3 |


---

## eth_mhyper_usdc

- **Max total supply (USD)**: 142,136,439.88
- **Total events**: 7,576
- **Number of users**: 262
- **Number of spikes**: 1

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 8.0 | -0.0308 |
| MarketRepay | 5.0 | -0.0008 |
| MarketWithdraw | 22.0 | 0.0152 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 1 |


---

## eth_usde_dai

- **Max total supply (USD)**: 154,685,204.51
- **Total events**: 3,217
- **Number of users**: 246
- **Number of spikes**: 1

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 6.0 | -0.0675 |
| MarketBorrow | 1.0 | 0.0002 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_wsteth_usdt

- **Max total supply (USD)**: 339,293,759.74
- **Total events**: 9,390
- **Number of users**: 240
- **Number of spikes**: 24

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketBorrow | 5.0 | -0.1079 |
| MarketRepay | 22.0 | -0.0681 |
| MarketSupply | 182.0 | -0.0640 |
| MarketWithdraw | 104.0 | 0.0167 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 22 |
| MarketBorrow,MarketSupplyCollateral | 1 |
| MarketSupply,MarketWithdraw | 1 |


---

## eth_syrupusdc_usdc

- **Max total supply (USD)**: 82,162,860.77
- **Total events**: 24,139
- **Number of users**: 184
- **Number of spikes**: 176

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 10.0 | -0.0823 |
| MarketSupply | 576.0 | -0.0683 |
| MarketBorrow | 1.0 | -0.0000 |
| MarketWithdraw | 268.0 | 0.0318 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 167 |
| MarketBorrow,MarketSupplyCollateral | 3 |
| MarketSupply,MarketWithdraw | 3 |
| MarketSupply | 1 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_csusdl_usdc

- **Max total supply (USD)**: 60,996,761.69
- **Total events**: 7,401
- **Number of users**: 105
- **Number of spikes**: 37

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 125.0 | -0.0994 |
| MarketRepay | 11.0 | -0.0135 |
| MarketWithdraw | 82.0 | 0.0359 |
| MarketBorrow | 5.0 | 0.0378 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 32 |
| MarketSupply,MarketWithdraw | 2 |
| MarketBorrow | 1 |
| MarketSupply | 1 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_slvlusd_usdc

- **Max total supply (USD)**: 67,373,880.68
- **Total events**: 8,636
- **Number of users**: 101
- **Number of spikes**: 32

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 72.0 | -0.0761 |
| MarketRepay | 7.0 | -0.0068 |
| MarketBorrow | 1.0 | 0.0008 |
| MarketWithdraw | 13.0 | 0.0199 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 27 |
| MarketBorrow,MarketSupply | 2 |
| MarketSupply,MarketWithdraw | 1 |
| MarketBorrow,MarketSupplyCollateral | 1 |
| MarketBorrow | 1 |


---

## eth_weth_usdt

- **Max total supply (USD)**: 614,128.00
- **Total events**: 1,522
- **Number of users**: 98
- **Number of spikes**: 4

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 57.0 | -0.6621 |
| MarketRepay | 16.0 | -0.0247 |
| MarketBorrow | 5.0 | 0.0122 |
| MarketWithdraw | 44.0 | 0.6760 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 4 |


---

## eth_reusd_usdc

- **Max total supply (USD)**: 9,983,558.96
- **Total events**: 5,335
- **Number of users**: 81
- **Number of spikes**: 29

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 145.0 | -0.0748 |
| MarketWithdraw | 107.0 | 0.0293 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 28 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_fxsave_usdc

- **Max total supply (USD)**: 39,034,562.39
- **Total events**: 7,941
- **Number of users**: 74
- **Number of spikes**: 61

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 181.0 | -0.0904 |
| MarketRepay | 3.0 | -0.0655 |
| MarketWithdraw | 78.0 | 0.0267 |
| MarketBorrow | 2.0 | 0.0434 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 60 |
| MarketSupply,MarketWithdraw | 1 |


---

## eth_wstusr_usdc

- **Max total supply (USD)**: 43,945,273.28
- **Total events**: 9,882
- **Number of users**: 73
- **Number of spikes**: 14

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 413.0 | -1.4083 |
| MarketWithdraw | 344.0 | 1.9235 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 13 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_siusd_usdc

- **Max total supply (USD)**: 95,936,123.41
- **Total events**: 14,812
- **Number of users**: 72
- **Number of spikes**: 20

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 13.0 | -0.0558 |
| MarketSupply | 164.0 | -0.0362 |
| MarketBorrow | 3.0 | -0.0011 |
| MarketWithdraw | 136.0 | 0.0169 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 19 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_stcusd_usdc

- **Max total supply (USD)**: 71,069,966.39
- **Total events**: 10,297
- **Number of users**: 53
- **Number of spikes**: 29

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 222.0 | -0.0385 |
| MarketRepay | 21.0 | -0.0269 |
| MarketWithdraw | 159.0 | 0.0142 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 14 |
| MarketSupply,MarketWithdraw | 9 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketSupply | 1 |


---

## eth_cbbtc_usdt

- **Max total supply (USD)**: 217,438,076.11
- **Total events**: 829
- **Number of users**: 44
- **Number of spikes**: 10

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 27.0 | -0.0851 |
| MarketBorrow | 2.0 | 0.0003 |
| MarketWithdraw | 11.0 | 0.0284 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 8 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |
| MarketSupply,MarketWithdraw | 1 |


---

## eth_wsrusd_usdc

- **Max total supply (USD)**: 100,015,387.35
- **Total events**: 6,423
- **Number of users**: 44
- **Number of spikes**: 9

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 23.0 | -0.0324 |
| MarketRepay | 59.0 | -0.0163 |
| MarketBorrow | 25.0 | 0.0036 |
| MarketWithdraw | 10.0 | 0.0313 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 9 |


---

## eth_sdeusd_usdc

- **Max total supply (USD)**: 69,911,852.93
- **Total events**: 12,733
- **Number of users**: 42
- **Number of spikes**: 50

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 104.0 | -0.0958 |
| MarketRepay | 6.0 | -0.0543 |
| MarketWithdraw | 35.0 | 0.0550 |
| MarketBorrow | 1.0 | 0.0743 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 47 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |


---

## eth_mapollo_usdc

- **Max total supply (USD)**: 5,370,054.71
- **Total events**: 406
- **Number of users**: 26
- **Number of spikes**: 4

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 4.0 | -0.1244 |
| MarketBorrow | 1.0 | 0.0217 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketWithdraw | 2 |


---

## eth_syrupusdc_pyusd

- **Max total supply (USD)**: 30,014,681.10
- **Total events**: 286
- **Number of users**: 25
- **Number of spikes**: 3

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 11.0 | -0.0897 |
| MarketRepay | 4.0 | -0.0861 |
| MarketBorrow | 1.0 | 0.0854 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 1 |
| MarketBorrow,MarketSupplyCollateral | 1 |
| MarketBorrow | 1 |


---

## eth_PT-reUSD-25JUN2026_usdc

- **Max total supply (USD)**: 53,310,153.67
- **Total events**: 13,284
- **Number of users**: 293
- **Number of spikes**: 6

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 135.0 | -0.0136 |
| MarketRepay | 16.0 | -0.0025 |
| MarketBorrow | 62.0 | 0.0004 |
| MarketWithdraw | 82.0 | 0.0147 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 6 |


---

## eth_PT-USDe-25SEP2025_usdc

- **Max total supply (USD)**: 418,822,963.58
- **Total events**: 12,543
- **Number of users**: 235
- **Number of spikes**: 13

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 24.0 | -0.0454 |
| MarketSupply | 119.0 | -0.0310 |
| MarketWithdraw | 67.0 | 0.0396 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 13 |


---

## PT-reUSD-25JUN2026_usdc

- **Max total supply (USD)**: 53,867,791.40
- **Total events**: 9,270
- **Number of users**: 176
- **Number of spikes**: 0

*No spikes detected or insufficient data for action analysis.*

---

## eth_PT-USDe-27MAR2025_dai

- **Max total supply (USD)**: 126,211,463.34
- **Total events**: 2,181
- **Number of users**: 133
- **Number of spikes**: 7

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 30.0 | -0.1095 |
| MarketRepay | 31.0 | -0.0608 |
| MarketWithdraw | 10.0 | 0.0071 |
| MarketBorrow | 4.0 | 0.0107 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 5 |
| MarketBorrow,MarketSupplyCollateral | 2 |


---

## eth_PT-USDe-25SEP2025_dai

- **Max total supply (USD)**: 504,042,081.14
- **Total events**: 2,875
- **Number of users**: 129
- **Number of spikes**: 0

*No spikes detected or insufficient data for action analysis.*

---

## eth_PT-USDe-25SEP2025_usdt

- **Max total supply (USD)**: 58,360,881.73
- **Total events**: 3,769
- **Number of users**: 117
- **Number of spikes**: 11

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 51.0 | -0.0983 |
| MarketRepay | 29.0 | -0.0216 |
| MarketBorrow | 1.0 | 0.0000 |
| MarketWithdraw | 23.0 | 0.0502 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 11 |


---

## eth_PT-csUSDL-31JUL2025_usdc

- **Max total supply (USD)**: 31,582,576.18
- **Total events**: 4,793
- **Number of users**: 112
- **Number of spikes**: 23

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 77.0 | -0.1038 |
| MarketRepay | 2.0 | -0.0003 |
| MarketWithdraw | 61.0 | 0.0212 |
| MarketBorrow | 1.0 | 0.0624 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 19 |
| MarketSupply,MarketWithdraw | 2 |
| MarketBorrow | 1 |
| MarketSupply | 1 |


---

## eth_PT-sNUSD-5MAR2026_usdc

- **Max total supply (USD)**: 11,460,920.52
- **Total events**: 2,432
- **Number of users**: 106
- **Number of spikes**: 11

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 44.0 | -0.0547 |
| MarketRepay | 5.0 | -0.0201 |
| MarketBorrow | 1.0 | -0.0015 |
| MarketWithdraw | 13.0 | 0.0545 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 10 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_PT-mHYPER-20NOV2025_usdc

- **Max total supply (USD)**: 38,891,074.29
- **Total events**: 2,359
- **Number of users**: 101
- **Number of spikes**: 4

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 14.0 | -0.2069 |
| MarketSupply | 28.0 | -0.0356 |
| MarketWithdraw | 64.0 | 0.0108 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 3 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_PT-stcUSD-29JAN2026_usdc

- **Max total supply (USD)**: 60,017,452.09
- **Total events**: 7,702
- **Number of users**: 100
- **Number of spikes**: 14

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 111.0 | -0.0528 |
| MarketRepay | 32.0 | -0.0248 |
| MarketBorrow | 3.0 | -0.0010 |
| MarketWithdraw | 87.0 | 0.0179 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 11 |
| MarketRepay | 1 |
| MarketBorrow | 1 |
| MarketSupply,MarketWithdraw | 1 |


---

## eth_PT-USDe-31JUL2025_dai

- **Max total supply (USD)**: 10,439,187.23
- **Total events**: 1,604
- **Number of users**: 97
- **Number of spikes**: 14

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 29.0 | -0.4832 |
| MarketRepay | 9.0 | -0.0325 |
| MarketBorrow | 2.0 | 0.0003 |
| MarketWithdraw | 15.0 | 0.0468 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 12 |
| MarketWithdrawCollateral | 1 |
| MarketBorrow | 1 |


---

## eth_PT-RLP-4SEP2025_usdc

- **Max total supply (USD)**: 16,632,337.06
- **Total events**: 2,845
- **Number of users**: 66
- **Number of spikes**: 24

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 70.0 | -0.0625 |
| MarketRepay | 3.0 | -0.0001 |
| MarketWithdraw | 25.0 | 0.0310 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 23 |
| MarketRepay,MarketWithdraw,MarketWithdrawCollateral | 1 |


---

## eth_PT-wstUSR-25SEP2025_usdc

- **Max total supply (USD)**: 17,812,907.25
- **Total events**: 2,987
- **Number of users**: 64
- **Number of spikes**: 37

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 50.0 | -0.0966 |
| MarketRepay | 1.0 | -0.0005 |
| MarketWithdraw | 7.0 | 0.0117 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 34 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |


---

## eth_PT-USD0++-27MAR2025_usdc

- **Max total supply (USD)**: 29,862,840.94
- **Total events**: 1,799
- **Number of users**: 61
- **Number of spikes**: 12

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 66.0 | -0.1684 |
| MarketRepay | 9.0 | -0.1461 |
| MarketWithdraw | 40.0 | 0.0475 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 12 |


---

## eth_PT-slvlUSD-29MAY2025_usdc

- **Max total supply (USD)**: 21,369,077.19
- **Total events**: 2,068
- **Number of users**: 52
- **Number of spikes**: 20

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 65.0 | -0.0667 |
| MarketBorrow | 1.0 | -0.0481 |
| MarketWithdraw | 35.0 | 0.0602 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 16 |
| MarketBorrow,MarketSupplyCollateral | 3 |
| MarketBorrow | 1 |


---

## eth_PT-syrupUSDC-28AUG2025_usdc

- **Max total supply (USD)**: 11,775,168.69
- **Total events**: 1,230
- **Number of users**: 39
- **Number of spikes**: 22

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 3.0 | -0.4521 |
| MarketSupply | 92.0 | -0.0974 |
| MarketWithdraw | 55.0 | 0.0223 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 22 |


---

## eth_PT-USDe-27NOV2025_usds

- **Max total supply (USD)**: 265,788,041.17
- **Total events**: 835
- **Number of users**: 34
- **Number of spikes**: 10

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 10.0 | -0.0706 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 7 |
| MarketBorrow | 3 |


---

## eth_PT-syrupUSDC-30OCT2025_usdc

- **Max total supply (USD)**: 38,130,515.89
- **Total events**: 3,269
- **Number of users**: 27
- **Number of spikes**: 20

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 61.0 | -0.0643 |
| MarketWithdraw | 33.0 | 0.0428 |
| MarketBorrow | 1.0 | 0.0607 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 16 |
| MarketBorrow,MarketSupply | 1 |
| MarketBorrow | 1 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |
| MarketSupply | 1 |


---

## PT-siUSD-26MAR2026_usdc

- **Max total supply (USD)**: 2,258,353.08
- **Total events**: 1,495
- **Number of users**: 13
- **Number of spikes**: 26

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 37.0 | -0.0723 |
| MarketWithdraw | 4.0 | 0.0742 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 26 |


---

## eth_PT-stcUSD-23JUL2026_usdc

- **Max total supply (USD)**: 3,114,579.50
- **Total events**: 2,667
- **Number of users**: 12
- **Number of spikes**: 41

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 1.0 | -0.0550 |
| MarketSupply | 128.0 | -0.0536 |
| MarketWithdraw | 28.0 | 0.0392 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 40 |
| MarketSupply | 1 |


---

