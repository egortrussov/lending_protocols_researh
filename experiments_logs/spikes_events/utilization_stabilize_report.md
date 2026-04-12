# Market Spike Analysis Report

## Combined Analysis Across All Markets

### Action Impact (weighted by volume) – All Markets

| Action Type | Count | Weighted Mean ΔUtil |
|-------------|-------|---------------------|
| MarketBorrow | 420.0 | 0.0216 |
| MarketLiquidation | 12.0 | -0.0019 |
| MarketRepay | 680.0 | -0.0515 |
| MarketSupply | 7686.0 | -0.0655 |
| MarketWithdraw | 4172.0 | 0.0279 |

### Weighted Mean ΔUtil by Market and Action Type

| Market | N Spikes | MarketSupply | MarketRepay | MarketLiquidation | MarketBorrow | MarketWithdraw| Address |
|---|---|---|---|---|---|---|---|
| base_cbbtc_usdc_full | 38 | **-0.0513** | -0.0001 | -0.0000 | 0.0002 | 0.0289 | 0x9103c3b4e834476c9a62ea009ba2c884ee42e94e6e314a26f04d312434191836 |
| eth_usr_usdc | 251 | **-0.0895** | -0.0852 | -0.0125 | 0.0265 | 0.0306 | 0x8e7cc042d739a365c43d0a52d5f24160fa7ae9b7e7c9a479bd02a56041d4cf77 |
| eth_wbtc_usdc | 98 | **-0.0732** | -0.0023 |  |  | 0.0077 | 0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49 |
| base_wbtc_usdc | 61 | **-0.0648** | -0.0249 |  | 0.0344 | 0.0447 | 0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49 |
| eth_cbbtc_usdc | 27 | **-0.0513** | -0.0258 | -0.0000 | 0.0159 | 0.0083 | 0x64d65c9a2d91c36d56fbc42d69e979335320169b3df63bf92789e2c8883fcc64 |
| eth_rlp_usdc | 103 | **-0.0419** | -0.0218 |  | -0.0084 | 0.0107 | 0xe1b65304edd8ceaea9b629df4c3c926a37d1216e27900505c04f14b2ed279f33 |
| base_wbtc_usdt | 16 | **-0.0667** | -0.0149 |  | 0.0095 | 0.0281 | 0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99 |
| eth_wbtc_usdt | 20 | **-0.0736** | -0.0174 |  | 0.0133 | 0.0314 | 0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99 |
| eth_PT-reUSD-25JUN2026_usdc | 0 |  |  |  |  |  | 0x9bc98c2f20ac58287ef2c860eea53a2fdc27c17a7817ff1206c0b7840cc7cd79 |
| eth_mhyper_usdc | 2 | **-0.0389** | -0.0212 |  | 0.0004 | 0.0147 | 0x95c28d447950ca6c8bbfd25fc05b80b1fd7a1cdd17a3610b4b3f1ffc8dc2e2ed |
| eth_wsteth_usdt | 28 | -0.0714 | -0.0811 |  | **-0.1080** | 0.0254 | 0xe7e9694b754c4d4f7e21faf7223f6fa71abaeb10296a4c43a54a7977149687d2 |
| eth_usde_dai | 1 |  | **-0.0040** |  | 0.0002 |  | 0xc581c5f70bd1afa283eed57d1418c6432cbff1d862f94eaf58fdd4e46afbb67f |
| eth_PT-USDe-25SEP2025_usdc | 14 | -0.0291 | **-0.0439** |  |  | 0.0377 | 0x7a5d67805cb78fad2596899e0c83719ba89df353b931582eb7d3041fd5a06dc8 |
| PT-reUSD-25JUN2026_usdc | 1 | -0.0110 | **-0.0411** |  | 0.0003 | 0.0085 | 0x9bc98c2f20ac58287ef2c860eea53a2fdc27c17a7817ff1206c0b7840cc7cd79 |
| eth_syrupusdc_usdc | 218 | **-0.0873** | -0.0823 |  | -0.0000 | 0.0297 | 0x729badf297ee9f2f6b3f717b96fd355fc6ec00422284ce1968e76647b258cf44 |
| eth_PT-stcUSD-29JAN2026_usdc | 16 | **-0.0631** | -0.0138 |  | 0.0001 | 0.0175 | 0x03f715ef1ae508ab3e1faf4dffdbf2a077d1f0ad10c5aad42cf4438d5e3328af |
| eth_PT-USDe-27MAR2025_dai | 8 | **-0.1047** | -0.0583 |  | 0.0107 | 0.0071 | 0xab0dcab71e65c05b7f241ea79a33452c87e62db387129e4abe15e458d433e4d8 |
| eth_PT-USDe-25SEP2025_dai | 0 |  |  |  |  |  | 0x45d97c66db5e803b9446802702f087d4293a2f74b370105dc3a88a278bf6bb21 |
| eth_PT-USDe-25SEP2025_usdt | 12 | **-0.0927** | -0.0208 |  | 0.0000 | 0.0383 | 0xb0a9ac81a8c6a5274aa1a8337aed35a2cb2cd4feb5c6d3b39d41f234fbf2955b |
| eth_PT-csUSDL-31JUL2025_usdc | 23 | -0.0742 | **-0.4109** |  | 0.0624 | 0.0212 | 0x544b0a093b130a3fb01b72a1279ab848575f049c73da3b5c9c718f9350a1519c |
| eth_slvlusd_usdc | 40 | **-0.0927** | -0.0067 |  | 0.0008 | 0.0245 | 0x8b1bc4d682b04a16309a8adf77b35de0c42063a7944016cfc37a79ccac0007b6 |
| eth_PT-sNUSD-5MAR2026_usdc | 11 | **-0.0547** | -0.0201 |  | -0.0015 | 0.0545 | 0x2a9a5c436719badcfadbad3ad8e8179a160ded758603eaa03a883f922a1790d3 |
| eth_PT-mHYPER-20NOV2025_usdc | 5 | -0.0395 | **-0.2069** |  | 0.0220 | 0.0108 | 0x1ca75949a91c157183f53282d73c37191e7cd84002310f6632047d874aad4a0f |
| eth_PT-USDe-31JUL2025_dai | 14 | **-0.4832** | -0.0325 |  | 0.0003 | 0.0468 | 0x760b14c9003f08ac4bf0cfb02596ee4d6f0548a4fde5826bfd56befb9ed62ae9 |
| eth_weth_usdt | 4 | -0.6621 | -0.0247 |  | 0.0122 | **0.6760** | 0xdbffac82c2dc7e8aa781bd05746530b0068d80929f23ac1628580e27810bc0c5 |
| eth_wstusr_usdc | 14 | -1.4083 |  |  |  | **1.9235** | 0xd9e34b1eed46d123ac1b69b224de1881dbc88798bc7b70f504920f62f58f28cc |
| eth_fxsave_usdc | 70 | -0.0826 | **-0.2918** |  | 0.0408 | 0.0347 | 0x43e925e52d7873fa8acac90dd5f246087d55b3a34c344b71884a6352491ff459 |
| eth_reusd_usdc | 30 | -0.0534 | **-0.2505** |  |  | 0.0296 | 0x4565ac05d38b19374ccbb04c17cca60ca9353cd41824f0803d0fc7704f60eaed |
| eth_siusd_usdc | 21 | **-0.0899** | -0.0740 |  | 0.0003 | 0.0191 | 0xbbf7ce1b40d32d3e3048f5cf27eeaa6de8cb27b80194690aab191a63381d8c99 |
| eth_PT-wstUSR-25SEP2025_usdc | 37 | **-0.0951** | -0.0143 |  | -0.0077 | 0.0225 | 0xeec6c7e2ddb7578f2a7d86fc11cf9da005df34452ad9b9189c51266216f5d71b |
| eth_stcusd_usdc | 38 | **-0.0524** | -0.0269 |  |  | 0.0150 | 0xeb17955ea422baeddbfb0b8d8c9086c5be7a9cfdefb292119a102e981a30062e |
| eth_PT-RLP-4SEP2025_usdc | 31 | -0.0568 | -0.0001 |  | **0.0967** | 0.0276 | 0xcc611d3ca8ce8dcc63e4e8c3cd17c9acb2ca1768eeb143b71e2dc8e6a98c3f65 |
| eth_PT-USD0++-27MAR2025_usdc | 16 | **-0.1532** | -0.0480 |  |  | 0.0475 | 0x147977320f168afc651b7e5a1849cc1b1e64e329e1bf0212fa49dcb2856074a4 |
| eth_PT-slvlUSD-29MAY2025_usdc | 24 | **-0.0709** |  |  |  | 0.0577 | 0xeb3e4a68c675d88f5a4378eab966e717bdee6a0f38c5ca6da2560ac5d1534f60 |
| eth_cbbtc_usdt | 11 | **-0.0844** |  |  | 0.0003 | 0.0284 | 0x45671fb8d5dea1c4fbca0b8548ad742f6643300eeb8dbd34ad64a658b2b05bca |
| eth_wsrusd_usdc | 16 | **-0.0354** | -0.0220 |  | 0.0119 | 0.0309 | 0x1590cb22d797e226df92ebc6e0153427e207299916e7e4e53461389ad68272fb |
| eth_sdeusd_usdc | 75 | **-0.0882** | -0.0563 | 0.0021 | 0.0743 | 0.0383 | 0x0f9563442d64ab3bd3bcb27058db0b0d4046a4c46f0acd811dacae9551d2b129 |
| eth_PT-syrupUSDC-28AUG2025_usdc | 26 | -0.0961 | **-0.7006** |  |  | 0.0223 | 0x3bdb58058b41bb700458ba3df317e254244ddec7fc35fec93d2d53475cc6ebdc |
| eth_PT-USDe-27NOV2025_usds | 11 | **-0.0701** |  |  |  |  | 0x8cdb63a27a48ac27fadc0f158a732104bcc4e10bb61c9a5095ea7c127204e26c |
| eth_PT-syrupUSDC-30OCT2025_usdc | 22 | -0.0589 |  |  | **0.0607** | 0.0417 | 0xb8afc953c3cc8077b4a4bf459bede8d3f80be45ca1f244e4bca13b7b1030eed5 |
| eth_mapollo_usdc | 5 | **-0.1231** | -0.0560 |  | 0.0217 | 0.0002 | 0x031c7333014af51e4fd18031d14e4eaada58348cde3f6dc6ea8cca16f7387fb2 |
| eth_syrupusdc_pyusd | 4 | **-0.0897** | -0.0861 |  | 0.0854 |  | 0xc9629945524f3fde56c7e8854a6c3d48e76b9d97236abbe73c750fcc7aeb8501 |
| PT-siUSD-26MAR2026_usdc | 28 | -0.0716 |  |  |  | **0.0742** | 0xaac3ffcdf8a75919657e789fa72ab742a7bbfdf5bb0b87e4bbeb3c29bbbbb05c |
| eth_PT-stcUSD-23JUL2026_usdc | 48 | **-0.0561** | -0.0550 |  |  | 0.0343 | 0x2fb3713487c7812e7309935b034f40228841666f6b048faf31fd2110ae674f20 |
## Summary Across All Markets

