# Market Spike Analysis Report

## Combined Analysis Across All Markets

### Action Impact (weighted by volume) – All Markets

| Action Type | Count | Weighted Mean ΔUtil |
|-------------|-------|---------------------|
| MarketBorrow | 2951.0 | 0.0007 |
| MarketLiquidation | 5.0 | -0.0445 |
| MarketRepay | 2915.0 | -0.0593 |
| MarketSupply | 23622.0 | -0.0697 |
| MarketWithdraw | 10665.0 | 0.0112 |

### Weighted Mean ΔUtil by Market and Action Type

| Market | N Spikes | MarketSupply | MarketRepay | MarketBorrow | MarketWithdraw | MarketLiquidation| Address |
|---|---|---|---|---|---|---|---|
| eth_usr_usdc | 384 | **-0.0685** | -0.0123 | -0.0073 | 0.0163 |  | 0x8e7cc042d739a365c43d0a52d5f24160fa7ae9b7e7c9a479bd02a56041d4cf77 |
| eth_wsteth_usdc | 61 | **-0.0461** | -0.0386 | 0.0048 | 0.0164 | -0.0029 | 0xb323495f7e4148be5643a4ea4a8221eef163e4bccfdedc2a6f4696baacbc86cc |
| eth_wbtc_usdc | 80 | -0.0494 | -0.0224 | **-0.0512** | 0.0136 |  | 0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49 |
| base_wbtc_usdc | 358 | **-0.0536** | -0.0235 | 0.0039 | 0.0119 |  | 0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49 |
| eth_rlp_usdc | 767 | -0.0533 | **-0.0556** | 0.0085 | 0.0059 |  | 0xe1b65304edd8ceaea9b629df4c3c926a37d1216e27900505c04f14b2ed279f33 |
| eth_cbbtc_usdc | 216 | **-0.0597** | -0.0336 | 0.0061 | 0.0090 |  | 0x64d65c9a2d91c36d56fbc42d69e979335320169b3df63bf92789e2c8883fcc64 |
| base_wbtc_usdt | 268 | **-0.0627** | -0.0271 | 0.0065 | 0.0115 |  | 0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99 |
| eth_wbtc_usdt | 298 | **-0.0684** | -0.0289 | 0.0068 | 0.0125 |  | 0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99 |
| eth_usd0++_usdc | 106 | **-0.0448** | -0.0144 | -0.0022 | 0.0116 |  | 0x1eda1b67414336cab3914316cb58339ddaef9e43f939af1fed162a989c98bc20 |
| eth_PT-reUSD-25JUN2026_usdc | 32 | -0.0323 | **-0.0331** | 0.0040 | 0.0140 |  | 0x9bc98c2f20ac58287ef2c860eea53a2fdc27c17a7817ff1206c0b7840cc7cd79 |
| eth_wsteth_usdt | 297 | **-0.0805** | -0.0555 | -0.0540 | 0.0089 |  | 0xe7e9694b754c4d4f7e21faf7223f6fa71abaeb10296a4c43a54a7977149687d2 |
| eth_PT-USDe-25SEP2025_usdc | 75 | -0.0456 | **-0.0481** | 0.0037 | 0.0088 |  | 0x7a5d67805cb78fad2596899e0c83719ba89df353b931582eb7d3041fd5a06dc8 |
| eth_usde_dai | 12 | -0.0036 | -0.0109 | 0.0067 | 0.0088 | **-0.0469** | 0xc581c5f70bd1afa283eed57d1418c6432cbff1d862f94eaf58fdd4e46afbb67f |
| eth_mhyper_usdc | 142 | **-0.0720** | -0.0140 | 0.0146 | 0.0131 |  | 0x95c28d447950ca6c8bbfd25fc05b80b1fd7a1cdd17a3610b4b3f1ffc8dc2e2ed |
| eth_syrupusdc_usdc | 681 | -0.0800 | **-0.1173** | 0.0077 | 0.0147 |  | 0x729badf297ee9f2f6b3f717b96fd355fc6ec00422284ce1968e76647b258cf44 |
| PT-reUSD-25JUN2026_usdc | 29 | -0.0322 | **-0.0352** | 0.0041 | 0.0142 |  | 0x9bc98c2f20ac58287ef2c860eea53a2fdc27c17a7817ff1206c0b7840cc7cd79 |
| eth_wstusr_usdc | 869 | -0.0944 | **-0.1528** | -0.0066 | -0.0161 |  | 0xd9e34b1eed46d123ac1b69b224de1881dbc88798bc7b70f504920f62f58f28cc |
| eth_PT-stcUSD-29JAN2026_usdc | 203 | -0.0617 | **-0.0740** | 0.0156 | 0.0131 |  | 0x03f715ef1ae508ab3e1faf4dffdbf2a077d1f0ad10c5aad42cf4438d5e3328af |
| eth_PT-USDe-27MAR2025_dai | 18 | **-0.0704** | -0.0274 | 0.0073 | 0.0069 |  | 0xab0dcab71e65c05b7f241ea79a33452c87e62db387129e4abe15e458d433e4d8 |
| eth_slvlusd_usdc | 198 | **-0.0957** | -0.0261 | 0.0001 | 0.0145 |  | 0x8b1bc4d682b04a16309a8adf77b35de0c42063a7944016cfc37a79ccac0007b6 |
| eth_PT-USDe-25SEP2025_usdt | 61 | **-0.0721** | -0.0524 | 0.0165 | 0.0098 |  | 0xb0a9ac81a8c6a5274aa1a8337aed35a2cb2cd4feb5c6d3b39d41f234fbf2955b |
| eth_PT-USDe-25SEP2025_dai | 0 |  |  |  |  |  | 0x45d97c66db5e803b9446802702f087d4293a2f74b370105dc3a88a278bf6bb21 |
| eth_PT-csUSDL-31JUL2025_usdc | 138 | **-0.1263** | -0.0748 | 0.0053 | 0.0130 |  | 0x544b0a093b130a3fb01b72a1279ab848575f049c73da3b5c9c718f9350a1519c |
| eth_PT-sNUSD-5MAR2026_usdc | 37 | **-0.0529** | -0.0149 | 0.0027 | 0.0158 |  | 0x2a9a5c436719badcfadbad3ad8e8179a160ded758603eaa03a883f922a1790d3 |
| eth_csusdl_usdc | 247 | **-0.0869** | -0.0005 | -0.0042 | 0.0149 |  | 0x83b7ad16905809ea36482f4fbf6cfee9c9f316d128de9a5da1952607d5e4df5e |
| eth_weth_usdt | 79 | **-1.1401** | -0.1874 | -0.0083 | 0.0154 |  | 0xdbffac82c2dc7e8aa781bd05746530b0068d80929f23ac1628580e27810bc0c5 |
| eth_PT-USDe-31JUL2025_dai | 22 | -0.0499 | **-0.1508** | 0.0211 | 0.0160 |  | 0x760b14c9003f08ac4bf0cfb02596ee4d6f0548a4fde5826bfd56befb9ed62ae9 |
| eth_PT-mHYPER-20NOV2025_usdc | 67 | -0.0530 | **-0.2275** | 0.0207 | 0.0112 |  | 0x1ca75949a91c157183f53282d73c37191e7cd84002310f6632047d874aad4a0f |
| eth_PT-lvlUSD-29MAY2025_usdc | 91 | -0.2304 | -0.0657 | **-0.4739** | 0.0148 |  | 0x185df29d35001b5657c9c964284ddbeee83a40c83e6c6e89432463e2157e075c |
| eth_mF-ONE_usdc | 235 | -0.1183 | **-0.1351** | 0.0228 | 0.0104 |  | 0xef2c308b5abecf5c8750a1aa82b47c558005feb7a03f4f8e1ad682d71ac8d0ba |
| eth_fxsave_usdc | 370 | -0.0765 | **-0.2391** | 0.0163 | 0.0105 |  | 0x43e925e52d7873fa8acac90dd5f246087d55b3a34c344b71884a6352491ff459 |
| eth_PT-slvlUSD-25SEP2025_usdc | 133 | -0.0556 | -0.0769 | **-0.1457** | 0.0144 | -0.0168 | 0x4005ba6eb7d2221fe58102bd320aa6d83c47b212771bc950ab71c5074d9ab0ec |
| eth_reusd_usdc | 187 | **-0.1229** |  | 0.0053 | 0.0117 |  | 0x4565ac05d38b19374ccbb04c17cca60ca9353cd41824f0803d0fc7704f60eaed |
| eth_siusd_usdc | 122 | **-0.0533** | -0.0330 | 0.0142 | 0.0131 |  | 0xbbf7ce1b40d32d3e3048f5cf27eeaa6de8cb27b80194690aab191a63381d8c99 |
| eth_stcusd_usdc | 305 | -0.0514 | **-0.0691** | 0.0189 | 0.0128 |  | 0xeb17955ea422baeddbfb0b8d8c9086c5be7a9cfdefb292119a102e981a30062e |
| eth_PT-USD0++-27MAR2025_usdc | 96 | -0.1165 | **-0.1477** | -0.0136 | 0.0183 |  | 0x147977320f168afc651b7e5a1849cc1b1e64e329e1bf0212fa49dcb2856074a4 |
| eth_PT-RLP-4SEP2025_usdc | 167 | **-0.0902** | -0.0414 | -0.0719 | 0.0125 |  | 0xcc611d3ca8ce8dcc63e4e8c3cd17c9acb2ca1768eeb143b71e2dc8e6a98c3f65 |
| eth_PT-wstUSR-25SEP2025_usdc | 170 | -0.0918 | **-0.7872** | -0.0322 | 0.0137 |  | 0xeec6c7e2ddb7578f2a7d86fc11cf9da005df34452ad9b9189c51266216f5d71b |
| eth_PT-reUSD-18DEC2025_usdc | 24 | **-0.1020** | -0.0987 | 0.0000 | 0.0158 |  | 0xf5de1cd86d1b96dae889356d9515a1ccfd6caae8570f8d6d49c218bb203d045d |
| eth_PT-slvlUSD-29MAY2025_usdc | 69 | -0.0571 | -0.0031 | **-0.0995** | 0.0111 |  | 0xeb3e4a68c675d88f5a4378eab966e717bdee6a0f38c5ca6da2560ac5d1534f60 |
| eth_sdeusd_usdc | 414 | **-0.0851** | -0.0366 | 0.0025 | 0.0139 | 0.0021 | 0x0f9563442d64ab3bd3bcb27058db0b0d4046a4c46f0acd811dacae9551d2b129 |
| eth_susde_pyusd | 17 | -0.0489 | **-0.1147** | 0.0024 |  |  | 0x90ef0c5a0dc7c4de4ad4585002d44e9d411d212d2f6258e94948beecf8b4c0d5 |
| eth_PT-wstUSR-27MAR2025_usr | 38 | **-0.2622** | -0.1094 | -0.0156 | 0.0082 |  | 0x1e1ae51d4be670307788612599a46a73649ef85e28bab194d3ae00c3cd693ea7 |
| eth_wsrusd_usdc | 49 | **-0.0412** | -0.0203 | 0.0098 | 0.0144 |  | 0x1590cb22d797e226df92ebc6e0153427e207299916e7e4e53461389ad68272fb |
| eth_cbbtc_usdt | 15 | **-0.1909** | -0.0285 | 0.0241 | 0.0158 |  | 0x45671fb8d5dea1c4fbca0b8548ad742f6643300eeb8dbd34ad64a658b2b05bca |
| eth_PT-syrupUSDC-28AUG2025_usdc | 63 | -0.0799 | **-0.1224** | 0.0000 | 0.0167 |  | 0x3bdb58058b41bb700458ba3df317e254244ddec7fc35fec93d2d53475cc6ebdc |
| eth_PT-USDe-27NOV2025_usds | 27 | **-0.1157** | -0.0025 | 0.0176 | 0.0081 |  | 0x8cdb63a27a48ac27fadc0f158a732104bcc4e10bb61c9a5095ea7c127204e26c |
| eth_mapollo_usdc | 17 | **-0.1376** | -0.0669 | 0.0217 | 0.0072 |  | 0x031c7333014af51e4fd18031d14e4eaada58348cde3f6dc6ea8cca16f7387fb2 |
| eth_PT-syrupUSDC-30OCT2025_usdc | 130 | **-0.0694** | -0.0001 | 0.0045 | 0.0148 |  | 0xb8afc953c3cc8077b4a4bf459bede8d3f80be45ca1f244e4bca13b7b1030eed5 |
| eth_syrupusdc_pyusd | 5 | -0.0648 | **-0.0699** | 0.0054 | 0.0111 |  | 0xc9629945524f3fde56c7e8854a6c3d48e76b9d97236abbe73c750fcc7aeb8501 |
| eth_PT-USR-29MAY2025_usdc | 62 | **-0.0768** | -0.0235 | 0.0201 | 0.0104 |  | 0x278290bf72ec20495f3f57910bebac7f2f6a6aeff9e9d550f225b4ba26454fe0 |
| eth_PT-sdeUSD-1753142406_usdc | 57 | **-0.1325** |  |  | 0.0116 |  | 0x4ef32e4877329436968f4a29b0c8285531d113dad29b727d88beafe5ed45be6a |
| PT-siUSD-26MAR2026_usdc | 124 | **-0.0714** | -0.0000 | -0.0118 | 0.0108 |  | 0xaac3ffcdf8a75919657e789fa72ab742a7bbfdf5bb0b87e4bbeb3c29bbbbb05c |
| eth_PT-stcUSD-23JUL2026_usdc | 262 | **-0.0633** |  |  | 0.0139 |  | 0x2fb3713487c7812e7309935b034f40228841666f6b048faf31fd2110ae674f20 |
| eth_PT-wstUSR-27MAR2025_usdc | 13 | -0.0675 | **-0.1222** |  | 0.0155 |  | 0x9940da579c167e13a14f07ba4a38e54cb8fa2abb35a3976ec1af07f77e972268 |
## Summary Across All Markets

| Metric | Value |
|--------|-------|
| Number of markets processed | 55 |
| Total spikes detected | 9007 |
| Total unique users across all markets | 13052 |
| Total events across all markets | 689027 |

## Per-Market Analysis

## eth_usr_usdc

- **Max total supply (USD)**: 133,737,726.89
- **Total events**: 24,794
- **Number of users**: 1,962
- **Number of spikes**: 384

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 893.0 | -0.0685 |
| MarketRepay | 129.0 | -0.0123 |
| MarketBorrow | 153.0 | -0.0073 |
| MarketWithdraw | 267.0 | 0.0163 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 368 |
| MarketSupply,MarketWithdraw | 11 |
| MarketBorrow | 5 |


---

## eth_wsteth_usdc

- **Max total supply (USD)**: 181,657,023.47
- **Total events**: 47,881
- **Number of users**: 1,081
- **Number of spikes**: 61

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 284.0 | -0.0461 |
| MarketRepay | 49.0 | -0.0386 |
| MarketLiquidation | 1.0 | -0.0029 |
| MarketBorrow | 55.0 | 0.0048 |
| MarketWithdraw | 90.0 | 0.0164 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 42 |
| MarketBorrow,MarketSupplyCollateral | 10 |
| MarketBorrow | 6 |
| MarketSupply,MarketWithdraw | 2 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_wbtc_usdc