| Metric | Value |
|--------|-------|
| Number of markets processed | 44 |
| Total spikes detected | 1538 |
| Total unique users across all markets | 33353 |
| Total events across all markets | 2045008 |

## Per-Market Analysis

## base_cbbtc_usdc_full

- **Max total supply (USD)**: 1,162,816,910.67
- **Total events**: 1,583,997
- **Number of users**: 24,782
- **Number of spikes**: 38

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 692.0 | -0.0513 |
| MarketRepay | 108.0 | -0.0001 |
| MarketLiquidation | 8.0 | -0.0000 |
| MarketBorrow | 123.0 | 0.0002 |
| MarketWithdraw | 172.0 | 0.0289 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 29 |
| MarketSupply | 6 |
| MarketSupplyCollateral | 2 |
| MarketRepay,MarketWithdrawCollateral | 1 |


---

## eth_usr_usdc

- **Max total supply (USD)**: 133,737,726.89
- **Total events**: 23,055
- **Number of users**: 1,225
- **Number of spikes**: 251

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 602.0 | -0.0895 |
| MarketRepay | 27.0 | -0.0852 |
| MarketLiquidation | 1.0 | -0.0125 |
| MarketBorrow | 9.0 | 0.0265 |
| MarketWithdraw | 206.0 | 0.0306 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 244 |
| MarketSupply | 4 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |
| MarketSupply,MarketWithdraw | 1 |


---

## eth_wbtc_usdc

- **Max total supply (USD)**: 277,575,216.81
- **Total events**: 36,914
- **Number of users**: 880
- **Number of spikes**: 98

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 32.0 | -0.0732 |
| MarketRepay | 1.0 | -0.0023 |
| MarketWithdraw | 3.0 | 0.0077 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 62 |
| MarketSupply,MarketWithdraw | 15 |
| MarketSupply | 12 |
| MarketRepay,MarketWithdrawCollateral | 4 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |


---

## base_wbtc_usdc

- **Max total supply (USD)**: 269,255,896.54
- **Total events**: 26,926
- **Number of users**: 780
- **Number of spikes**: 61

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 444.0 | -0.0648 |
| MarketRepay | 33.0 | -0.0249 |
| MarketBorrow | 76.0 | 0.0344 |
| MarketWithdraw | 309.0 | 0.0447 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 58 |
| MarketSupply,MarketWithdraw | 3 |


---

## eth_cbbtc_usdc

- **Max total supply (USD)**: 607,128,500.34
- **Total events**: 48,485
- **Number of users**: 533
- **Number of spikes**: 27

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 463.0 | -0.0513 |
| MarketRepay | 26.0 | -0.0258 |
| MarketLiquidation | 1.0 | -0.0000 |
| MarketWithdraw | 187.0 | 0.0083 |
| MarketBorrow | 14.0 | 0.0159 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 18 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 7 |
| MarketSupply,MarketWithdraw | 1 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_rlp_usdc