- **Max total supply (USD)**: 277,575,216.81
- **Total events**: 46,009
- **Number of users**: 1,032
- **Number of spikes**: 80

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketBorrow | 19.0 | -0.0512 |
| MarketSupply | 132.0 | -0.0494 |
| MarketRepay | 21.0 | -0.0224 |
| MarketWithdraw | 25.0 | 0.0136 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 58 |
| MarketBorrow,MarketSupplyCollateral | 11 |
| MarketSupply,MarketWithdraw | 7 |
| MarketBorrow | 3 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## base_wbtc_usdc

- **Max total supply (USD)**: 269,255,896.54
- **Total events**: 33,524
- **Number of users**: 917
- **Number of spikes**: 358

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 1382.0 | -0.0536 |
| MarketRepay | 251.0 | -0.0235 |
| MarketBorrow | 487.0 | 0.0039 |
| MarketWithdraw | 821.0 | 0.0119 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 270 |
| MarketSupply,MarketWithdraw | 60 |
| MarketBorrow,MarketSupplyCollateral | 18 |
| MarketBorrow | 6 |
| MarketBorrow,MarketSupply | 2 |


---

## eth_rlp_usdc

- **Max total supply (USD)**: 154,288,632.54
- **Total events**: 56,485
- **Number of users**: 679
- **Number of spikes**: 767

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 132.0 | -0.0556 |
| MarketSupply | 1846.0 | -0.0533 |
| MarketWithdraw | 942.0 | 0.0059 |
| MarketBorrow | 81.0 | 0.0085 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 709 |
| MarketBorrow,MarketSupplyCollateral | 22 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 12 |
| MarketBorrow | 10 |
| MarketSupply,MarketWithdraw | 8 |


---

## eth_cbbtc_usdc

- **Max total supply (USD)**: 607,128,500.34
- **Total events**: 60,270
- **Number of users**: 642
- **Number of spikes**: 216

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 672.0 | -0.0597 |
| MarketRepay | 40.0 | -0.0336 |
| MarketBorrow | 38.0 | 0.0061 |
| MarketWithdraw | 185.0 | 0.0090 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 177 |
| MarketSupply,MarketWithdraw | 17 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 13 |
| MarketBorrow,MarketSupplyCollateral | 5 |
| MarketBorrow,MarketSupply | 3 |


---

## base_wbtc_usdt

- **Max total supply (USD)**: 541,018,474.87
- **Total events**: 27,809
- **Number of users**: 518
- **Number of spikes**: 268

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 2693.0 | -0.0627 |
| MarketRepay | 354.0 | -0.0271 |
| MarketBorrow | 491.0 | 0.0065 |
| MarketWithdraw | 1375.0 | 0.0115 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 194 |
| MarketSupply,MarketWithdraw | 43 |
| MarketBorrow,MarketSupplyCollateral | 16 |
| MarketBorrow | 11 |
| MarketBorrow,MarketSupply | 2 |


---

## eth_wbtc_usdt

- **Max total supply (USD)**: 529,825,941.69
- **Total events**: 27,694
- **Number of users**: 517
- **Number of spikes**: 298

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 2816.0 | -0.0684 |
| MarketRepay | 369.0 | -0.0289 |
| MarketBorrow | 515.0 | 0.0068 |
| MarketWithdraw | 1547.0 | 0.0125 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 211 |
| MarketSupply,MarketWithdraw | 52 |
| MarketBorrow,MarketSupplyCollateral | 17 |
| MarketBorrow | 14 |
| MarketBorrow,MarketSupply | 2 |


---

## eth_usd0++_usdc

- **Max total supply (USD)**: 309,982,120.95
- **Total events**: 25,034
- **Number of users**: 416
- **Number of spikes**: 106

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 622.0 | -0.0448 |
| MarketRepay | 163.0 | -0.0144 |
| MarketBorrow | 120.0 | -0.0022 |
| MarketWithdraw | 388.0 | 0.0116 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 96 |
| MarketBorrow,MarketSupplyCollateral | 5 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |
| MarketRepay,MarketWithdraw,MarketWithdrawCollateral | 1 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral,MarketWithdraw | 1 |


---

## eth_wsteth_usdt

- **Max total supply (USD)**: 339,293,759.74
- **Total events**: 13,064
- **Number of users**: 304
- **Number of spikes**: 297

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 872.0 | -0.0805 |
| MarketRepay | 65.0 | -0.0555 |
| MarketBorrow | 57.0 | -0.0540 |
| MarketWithdraw | 372.0 | 0.0089 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 235 |
| MarketSupply,MarketWithdraw | 44 |
| MarketBorrow,MarketSupplyCollateral | 6 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 6 |
| MarketBorrow | 5 |


---

## eth_usde_dai

- **Max total supply (USD)**: 154,685,204.51
- **Total events**: 4,351
- **Number of users**: 285
- **Number of spikes**: 12

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketLiquidation | 1.0 | -0.0469 |
| MarketRepay | 116.0 | -0.0109 |
| MarketSupply | 1.0 | -0.0036 |
| MarketBorrow | 69.0 | 0.0067 |
| MarketWithdraw | 5.0 | 0.0088 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 5 |
| MarketWithdraw | 4 |
| MarketBorrow | 3 |


---

## eth_mhyper_usdc

- **Max total supply (USD)**: 142,136,439.88
- **Total events**: 10,787
- **Number of users**: 276
- **Number of spikes**: 142

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 372.0 | -0.0720 |
| MarketRepay | 104.0 | -0.0140 |
| MarketWithdraw | 301.0 | 0.0131 |
| MarketBorrow | 20.0 | 0.0146 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 113 |
| MarketBorrow | 19 |
| MarketBorrow,MarketSupplyCollateral | 8 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |


---

## eth_syrupusdc_usdc