- **Max total supply (USD)**: 154,288,632.54
- **Total events**: 47,028
- **Number of users**: 445
- **Number of spikes**: 103

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 831.0 | -0.0419 |
| MarketRepay | 79.0 | -0.0218 |
| MarketBorrow | 6.0 | -0.0084 |
| MarketWithdraw | 611.0 | 0.0107 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 94 |
| MarketSupply,MarketWithdraw | 3 |
| MarketSupply | 3 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketBorrow | 1 |


---

## base_wbtc_usdt

- **Max total supply (USD)**: 541,018,474.87
- **Total events**: 22,324
- **Number of users**: 409
- **Number of spikes**: 16

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 380.0 | -0.0667 |
| MarketRepay | 9.0 | -0.0149 |
| MarketBorrow | 40.0 | 0.0095 |
| MarketWithdraw | 260.0 | 0.0281 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 12 |
| MarketSupply,MarketWithdraw | 3 |
| MarketSupply | 1 |


---

## eth_wbtc_usdt

- **Max total supply (USD)**: 529,825,941.69
- **Total events**: 22,233
- **Number of users**: 409
- **Number of spikes**: 20

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 520.0 | -0.0736 |
| MarketRepay | 17.0 | -0.0174 |
| MarketBorrow | 45.0 | 0.0133 |
| MarketWithdraw | 301.0 | 0.0314 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 16 |
| MarketSupply,MarketWithdraw | 3 |
| MarketSupply | 1 |


---

## eth_mhyper_usdc

- **Max total supply (USD)**: 142,136,439.88
- **Total events**: 8,665
- **Number of users**: 270
- **Number of spikes**: 2

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 17.0 | -0.0389 |
| MarketRepay | 9.0 | -0.0212 |
| MarketBorrow | 13.0 | 0.0004 |
| MarketWithdraw | 36.0 | 0.0147 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 1 |
| MarketWithdraw | 1 |


---

## eth_wsteth_usdt

- **Max total supply (USD)**: 339,293,759.74
- **Total events**: 10,720
- **Number of users**: 256
- **Number of spikes**: 28

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketBorrow | 4.0 | -0.1080 |
| MarketRepay | 9.0 | -0.0811 |
| MarketSupply | 252.0 | -0.0714 |
| MarketWithdraw | 131.0 | 0.0254 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 26 |
| MarketSupply | 1 |
| MarketSupply,MarketWithdraw | 1 |


---

## eth_usde_dai