- **Max total supply (USD)**: 93,767,984.11
- **Total events**: 34,386
- **Number of users**: 256
- **Number of spikes**: 681

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 26.0 | -0.1173 |
| MarketSupply | 1292.0 | -0.0800 |
| MarketBorrow | 18.0 | 0.0077 |
| MarketWithdraw | 378.0 | 0.0147 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 634 |
| MarketSupply,MarketWithdraw | 25 |
| MarketBorrow,MarketSupplyCollateral | 14 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 6 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_wstusr_usdc

- **Max total supply (USD)**: 43,945,273.28
- **Total events**: 13,478
- **Number of users**: 239
- **Number of spikes**: 869

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 26.0 | -0.1528 |
| MarketSupply | 1193.0 | -0.0944 |
| MarketWithdraw | 217.0 | -0.0161 |
| MarketBorrow | 35.0 | -0.0066 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 760 |
| MarketSupply,MarketWithdraw | 52 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 26 |
| MarketBorrow,MarketSupplyCollateral | 19 |
| MarketBorrow,MarketSupply | 8 |


---

## eth_slvlusd_usdc

- **Max total supply (USD)**: 67,373,880.68
- **Total events**: 12,226
- **Number of users**: 144
- **Number of spikes**: 198

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 288.0 | -0.0957 |
| MarketRepay | 9.0 | -0.0261 |
| MarketBorrow | 2.0 | 0.0001 |
| MarketWithdraw | 71.0 | 0.0145 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 160 |
| MarketSupply,MarketWithdraw | 19 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 10 |
| MarketBorrow,MarketSupplyCollateral | 5 |
| MarketBorrow | 2 |


---

## eth_csusdl_usdc

- **Max total supply (USD)**: 68,016,629.78
- **Total events**: 10,477
- **Number of users**: 119
- **Number of spikes**: 247

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 362.0 | -0.0869 |
| MarketBorrow | 11.0 | -0.0042 |
| MarketRepay | 12.0 | -0.0005 |
| MarketWithdraw | 136.0 | 0.0149 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 223 |
| MarketSupply,MarketWithdraw | 17 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 4 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_weth_usdt

- **Max total supply (USD)**: 614,128.00
- **Total events**: 2,100
- **Number of users**: 114
- **Number of spikes**: 79

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 149.0 | -1.1401 |
| MarketRepay | 170.0 | -0.1874 |
| MarketBorrow | 225.0 | -0.0083 |
| MarketWithdraw | 36.0 | 0.0154 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 60 |
| MarketBorrow,MarketSupplyCollateral | 11 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 4 |
| MarketBorrow,MarketSupply | 2 |
| MarketBorrow,MarketRepay,MarketSupplyCollateral | 1 |


---

## eth_mF-ONE_usdc

- **Max total supply (USD)**: 94,397,196.16
- **Total events**: 17,168
- **Number of users**: 102
- **Number of spikes**: 235

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 27.0 | -0.1351 |
| MarketSupply | 565.0 | -0.1183 |
| MarketWithdraw | 414.0 | 0.0104 |
| MarketBorrow | 5.0 | 0.0228 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 187 |
| MarketSupply,MarketWithdraw | 16 |
| MarketBorrow | 14 |
| MarketBorrow,MarketSupplyCollateral | 8 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 7 |


---

## eth_fxsave_usdc

- **Max total supply (USD)**: 39,034,562.39
- **Total events**: 11,285
- **Number of users**: 99
- **Number of spikes**: 370

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 24.0 | -0.2391 |
| MarketSupply | 732.0 | -0.0765 |
| MarketWithdraw | 286.0 | 0.0105 |
| MarketBorrow | 12.0 | 0.0163 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 320 |
| MarketBorrow,MarketSupplyCollateral | 19 |
| MarketBorrow | 15 |
| MarketSupply,MarketWithdraw | 7 |
| MarketBorrow,MarketSupply | 5 |


---

## eth_reusd_usdc

- **Max total supply (USD)**: 13,221,619.01
- **Total events**: 7,598
- **Number of users**: 97
- **Number of spikes**: 187

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 387.0 | -0.1229 |
| MarketBorrow | 3.0 | 0.0053 |
| MarketWithdraw | 253.0 | 0.0117 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 180 |
| MarketBorrow | 4 |
| MarketBorrow,MarketSupplyCollateral | 3 |


---

## eth_siusd_usdc

- **Max total supply (USD)**: 95,936,123.41
- **Total events**: 21,062
- **Number of users**: 93
- **Number of spikes**: 122

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 326.0 | -0.0533 |
| MarketRepay | 49.0 | -0.0330 |
| MarketWithdraw | 210.0 | 0.0131 |
| MarketBorrow | 20.0 | 0.0142 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 94 |
| MarketSupply,MarketWithdraw | 17 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 8 |
| MarketBorrow,MarketSupplyCollateral | 3 |


---

## eth_stcusd_usdc

- **Max total supply (USD)**: 75,119,129.83
- **Total events**: 14,693
- **Number of users**: 87
- **Number of spikes**: 305

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 24.0 | -0.0691 |
| MarketSupply | 710.0 | -0.0514 |
| MarketWithdraw | 347.0 | 0.0128 |
| MarketBorrow | 7.0 | 0.0189 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 254 |
| MarketSupply,MarketWithdraw | 36 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 10 |
| MarketBorrow,MarketSupplyCollateral | 4 |
| MarketBorrow | 1 |


---

## eth_sdeusd_usdc

- **Max total supply (USD)**: 103,506,497.03
- **Total events**: 18,181
- **Number of users**: 61
- **Number of spikes**: 414

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 673.0 | -0.0851 |
| MarketRepay | 11.0 | -0.0366 |
| MarketLiquidation | 2.0 | 0.0021 |
| MarketBorrow | 7.0 | 0.0025 |
| MarketWithdraw | 197.0 | 0.0139 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 394 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 7 |
| MarketSupply,MarketWithdraw | 6 |
| MarketBorrow,MarketSupplyCollateral | 4 |
| MarketBorrow | 3 |


---

## eth_susde_pyusd

- **Max total supply (USD)**: 180,022,683.64
- **Total events**: 1,092
- **Number of users**: 56
- **Number of spikes**: 17

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 7.0 | -0.1147 |
| MarketSupply | 20.0 | -0.0489 |
| MarketBorrow | 11.0 | 0.0024 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 8 |
| MarketWithdraw | 5 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_wsrusd_usdc

- **Max total supply (USD)**: 100,015,387.35
- **Total events**: 9,163
- **Number of users**: 44
- **Number of spikes**: 49

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 55.0 | -0.0412 |
| MarketRepay | 136.0 | -0.0203 |
| MarketBorrow | 42.0 | 0.0098 |
| MarketWithdraw | 19.0 | 0.0144 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 39 |
| MarketBorrow,MarketSupplyCollateral | 10 |


---

## eth_cbbtc_usdt

- **Max total supply (USD)**: 372,254,049.87
- **Total events**: 956
- **Number of users**: 43
- **Number of spikes**: 15

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 32.0 | -0.1909 |
| MarketRepay | 2.0 | -0.0285 |
| MarketWithdraw | 11.0 | 0.0158 |
| MarketBorrow | 3.0 | 0.0241 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 13 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |
| MarketSupply,MarketWithdraw | 1 |


---

## eth_mapollo_usdc

- **Max total supply (USD)**: 5,370,054.71
- **Total events**: 578
- **Number of users**: 31
- **Number of spikes**: 17

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 29.0 | -0.1376 |
| MarketRepay | 10.0 | -0.0669 |
| MarketWithdraw | 54.0 | 0.0072 |
| MarketBorrow | 8.0 | 0.0217 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 9 |
| MarketBorrow,MarketSupplyCollateral | 6 |
| MarketBorrow | 2 |


---

## eth_syrupusdc_pyusd

- **Max total supply (USD)**: 30,014,681.10
- **Total events**: 402
- **Number of users**: 26
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

- **Max total supply (USD)**: 54,243,591.24
- **Total events**: 18,971
- **Number of users**: 361
- **Number of spikes**: 32

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 22.0 | -0.0331 |
| MarketSupply | 171.0 | -0.0323 |
| MarketBorrow | 79.0 | 0.0040 |
| MarketWithdraw | 44.0 | 0.0140 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 22 |
| MarketBorrow | 6 |
| MarketBorrow,MarketSupplyCollateral | 4 |


---

## eth_PT-USDe-25SEP2025_usdc

- **Max total supply (USD)**: 418,822,963.58
- **Total events**: 17,897
- **Number of users**: 290
- **Number of spikes**: 75

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 45.0 | -0.0481 |
| MarketSupply | 247.0 | -0.0456 |
| MarketBorrow | 21.0 | 0.0037 |
| MarketWithdraw | 106.0 | 0.0088 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 44 |
| MarketBorrow,MarketSupplyCollateral | 17 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 9 |
| MarketSupply,MarketWithdraw | 2 |
| MarketBorrow | 2 |


---

## PT-reUSD-25JUN2026_usdc

- **Max total supply (USD)**: 54,243,591.24
- **Total events**: 13,237
- **Number of users**: 249
- **Number of spikes**: 29

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 20.0 | -0.0352 |
| MarketSupply | 164.0 | -0.0322 |
| MarketBorrow | 77.0 | 0.0041 |
| MarketWithdraw | 41.0 | 0.0142 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 19 |
| MarketBorrow | 6 |
| MarketBorrow,MarketSupplyCollateral | 4 |


---

## eth_PT-stcUSD-29JAN2026_usdc

- **Max total supply (USD)**: 60,017,452.09
- **Total events**: 10,954
- **Number of users**: 175
- **Number of spikes**: 203

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 91.0 | -0.0740 |
| MarketSupply | 447.0 | -0.0617 |
| MarketWithdraw | 280.0 | 0.0131 |
| MarketBorrow | 9.0 | 0.0156 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 184 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 10 |
| MarketSupply,MarketWithdraw | 7 |
| MarketBorrow,MarketSupplyCollateral | 1 |
| MarketBorrow | 1 |


---

## eth_PT-USDe-27MAR2025_dai

- **Max total supply (USD)**: 126,211,463.34
- **Total events**: 3,089
- **Number of users**: 156
- **Number of spikes**: 18

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 47.0 | -0.0704 |
| MarketRepay | 60.0 | -0.0274 |
| MarketWithdraw | 13.0 | 0.0069 |
| MarketBorrow | 40.0 | 0.0073 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 10 |
| MarketBorrow,MarketSupplyCollateral | 5 |
| MarketBorrow | 3 |


---

## eth_PT-USDe-25SEP2025_usdt