- **Max total supply (USD)**: 154,685,204.51
- **Total events**: 3,578
- **Number of users**: 253
- **Number of spikes**: 1

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 5.0 | -0.0040 |
| MarketBorrow | 1.0 | 0.0002 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_syrupusdc_usdc

- **Max total supply (USD)**: 93,767,984.11
- **Total events**: 27,590
- **Number of users**: 200
- **Number of spikes**: 218

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 670.0 | -0.0873 |
| MarketRepay | 10.0 | -0.0823 |
| MarketBorrow | 3.0 | -0.0000 |
| MarketWithdraw | 288.0 | 0.0297 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 209 |
| MarketBorrow,MarketSupplyCollateral | 3 |
| MarketSupply,MarketWithdraw | 3 |
| MarketSupply | 1 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_slvlusd_usdc

- **Max total supply (USD)**: 67,373,880.68
- **Total events**: 9,574
- **Number of users**: 114
- **Number of spikes**: 40

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 94.0 | -0.0927 |
| MarketRepay | 8.0 | -0.0067 |
| MarketBorrow | 1.0 | 0.0008 |
| MarketWithdraw | 24.0 | 0.0245 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 29 |
| MarketSupply,MarketWithdraw | 4 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketBorrow,MarketSupply | 2 |


---

## eth_weth_usdt

- **Max total supply (USD)**: 614,128.00
- **Total events**: 1,758
- **Number of users**: 99
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

## eth_wstusr_usdc

- **Max total supply (USD)**: 43,945,273.28
- **Total events**: 11,159
- **Number of users**: 92
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

## eth_fxsave_usdc

- **Max total supply (USD)**: 39,034,562.39
- **Total events**: 9,128
- **Number of users**: 87
- **Number of spikes**: 70

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 6.0 | -0.2918 |
| MarketSupply | 217.0 | -0.0826 |
| MarketWithdraw | 92.0 | 0.0347 |
| MarketBorrow | 3.0 | 0.0408 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 66 |
| MarketBorrow,MarketSupplyCollateral | 3 |
| MarketSupply,MarketWithdraw | 1 |


---

## eth_reusd_usdc

- **Max total supply (USD)**: 13,221,619.01
- **Total events**: 6,099
- **Number of users**: 87
- **Number of spikes**: 30

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 1.0 | -0.2505 |
| MarketSupply | 149.0 | -0.0534 |
| MarketWithdraw | 115.0 | 0.0296 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 29 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_siusd_usdc

- **Max total supply (USD)**: 95,936,123.41
- **Total events**: 17,135
- **Number of users**: 80
- **Number of spikes**: 21

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 139.0 | -0.0899 |
| MarketRepay | 14.0 | -0.0740 |
| MarketBorrow | 2.0 | 0.0003 |
| MarketWithdraw | 118.0 | 0.0191 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 20 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_stcusd_usdc

- **Max total supply (USD)**: 71,069,966.39
- **Total events**: 11,776
- **Number of users**: 66
- **Number of spikes**: 38

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 210.0 | -0.0524 |
| MarketRepay | 21.0 | -0.0269 |
| MarketWithdraw | 140.0 | 0.0150 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 21 |
| MarketSupply,MarketWithdraw | 9 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 5 |
| MarketBorrow,MarketSupplyCollateral | 3 |


---

## eth_cbbtc_usdt

- **Max total supply (USD)**: 239,531,763.80
- **Total events**: 970
- **Number of users**: 45
- **Number of spikes**: 11

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 28.0 | -0.0844 |
| MarketBorrow | 2.0 | 0.0003 |
| MarketWithdraw | 11.0 | 0.0284 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 9 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |
| MarketSupply,MarketWithdraw | 1 |


---

## eth_wsrusd_usdc

- **Max total supply (USD)**: 100,015,387.35
- **Total events**: 7,345
- **Number of users**: 44
- **Number of spikes**: 16

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 42.0 | -0.0354 |
| MarketRepay | 79.0 | -0.0220 |
| MarketBorrow | 41.0 | 0.0119 |
| MarketWithdraw | 15.0 | 0.0309 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 13 |
| MarketBorrow,MarketSupplyCollateral | 3 |


---

## eth_sdeusd_usdc