- **Max total supply (USD)**: 58,360,881.73
- **Total events**: 5,301
- **Number of users**: 143
- **Number of spikes**: 61

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 210.0 | -0.0721 |
| MarketRepay | 71.0 | -0.0524 |
| MarketWithdraw | 66.0 | 0.0098 |
| MarketBorrow | 20.0 | 0.0165 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 34 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 12 |
| MarketBorrow,MarketSupplyCollateral | 12 |
| MarketSupply,MarketWithdraw | 2 |
| MarketBorrow | 1 |


---

## eth_PT-USDe-25SEP2025_dai

- **Max total supply (USD)**: 504,042,081.14
- **Total events**: 3,959
- **Number of users**: 140
- **Number of spikes**: 0

*No spikes detected or insufficient data for action analysis.*

---

## eth_PT-csUSDL-31JUL2025_usdc

- **Max total supply (USD)**: 31,582,576.18
- **Total events**: 6,549
- **Number of users**: 123
- **Number of spikes**: 138

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 225.0 | -0.1263 |
| MarketRepay | 6.0 | -0.0748 |
| MarketBorrow | 14.0 | 0.0053 |
| MarketWithdraw | 89.0 | 0.0130 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 82 |
| MarketSupply,MarketWithdraw | 37 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 15 |
| MarketBorrow,MarketSupply | 2 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_PT-sNUSD-5MAR2026_usdc

- **Max total supply (USD)**: 11,460,920.52
- **Total events**: 3,474
- **Number of users**: 120
- **Number of spikes**: 37

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 73.0 | -0.0529 |
| MarketRepay | 7.0 | -0.0149 |
| MarketBorrow | 18.0 | 0.0027 |
| MarketWithdraw | 19.0 | 0.0158 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 24 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 10 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_PT-USDe-31JUL2025_dai

- **Max total supply (USD)**: 10,439,187.23
- **Total events**: 2,073
- **Number of users**: 113
- **Number of spikes**: 22

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 41.0 | -0.1508 |
| MarketSupply | 24.0 | -0.0499 |
| MarketWithdraw | 8.0 | 0.0160 |
| MarketBorrow | 8.0 | 0.0211 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow | 9 |
| MarketBorrow,MarketSupplyCollateral | 8 |
| MarketWithdraw | 5 |


---

## eth_PT-mHYPER-20NOV2025_usdc

- **Max total supply (USD)**: 38,891,074.29
- **Total events**: 3,348
- **Number of users**: 110
- **Number of spikes**: 67

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 53.0 | -0.2275 |
| MarketSupply | 207.0 | -0.0530 |
| MarketWithdraw | 252.0 | 0.0112 |
| MarketBorrow | 5.0 | 0.0207 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 35 |
| MarketBorrow,MarketSupplyCollateral | 13 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 10 |
| MarketBorrow | 9 |


---

## eth_PT-lvlUSD-29MAY2025_usdc

- **Max total supply (USD)**: 31,143,600.86
- **Total events**: 4,960
- **Number of users**: 107
- **Number of spikes**: 91

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketBorrow | 18.0 | -0.4739 |
| MarketSupply | 151.0 | -0.2304 |
| MarketRepay | 15.0 | -0.0657 |
| MarketWithdraw | 106.0 | 0.0148 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 70 |
| MarketSupply,MarketWithdraw | 14 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketBorrow | 1 |


---

## eth_PT-slvlUSD-25SEP2025_usdc

- **Max total supply (USD)**: 18,824,491.59
- **Total events**: 7,659
- **Number of users**: 97
- **Number of spikes**: 133

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketBorrow | 6.0 | -0.1457 |
| MarketRepay | 3.0 | -0.0769 |
| MarketSupply | 205.0 | -0.0556 |
| MarketLiquidation | 1.0 | -0.0168 |
| MarketWithdraw | 81.0 | 0.0144 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 113 |
| MarketSupply,MarketWithdraw | 15 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 5 |


---

## eth_PT-USD0++-27MAR2025_usdc

- **Max total supply (USD)**: 29,862,840.94
- **Total events**: 2,529
- **Number of users**: 86
- **Number of spikes**: 96

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 29.0 | -0.1477 |
| MarketSupply | 133.0 | -0.1165 |
| MarketBorrow | 24.0 | -0.0136 |
| MarketWithdraw | 59.0 | 0.0183 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 91 |
| MarketBorrow,MarketSupply | 3 |
| MarketBorrow,MarketSupplyCollateral | 1 |
| MarketBorrow | 1 |


---

## eth_PT-RLP-4SEP2025_usdc

- **Max total supply (USD)**: 16,632,337.06
- **Total events**: 4,054
- **Number of users**: 82
- **Number of spikes**: 167

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 257.0 | -0.0902 |
| MarketBorrow | 11.0 | -0.0719 |
| MarketRepay | 21.0 | -0.0414 |
| MarketWithdraw | 78.0 | 0.0125 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 155 |
| MarketBorrow,MarketSupplyCollateral | 6 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |
| MarketRepay,MarketWithdraw,MarketWithdrawCollateral | 2 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_PT-wstUSR-25SEP2025_usdc

- **Max total supply (USD)**: 17,812,907.25
- **Total events**: 4,257
- **Number of users**: 76
- **Number of spikes**: 170

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 12.0 | -0.7872 |
| MarketSupply | 194.0 | -0.0918 |
| MarketBorrow | 7.0 | -0.0322 |
| MarketWithdraw | 30.0 | 0.0137 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 145 |
| MarketBorrow,MarketSupplyCollateral | 11 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 10 |
| MarketBorrow | 4 |