- **Max total supply (USD)**: 82,421,369.96
- **Total events**: 14,600
- **Number of users**: 43
- **Number of spikes**: 75

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 251.0 | -0.0882 |
| MarketRepay | 6.0 | -0.0563 |
| MarketLiquidation | 2.0 | 0.0021 |
| MarketWithdraw | 128.0 | 0.0383 |
| MarketBorrow | 3.0 | 0.0743 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 72 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |


---

## eth_mapollo_usdc

- **Max total supply (USD)**: 5,370,054.71
- **Total events**: 468
- **Number of users**: 27
- **Number of spikes**: 5

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 5.0 | -0.1231 |
| MarketRepay | 1.0 | -0.0560 |
| MarketWithdraw | 2.0 | 0.0002 |
| MarketBorrow | 1.0 | 0.0217 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 3 |
| MarketBorrow,MarketSupplyCollateral | 2 |


---

## eth_syrupusdc_pyusd

- **Max total supply (USD)**: 30,014,681.10
- **Total events**: 336
- **Number of users**: 25
- **Number of spikes**: 4

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 11.0 | -0.0897 |
| MarketRepay | 4.0 | -0.0861 |
| MarketBorrow | 1.0 | 0.0854 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 2 |
| MarketBorrow,MarketSupplyCollateral | 1 |
| MarketBorrow | 1 |


---

## eth_PT-reUSD-25JUN2026_usdc

- **Max total supply (USD)**: 53,867,791.40
- **Total events**: 15,181
- **Number of users**: 300
- **Number of spikes**: 0

*No spikes detected or insufficient data for action analysis.*

---

## eth_PT-USDe-25SEP2025_usdc

- **Max total supply (USD)**: 418,822,963.58
- **Total events**: 14,256
- **Number of users**: 252
- **Number of spikes**: 14

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 28.0 | -0.0439 |
| MarketSupply | 134.0 | -0.0291 |
| MarketWithdraw | 82.0 | 0.0377 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 13 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## PT-reUSD-25JUN2026_usdc

- **Max total supply (USD)**: 54,243,591.24
- **Total events**: 10,595
- **Number of users**: 202
- **Number of spikes**: 1

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 1.0 | -0.0411 |
| MarketSupply | 16.0 | -0.0110 |
| MarketBorrow | 1.0 | 0.0003 |
| MarketWithdraw | 7.0 | 0.0085 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_PT-stcUSD-29JAN2026_usdc

- **Max total supply (USD)**: 60,017,452.09
- **Total events**: 8,831
- **Number of users**: 141
- **Number of spikes**: 16

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 63.0 | -0.0631 |
| MarketRepay | 48.0 | -0.0138 |
| MarketBorrow | 5.0 | 0.0001 |
| MarketWithdraw | 93.0 | 0.0175 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 15 |
| MarketRepay | 1 |


---

## eth_PT-USDe-27MAR2025_dai

- **Max total supply (USD)**: 126,211,463.34
- **Total events**: 2,339
- **Number of users**: 135
- **Number of spikes**: 8

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 32.0 | -0.1047 |
| MarketRepay | 32.0 | -0.0583 |
| MarketWithdraw | 10.0 | 0.0071 |
| MarketBorrow | 4.0 | 0.0107 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 5 |
| MarketBorrow,MarketSupplyCollateral | 3 |


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
- **Number of spikes**: 12

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 68.0 | -0.0927 |
| MarketRepay | 32.0 | -0.0208 |
| MarketBorrow | 1.0 | 0.0000 |
| MarketWithdraw | 30.0 | 0.0383 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 12 |


---

## eth_PT-csUSDL-31JUL2025_usdc

- **Max total supply (USD)**: 31,582,576.18
- **Total events**: 5,483
- **Number of users**: 115
- **Number of spikes**: 23

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 3.0 | -0.4109 |
| MarketSupply | 78.0 | -0.0742 |
| MarketWithdraw | 60.0 | 0.0212 |
| MarketBorrow | 1.0 | 0.0624 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 19 |
| MarketSupply,MarketWithdraw | 2 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |
| MarketBorrow | 1 |


---

## eth_PT-sNUSD-5MAR2026_usdc