---

## eth_PT-reUSD-18DEC2025_usdc

- **Max total supply (USD)**: 11,432,448.43
- **Total events**: 1,207
- **Number of users**: 69
- **Number of spikes**: 24

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 34.0 | -0.1020 |
| MarketRepay | 18.0 | -0.0987 |
| MarketBorrow | 1.0 | 0.0000 |
| MarketWithdraw | 29.0 | 0.0158 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 16 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 4 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketBorrow,MarketSupply | 1 |
| MarketBorrow | 1 |


---

## eth_PT-slvlUSD-29MAY2025_usdc

- **Max total supply (USD)**: 21,369,077.19
- **Total events**: 2,836
- **Number of users**: 62
- **Number of spikes**: 69

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketBorrow | 2.0 | -0.0995 |
| MarketSupply | 202.0 | -0.0571 |
| MarketRepay | 9.0 | -0.0031 |
| MarketWithdraw | 123.0 | 0.0111 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 53 |
| MarketBorrow,MarketSupplyCollateral | 15 |
| MarketBorrow | 1 |


---

## eth_PT-wstUSR-27MAR2025_usr

- **Max total supply (USD)**: 15,856,215.65
- **Total events**: 902
- **Number of users**: 55
- **Number of spikes**: 38

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 52.0 | -0.2622 |
| MarketRepay | 34.0 | -0.1094 |
| MarketBorrow | 23.0 | -0.0156 |
| MarketWithdraw | 10.0 | 0.0082 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 25 |
| MarketBorrow,MarketSupplyCollateral | 7 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 4 |
| MarketBorrow | 2 |


---

## eth_PT-syrupUSDC-28AUG2025_usdc

- **Max total supply (USD)**: 11,775,168.69
- **Total events**: 1,734
- **Number of users**: 41
- **Number of spikes**: 63

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 1.0 | -0.1224 |
| MarketSupply | 129.0 | -0.0799 |
| MarketBorrow | 1.0 | 0.0000 |
| MarketWithdraw | 64.0 | 0.0167 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 62 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_PT-USDe-27NOV2025_usds

- **Max total supply (USD)**: 265,788,041.17
- **Total events**: 1,062
- **Number of users**: 35
- **Number of spikes**: 27

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 28.0 | -0.1157 |
| MarketRepay | 13.0 | -0.0025 |
| MarketWithdraw | 2.0 | 0.0081 |
| MarketBorrow | 25.0 | 0.0176 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 21 |
| MarketBorrow | 4 |
| MarketWithdraw | 2 |


---

## eth_PT-syrupUSDC-30OCT2025_usdc

- **Max total supply (USD)**: 41,739,570.56
- **Total events**: 4,667
- **Number of users**: 27
- **Number of spikes**: 130

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 205.0 | -0.0694 |
| MarketRepay | 1.0 | -0.0001 |
| MarketBorrow | 1.0 | 0.0045 |
| MarketWithdraw | 53.0 | 0.0148 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 111 |
| MarketSupply,MarketWithdraw | 8 |
| MarketBorrow,MarketSupply | 6 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 4 |
| MarketBorrow | 1 |


---

## eth_PT-USR-29MAY2025_usdc

- **Max total supply (USD)**: 17,663,436.43
- **Total events**: 1,666
- **Number of users**: 25
- **Number of spikes**: 62

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 85.0 | -0.0768 |
| MarketRepay | 9.0 | -0.0235 |
| MarketWithdraw | 12.0 | 0.0104 |
| MarketBorrow | 19.0 | 0.0201 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 45 |
| MarketBorrow,MarketSupplyCollateral | 7 |
| MarketBorrow | 5 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 4 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_PT-sdeUSD-1753142406_usdc

- **Max total supply (USD)**: 13,003,702.42
- **Total events**: 4,030
- **Number of users**: 23
- **Number of spikes**: 57

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 106.0 | -0.1325 |
| MarketWithdraw | 47.0 | 0.0116 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 56 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## PT-siUSD-26MAR2026_usdc

- **Max total supply (USD)**: 2,258,353.08
- **Total events**: 2,135
- **Number of users**: 18
- **Number of spikes**: 124

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 160.0 | -0.0714 |
| MarketBorrow | 5.0 | -0.0118 |
| MarketRepay | 1.0 | -0.0000 |
| MarketWithdraw | 29.0 | 0.0108 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 114 |
| MarketSupply,MarketWithdraw | 8 |
| MarketBorrow,MarketSupplyCollateral | 1 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_PT-stcUSD-23JUL2026_usdc

- **Max total supply (USD)**: 26,840,950.18
- **Total events**: 3,809
- **Number of users**: 15
- **Number of spikes**: 262

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 460.0 | -0.0633 |
| MarketWithdraw | 73.0 | 0.0139 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 254 |
| MarketSupply,MarketWithdraw | 7 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_PT-wstUSR-27MAR2025_usdc

- **Max total supply (USD)**: 9,229,125.60
- **Total events**: 121
- **Number of users**: 14
- **Number of spikes**: 13

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 4.0 | -0.1222 |
| MarketSupply | 4.0 | -0.0675 |
| MarketWithdraw | 3.0 | 0.0155 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 9 |
| MarketBorrow,MarketSupplyCollateral | 4 |


---