- **Max total supply (USD)**: 11,460,920.52
- **Total events**: 2,811
- **Number of users**: 111
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
- **Total events**: 2,701
- **Number of users**: 106
- **Number of spikes**: 5

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 14.0 | -0.2069 |
| MarketSupply | 31.0 | -0.0395 |
| MarketWithdraw | 64.0 | 0.0108 |
| MarketBorrow | 1.0 | 0.0220 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 3 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |


---

## eth_PT-USDe-31JUL2025_dai

- **Max total supply (USD)**: 10,439,187.23
- **Total events**: 1,835
- **Number of users**: 104
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
| MarketBorrow,MarketSupplyCollateral | 1 |
| MarketBorrow | 1 |


---

## eth_PT-wstUSR-25SEP2025_usdc

- **Max total supply (USD)**: 17,812,907.25
- **Total events**: 3,406
- **Number of users**: 67
- **Number of spikes**: 37

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 67.0 | -0.0951 |
| MarketRepay | 2.0 | -0.0143 |
| MarketBorrow | 9.0 | -0.0077 |
| MarketWithdraw | 22.0 | 0.0225 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 33 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_PT-RLP-4SEP2025_usdc

- **Max total supply (USD)**: 16,632,337.06
- **Total events**: 3,235
- **Number of users**: 66
- **Number of spikes**: 31

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 95.0 | -0.0568 |
| MarketRepay | 3.0 | -0.0001 |
| MarketWithdraw | 36.0 | 0.0276 |
| MarketBorrow | 1.0 | 0.0967 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 30 |
| MarketRepay,MarketWithdraw,MarketWithdrawCollateral | 1 |


---

## eth_PT-USD0++-27MAR2025_usdc

- **Max total supply (USD)**: 29,862,840.94
- **Total events**: 2,052
- **Number of users**: 66
- **Number of spikes**: 16

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 74.0 | -0.1532 |
| MarketRepay | 9.0 | -0.0480 |
| MarketWithdraw | 40.0 | 0.0475 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 16 |


---

## eth_PT-slvlUSD-29MAY2025_usdc

- **Max total supply (USD)**: 21,369,077.19
- **Total events**: 2,235
- **Number of users**: 52
- **Number of spikes**: 24

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 52.0 | -0.0709 |
| MarketWithdraw | 19.0 | 0.0577 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 17 |
| MarketBorrow,MarketSupplyCollateral | 6 |
| MarketBorrow | 1 |


---

## eth_PT-syrupUSDC-28AUG2025_usdc

- **Max total supply (USD)**: 11,775,168.69
- **Total events**: 1,407
- **Number of users**: 39
- **Number of spikes**: 26

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 4.0 | -0.7006 |
| MarketSupply | 98.0 | -0.0961 |
| MarketWithdraw | 57.0 | 0.0223 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 26 |


---

## eth_PT-USDe-27NOV2025_usds

- **Max total supply (USD)**: 265,788,041.17
- **Total events**: 931
- **Number of users**: 35
- **Number of spikes**: 11

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 11.0 | -0.0701 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 8 |
| MarketBorrow | 3 |


---

## eth_PT-syrupUSDC-30OCT2025_usdc

- **Max total supply (USD)**: 38,130,515.89
- **Total events**: 3,819
- **Number of users**: 27
- **Number of spikes**: 22

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 67.0 | -0.0589 |
| MarketWithdraw | 34.0 | 0.0417 |
| MarketBorrow | 1.0 | 0.0607 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 18 |
| MarketBorrow,MarketSupply | 1 |
| MarketBorrow | 1 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |
| MarketSupply | 1 |


---

## PT-siUSD-26MAR2026_usdc

- **Max total supply (USD)**: 2,258,353.08
- **Total events**: 1,718
- **Number of users**: 16
- **Number of spikes**: 28

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 40.0 | -0.0716 |
| MarketWithdraw | 4.0 | 0.0742 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 28 |


---

## eth_PT-stcUSD-23JUL2026_usdc

- **Max total supply (USD)**: 3,114,579.50
- **Total events**: 3,089
- **Number of users**: 12
- **Number of spikes**: 48

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 168.0 | -0.0561 |
| MarketRepay | 1.0 | -0.0550 |
| MarketWithdraw | 49.0 | 0.0343 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 47 |
| MarketSupply | 1 |


---

