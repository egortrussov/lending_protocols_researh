# Market Spike Analysis Report

## Combined Analysis Across All Markets

### Action Impact (weighted by volume) – All Markets

| Action Type | Count | Weighted Mean ΔUtil |
|-------------|-------|---------------------|
| MarketBorrow | 1686.0 | 0.0013 |
| MarketLiquidation | 26.0 | -0.0121 |
| MarketRepay | 2178.0 | -0.0646 |
| MarketSupply | 18737.0 | -0.0647 |
| MarketWithdraw | 8165.0 | 0.0111 |

### Weighted Mean ΔUtil by Market and Action Type

| Market | N Spikes | MarketSupply | MarketRepay | MarketBorrow | MarketWithdraw | MarketLiquidation| Address |
|---|---|---|---|---|---|---|---|
| eth_usr_usdc | 374 | **-0.0690** | -0.0123 | -0.0078 | 0.0165 |  | 0x8e7cc042d739a365c43d0a52d5f24160fa7ae9b7e7c9a479bd02a56041d4cf77 |
| eth_wsteth_usdc | 579 | **-0.0480** | -0.0263 | 0.0041 | 0.0125 | -0.0070 | 0xb323495f7e4148be5643a4ea4a8221eef163e4bccfdedc2a6f4696baacbc86cc |
| eth_wbtc_usdc | 78 | **-0.0507** | -0.0229 | -0.0001 | 0.0136 |  | 0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49 |
| base_wbtc_usdc | 356 | **-0.0520** | -0.0235 | 0.0036 | 0.0120 |  | 0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49 |
| base_wbtc_usdt | 19 | -0.0605 | **-0.0815** | 0.0086 | 0.0148 |  | 0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99 |
| eth_wbtc_usdt | 19 | -0.0605 | **-0.0815** | 0.0086 | 0.0148 |  | 0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99 |
| eth_rlp_usdc | 730 | -0.0540 | **-0.0558** | 0.0121 | 0.0058 |  | 0xe1b65304edd8ceaea9b629df4c3c926a37d1216e27900505c04f14b2ed279f33 |
| eth_cbbtc_usdc | 217 | **-0.0600** | -0.0336 | 0.0136 | 0.0090 |  | 0x64d65c9a2d91c36d56fbc42d69e979335320169b3df63bf92789e2c8883fcc64 |
| eth_wsteth_usdt | 226 | -0.0551 | **-0.0719** | 0.0040 | 0.0118 | 0.0000 | 0xe7e9694b754c4d4f7e21faf7223f6fa71abaeb10296a4c43a54a7977149687d2 |
| eth_usd0++_usdc | 323 | **-0.0689** | -0.0161 | -0.0023 | 0.0125 |  | 0x1eda1b67414336cab3914316cb58339ddaef9e43f939af1fed162a989c98bc20 |
| eth_PT-reUSD-25JUN2026_usdc | 28 | -0.0329 | **-0.0332** | 0.0041 | 0.0129 |  | 0x9bc98c2f20ac58287ef2c860eea53a2fdc27c17a7817ff1206c0b7840cc7cd79 |
| eth_PT-USDe-25SEP2025_usdc | 73 | -0.0456 | **-0.0481** | 0.0037 | 0.0088 |  | 0x7a5d67805cb78fad2596899e0c83719ba89df353b931582eb7d3041fd5a06dc8 |
| eth_usde_dai | 15 | -0.0439 | **-0.0487** | 0.0067 | 0.0082 | -0.0251 | 0xc581c5f70bd1afa283eed57d1418c6432cbff1d862f94eaf58fdd4e46afbb67f |
| eth_mhyper_usdc | 140 | **-0.0625** | -0.0140 | 0.0145 | 0.0131 |  | 0x95c28d447950ca6c8bbfd25fc05b80b1fd7a1cdd17a3610b4b3f1ffc8dc2e2ed |
| eth_syrupusdc_usdc | 670 | -0.0747 | **-0.1339** | -0.0208 | 0.0147 |  | 0x729badf297ee9f2f6b3f717b96fd355fc6ec00422284ce1968e76647b258cf44 |
| PT-reUSD-25JUN2026_usdc | 25 | -0.0329 | **-0.0352** | 0.0042 | 0.0131 |  | 0x9bc98c2f20ac58287ef2c860eea53a2fdc27c17a7817ff1206c0b7840cc7cd79 |
| eth_wstusr_usdc | 849 | -0.1131 | **-0.1741** | -0.0110 | -0.0254 |  | 0xd9e34b1eed46d123ac1b69b224de1881dbc88798bc7b70f504920f62f58f28cc |
| eth_PT-stcUSD-29JAN2026_usdc | 196 | -0.0616 | **-0.0740** | 0.0156 | 0.0130 |  | 0x03f715ef1ae508ab3e1faf4dffdbf2a077d1f0ad10c5aad42cf4438d5e3328af |
| eth_PT-USDe-27MAR2025_dai | 17 | **-0.0714** | -0.0274 | 0.0073 | 0.0069 |  | 0xab0dcab71e65c05b7f241ea79a33452c87e62db387129e4abe15e458d433e4d8 |
| eth_slvlusd_usdc | 194 | **-0.0955** | -0.0261 | 0.0001 | 0.0145 |  | 0x8b1bc4d682b04a16309a8adf77b35de0c42063a7944016cfc37a79ccac0007b6 |
| eth_weth_usdt | 16 | -0.0104 | **-0.2241** | 0.0001 | 0.0170 |  | 0xdbffac82c2dc7e8aa781bd05746530b0068d80929f23ac1628580e27810bc0c5 |
| eth_PT-USDe-25SEP2025_usdt | 61 | **-0.0721** | -0.0524 | 0.0165 | 0.0098 |  | 0xb0a9ac81a8c6a5274aa1a8337aed35a2cb2cd4feb5c6d3b39d41f234fbf2955b |
| eth_PT-USDe-25SEP2025_dai | 0 |  |  |  |  |  | 0x45d97c66db5e803b9446802702f087d4293a2f74b370105dc3a88a278bf6bb21 |
| eth_PT-csUSDL-31JUL2025_usdc | 129 | **-0.1287** | -0.0748 | 0.0053 | 0.0127 |  | 0x544b0a093b130a3fb01b72a1279ab848575f049c73da3b5c9c718f9350a1519c |
| eth_PT-sNUSD-5MAR2026_usdc | 35 | **-0.0533** | -0.0151 | 0.0027 | 0.0158 |  | 0x2a9a5c436719badcfadbad3ad8e8179a160ded758603eaa03a883f922a1790d3 |
| eth_csusdl_usdc | 246 | **-0.1397** |  | 0.0000 | 0.0185 |  | 0x83b7ad16905809ea36482f4fbf6cfee9c9f316d128de9a5da1952607d5e4df5e |
| eth_PT-USDe-31JUL2025_dai | 22 | -0.0499 | **-0.1508** | 0.0211 | 0.0160 |  | 0x760b14c9003f08ac4bf0cfb02596ee4d6f0548a4fde5826bfd56befb9ed62ae9 |
| eth_PT-mHYPER-20NOV2025_usdc | 67 | -0.0530 | **-0.2275** | 0.0207 | 0.0112 |  | 0x1ca75949a91c157183f53282d73c37191e7cd84002310f6632047d874aad4a0f |
| eth_PT-lvlUSD-29MAY2025_usdc | 79 | -0.2471 | -0.0657 | **-0.4739** | 0.0136 |  | 0x185df29d35001b5657c9c964284ddbeee83a40c83e6c6e89432463e2157e075c |
| eth_mF-ONE_usdc | 234 | -0.1185 | **-0.1351** | 0.0228 | 0.0104 |  | 0xef2c308b5abecf5c8750a1aa82b47c558005feb7a03f4f8e1ad682d71ac8d0ba |
| eth_fxsave_usdc | 362 | -0.0745 | **-0.2391** | 0.0163 | 0.0105 |  | 0x43e925e52d7873fa8acac90dd5f246087d55b3a34c344b71884a6352491ff459 |
| eth_PT-slvlUSD-25SEP2025_usdc | 125 | -0.0550 | -0.0769 | **-0.1457** | 0.0121 | -0.0168 | 0x4005ba6eb7d2221fe58102bd320aa6d83c47b212771bc950ab71c5074d9ab0ec |
| eth_reusd_usdc | 181 | **-0.1137** |  | 0.0022 | 0.0117 |  | 0x4565ac05d38b19374ccbb04c17cca60ca9353cd41824f0803d0fc7704f60eaed |
| eth_cbbtc_usdt | 136 | **-0.0991** | -0.0490 | 0.0084 | 0.0146 |  | 0x45671fb8d5dea1c4fbca0b8548ad742f6643300eeb8dbd34ad64a658b2b05bca |
| eth_siusd_usdc | 111 | **-0.0538** | -0.0338 | 0.0142 | 0.0125 |  | 0xbbf7ce1b40d32d3e3048f5cf27eeaa6de8cb27b80194690aab191a63381d8c99 |
| eth_stcusd_usdc | 298 | -0.0516 | **-0.0691** | 0.0189 | 0.0127 |  | 0xeb17955ea422baeddbfb0b8d8c9086c5be7a9cfdefb292119a102e981a30062e |
| eth_PT-USD0++-27MAR2025_usdc | 96 | -0.1165 | **-0.1477** | -0.0136 | 0.0183 |  | 0x147977320f168afc651b7e5a1849cc1b1e64e329e1bf0212fa49dcb2856074a4 |
| eth_PT-RLP-4SEP2025_usdc | 165 | **-0.0905** | -0.0414 | -0.0719 | 0.0125 |  | 0xcc611d3ca8ce8dcc63e4e8c3cd17c9acb2ca1768eeb143b71e2dc8e6a98c3f65 |
| eth_PT-wstUSR-25SEP2025_usdc | 167 | -0.0922 | **-0.7872** | -0.0322 | 0.0135 |  | 0xeec6c7e2ddb7578f2a7d86fc11cf9da005df34452ad9b9189c51266216f5d71b |
| eth_PT-reUSD-18DEC2025_usdc | 24 | **-0.1020** | -0.0987 | 0.0000 | 0.0158 |  | 0xf5de1cd86d1b96dae889356d9515a1ccfd6caae8570f8d6d49c218bb203d045d |
| eth_PT-slvlUSD-29MAY2025_usdc | 67 | -0.0569 | -0.0031 | **-0.0995** | 0.0111 |  | 0xeb3e4a68c675d88f5a4378eab966e717bdee6a0f38c5ca6da2560ac5d1534f60 |
| eth_sdeusd_usdc | 663 | **-0.1081** | -0.0363 | 0.0000 | 0.0159 | 0.0000 | 0x0f9563442d64ab3bd3bcb27058db0b0d4046a4c46f0acd811dacae9551d2b129 |
| eth_susde_pyusd | 16 | -0.0621 | **-0.1147** | 0.0048 |  |  | 0x90ef0c5a0dc7c4de4ad4585002d44e9d411d212d2f6258e94948beecf8b4c0d5 |
| eth_PT-wstUSR-27MAR2025_usr | 38 | **-0.2622** | -0.1094 | -0.0156 | 0.0082 |  | 0x1e1ae51d4be670307788612599a46a73649ef85e28bab194d3ae00c3cd693ea7 |
| eth_wsrusd_usdc | 49 | **-0.0450** | -0.0240 | 0.0114 | 0.0152 |  | 0x1590cb22d797e226df92ebc6e0153427e207299916e7e4e53461389ad68272fb |
| eth_PT-syrupUSDC-28AUG2025_usdc | 59 | -0.0807 | **-0.1224** | 0.0000 | 0.0174 |  | 0x3bdb58058b41bb700458ba3df317e254244ddec7fc35fec93d2d53475cc6ebdc |
| eth_PT-USDe-27NOV2025_usds | 26 | **-0.0613** | -0.0025 | 0.0241 | 0.0081 |  | 0x8cdb63a27a48ac27fadc0f158a732104bcc4e10bb61c9a5095ea7c127204e26c |
| eth_mapollo_usdc | 15 | **-0.1455** | -0.0681 | 0.0217 | 0.0073 |  | 0x031c7333014af51e4fd18031d14e4eaada58348cde3f6dc6ea8cca16f7387fb2 |
| eth_PT-syrupUSDC-30OCT2025_usdc | 124 | **-0.0703** | -0.0001 |  | 0.0148 |  | 0xb8afc953c3cc8077b4a4bf459bede8d3f80be45ca1f244e4bca13b7b1030eed5 |
| eth_syrupusdc_pyusd | 4 | **-0.0863** | -0.0699 |  | 0.0111 |  | 0xc9629945524f3fde56c7e8854a6c3d48e76b9d97236abbe73c750fcc7aeb8501 |
| eth_PT-USR-29MAY2025_usdc | 61 | **-0.0769** | -0.0235 | 0.0201 | 0.0105 |  | 0x278290bf72ec20495f3f57910bebac7f2f6a6aeff9e9d550f225b4ba26454fe0 |
| eth_PT-sdeUSD-1753142406_usdc | 53 | **-0.1361** |  |  | 0.0117 |  | 0x4ef32e4877329436968f4a29b0c8285531d113dad29b727d88beafe5ed45be6a |
| PT-siUSD-26MAR2026_usdc | 123 | **-0.0715** | -0.0000 | -0.0118 | 0.0107 |  | 0xaac3ffcdf8a75919657e789fa72ab742a7bbfdf5bb0b87e4bbeb3c29bbbbb05c |
| eth_PT-stcUSD-23JUL2026_usdc | 261 | **-0.0634** |  |  | 0.0139 |  | 0x2fb3713487c7812e7309935b034f40228841666f6b048faf31fd2110ae674f20 |
| eth_PT-wstUSR-27MAR2025_usdc | 13 | -0.0675 | **-0.1222** |  | 0.0155 |  | 0x9940da579c167e13a14f07ba4a38e54cb8fa2abb35a3976ec1af07f77e972268 |
## Summary Across All Markets

| Metric | Value |
|--------|-------|
| Number of markets processed | 55 |
| Total spikes detected | 9254 |
| Total unique users across all markets | 13761 |
| Total events across all markets | 763999 |

## Per-Market Analysis

## eth_usr_usdc

- **Max total supply (USD)**: 133,737,526.06
- **Total events**: 24,794
- **Number of users**: 1,962
- **Number of spikes**: 374

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 857.0 | -0.0690 |
| MarketRepay | 128.0 | -0.0123 |
| MarketBorrow | 138.0 | -0.0078 |
| MarketWithdraw | 256.0 | 0.0165 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 362 |
| MarketSupply,MarketWithdraw | 7 |
| MarketBorrow | 5 |


---

## eth_wsteth_usdc

- **Max total supply (USD)**: 153,161,907.54
- **Total events**: 47,881
- **Number of users**: 1,081
- **Number of spikes**: 579

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 1714.0 | -0.0480 |
| MarketRepay | 179.0 | -0.0263 |
| MarketLiquidation | 20.0 | -0.0070 |
| MarketBorrow | 163.0 | 0.0041 |
| MarketWithdraw | 456.0 | 0.0125 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 487 |
| MarketSupply,MarketWithdraw | 42 |
| MarketBorrow,MarketSupplyCollateral | 23 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 12 |
| MarketBorrow | 11 |


---

## eth_wbtc_usdc

- **Max total supply (USD)**: 277,575,216.81
- **Total events**: 46,009
- **Number of users**: 1,032
- **Number of spikes**: 78

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 134.0 | -0.0507 |
| MarketRepay | 20.0 | -0.0229 |
| MarketBorrow | 16.0 | -0.0001 |
| MarketWithdraw | 25.0 | 0.0136 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 56 |
| MarketBorrow,MarketSupplyCollateral | 11 |
| MarketSupply,MarketWithdraw | 7 |
| MarketBorrow | 3 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## base_wbtc_usdc

- **Max total supply (USD)**: 269,255,896.54
- **Total events**: 33,524
- **Number of users**: 917
- **Number of spikes**: 356

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 1374.0 | -0.0520 |
| MarketRepay | 251.0 | -0.0235 |
| MarketBorrow | 486.0 | 0.0036 |
| MarketWithdraw | 816.0 | 0.0120 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 270 |
| MarketSupply,MarketWithdraw | 60 |
| MarketBorrow,MarketSupplyCollateral | 16 |
| MarketBorrow | 6 |
| MarketBorrow,MarketSupply | 2 |


---

## base_wbtc_usdt

- **Max total supply (USD)**: 543,656,708.13
- **Total events**: 53,794
- **Number of users**: 748
- **Number of spikes**: 19

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 15.0 | -0.0815 |
| MarketSupply | 59.0 | -0.0605 |
| MarketBorrow | 21.0 | 0.0086 |
| MarketWithdraw | 21.0 | 0.0148 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 8 |
| MarketBorrow,MarketSupplyCollateral | 6 |
| MarketBorrow | 5 |


---

## eth_wbtc_usdt

- **Max total supply (USD)**: 543,656,708.13
- **Total events**: 53,792
- **Number of users**: 748
- **Number of spikes**: 19

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 15.0 | -0.0815 |
| MarketSupply | 59.0 | -0.0605 |
| MarketBorrow | 21.0 | 0.0086 |
| MarketWithdraw | 21.0 | 0.0148 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 8 |
| MarketBorrow,MarketSupplyCollateral | 6 |
| MarketBorrow | 5 |


---

## eth_rlp_usdc

- **Max total supply (USD)**: 154,288,628.96
- **Total events**: 56,485
- **Number of users**: 679
- **Number of spikes**: 730

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 130.0 | -0.0558 |
| MarketSupply | 1799.0 | -0.0540 |
| MarketWithdraw | 923.0 | 0.0058 |
| MarketBorrow | 73.0 | 0.0121 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 675 |
| MarketBorrow,MarketSupplyCollateral | 21 |
| MarketBorrow | 10 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 10 |
| MarketSupply,MarketWithdraw | 8 |


---

## eth_cbbtc_usdc

- **Max total supply (USD)**: 607,128,500.34
- **Total events**: 60,270
- **Number of users**: 642
- **Number of spikes**: 217

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 673.0 | -0.0600 |
| MarketRepay | 40.0 | -0.0336 |
| MarketWithdraw | 184.0 | 0.0090 |
| MarketBorrow | 35.0 | 0.0136 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 177 |
| MarketSupply,MarketWithdraw | 16 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 14 |
| MarketBorrow,MarketSupplyCollateral | 5 |
| MarketBorrow,MarketSupply | 4 |


---

## eth_wsteth_usdt

- **Max total supply (USD)**: 340,229,595.17
- **Total events**: 30,308
- **Number of users**: 468
- **Number of spikes**: 226

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 40.0 | -0.0719 |
| MarketSupply | 778.0 | -0.0551 |
| MarketLiquidation | 1.0 | 0.0000 |
| MarketBorrow | 24.0 | 0.0040 |
| MarketWithdraw | 351.0 | 0.0118 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 183 |
| MarketSupply,MarketWithdraw | 31 |
| MarketBorrow | 5 |
| MarketBorrow,MarketSupplyCollateral | 3 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |


---

## eth_usd0++_usdc

- **Max total supply (USD)**: 309,982,120.95
- **Total events**: 25,053
- **Number of users**: 417
- **Number of spikes**: 323

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 1342.0 | -0.0689 |
| MarketRepay | 223.0 | -0.0161 |
| MarketBorrow | 124.0 | -0.0023 |
| MarketWithdraw | 961.0 | 0.0125 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 311 |
| MarketBorrow,MarketSupplyCollateral | 7 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |
| MarketRepay,MarketWithdraw,MarketWithdrawCollateral | 1 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral,MarketWithdraw | 1 |


---

## eth_usde_dai

- **Max total supply (USD)**: 154,681,054.53
- **Total events**: 4,351
- **Number of users**: 285
- **Number of spikes**: 15

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 126.0 | -0.0487 |
| MarketSupply | 6.0 | -0.0439 |
| MarketLiquidation | 2.0 | -0.0251 |
| MarketBorrow | 69.0 | 0.0067 |
| MarketWithdraw | 7.0 | 0.0082 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 6 |
| MarketWithdraw | 6 |
| MarketBorrow | 3 |


---

## eth_mhyper_usdc

- **Max total supply (USD)**: 142,131,528.28
- **Total events**: 10,787
- **Number of users**: 276
- **Number of spikes**: 140

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 293.0 | -0.0625 |
| MarketRepay | 103.0 | -0.0140 |
| MarketWithdraw | 266.0 | 0.0131 |
| MarketBorrow | 13.0 | 0.0145 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 111 |
| MarketBorrow | 19 |
| MarketBorrow,MarketSupplyCollateral | 8 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |


---

## eth_syrupusdc_usdc

- **Max total supply (USD)**: 93,767,984.11
- **Total events**: 34,386
- **Number of users**: 256
- **Number of spikes**: 670

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 9.0 | -0.1339 |
| MarketSupply | 566.0 | -0.0747 |
| MarketBorrow | 3.0 | -0.0208 |
| MarketWithdraw | 172.0 | 0.0147 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 628 |
| MarketSupply,MarketWithdraw | 22 |
| MarketBorrow,MarketSupplyCollateral | 14 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 4 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_wstusr_usdc

- **Max total supply (USD)**: 43,945,273.28
- **Total events**: 13,478
- **Number of users**: 239
- **Number of spikes**: 849

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 23.0 | -0.1741 |
| MarketSupply | 1034.0 | -0.1131 |
| MarketWithdraw | 186.0 | -0.0254 |
| MarketBorrow | 33.0 | -0.0110 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 742 |
| MarketSupply,MarketWithdraw | 51 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 26 |
| MarketBorrow,MarketSupplyCollateral | 19 |
| MarketBorrow,MarketSupply | 8 |


---

## eth_slvlusd_usdc

- **Max total supply (USD)**: 67,373,880.68
- **Total events**: 12,226
- **Number of users**: 144
- **Number of spikes**: 194

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 286.0 | -0.0955 |
| MarketRepay | 9.0 | -0.0261 |
| MarketBorrow | 2.0 | 0.0001 |
| MarketWithdraw | 71.0 | 0.0145 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 157 |
| MarketSupply,MarketWithdraw | 18 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 10 |
| MarketBorrow,MarketSupplyCollateral | 5 |
| MarketBorrow | 2 |


---

## eth_weth_usdt

- **Max total supply (USD)**: 1,061,842.42
- **Total events**: 2,349
- **Number of users**: 144
- **Number of spikes**: 16

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 34.0 | -0.2241 |
| MarketSupply | 40.0 | -0.0104 |
| MarketBorrow | 69.0 | 0.0001 |
| MarketWithdraw | 5.0 | 0.0170 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 10 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |
| MarketBorrow,MarketSupply | 1 |
| MarketBorrow,MarketRepay,MarketSupplyCollateral | 1 |


---

## eth_csusdl_usdc

- **Max total supply (USD)**: 68,016,629.78
- **Total events**: 10,477
- **Number of users**: 119
- **Number of spikes**: 246

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 111.0 | -0.1397 |
| MarketBorrow | 3.0 | 0.0000 |
| MarketWithdraw | 25.0 | 0.0185 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 223 |
| MarketSupply,MarketWithdraw | 16 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 4 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_mF-ONE_usdc

- **Max total supply (USD)**: 94,397,196.16
- **Total events**: 17,168
- **Number of users**: 102
- **Number of spikes**: 234

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 27.0 | -0.1351 |
| MarketSupply | 563.0 | -0.1185 |
| MarketWithdraw | 414.0 | 0.0104 |
| MarketBorrow | 5.0 | 0.0228 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 186 |
| MarketSupply,MarketWithdraw | 16 |
| MarketBorrow | 14 |
| MarketBorrow,MarketSupplyCollateral | 8 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 7 |


---

## eth_fxsave_usdc

- **Max total supply (USD)**: 39,034,562.39
- **Total events**: 11,285
- **Number of users**: 99
- **Number of spikes**: 362

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 24.0 | -0.2391 |
| MarketSupply | 720.0 | -0.0745 |
| MarketWithdraw | 283.0 | 0.0105 |
| MarketBorrow | 12.0 | 0.0163 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 312 |
| MarketBorrow,MarketSupplyCollateral | 19 |
| MarketBorrow | 15 |
| MarketSupply,MarketWithdraw | 7 |
| MarketBorrow,MarketSupply | 5 |


---

## eth_reusd_usdc

- **Max total supply (USD)**: 13,221,619.01
- **Total events**: 7,598
- **Number of users**: 97
- **Number of spikes**: 181

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 379.0 | -0.1137 |
| MarketBorrow | 2.0 | 0.0022 |
| MarketWithdraw | 247.0 | 0.0117 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 174 |
| MarketBorrow | 4 |
| MarketBorrow,MarketSupplyCollateral | 3 |


---

## eth_cbbtc_usdt

- **Max total supply (USD)**: 372,254,049.87
- **Total events**: 6,333
- **Number of users**: 96
- **Number of spikes**: 136

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 311.0 | -0.0991 |
| MarketRepay | 12.0 | -0.0490 |
| MarketBorrow | 10.0 | 0.0084 |
| MarketWithdraw | 111.0 | 0.0146 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 124 |
| MarketSupply,MarketWithdraw | 4 |
| MarketBorrow,MarketSupplyCollateral | 4 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_siusd_usdc

- **Max total supply (USD)**: 95,936,123.41
- **Total events**: 21,062
- **Number of users**: 93
- **Number of spikes**: 111

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 302.0 | -0.0538 |
| MarketRepay | 48.0 | -0.0338 |
| MarketWithdraw | 199.0 | 0.0125 |
| MarketBorrow | 20.0 | 0.0142 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 89 |
| MarketSupply,MarketWithdraw | 12 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 8 |
| MarketBorrow,MarketSupplyCollateral | 2 |


---

## eth_stcusd_usdc

- **Max total supply (USD)**: 75,119,129.83
- **Total events**: 14,693
- **Number of users**: 87
- **Number of spikes**: 298

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 24.0 | -0.0691 |
| MarketSupply | 703.0 | -0.0516 |
| MarketWithdraw | 342.0 | 0.0127 |
| MarketBorrow | 7.0 | 0.0189 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 249 |
| MarketSupply,MarketWithdraw | 34 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 10 |
| MarketBorrow,MarketSupplyCollateral | 4 |
| MarketBorrow | 1 |


---

## eth_sdeusd_usdc

- **Max total supply (USD)**: 103,288,194.17
- **Total events**: 18,181
- **Number of users**: 61
- **Number of spikes**: 663

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 471.0 | -0.1081 |
| MarketRepay | 9.0 | -0.0363 |
| MarketBorrow | 3.0 | 0.0000 |
| MarketLiquidation | 2.0 | 0.0000 |
| MarketWithdraw | 98.0 | 0.0159 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 643 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 7 |
| MarketSupply,MarketWithdraw | 6 |
| MarketBorrow,MarketSupplyCollateral | 4 |
| MarketBorrow | 3 |


---

## eth_susde_pyusd

- **Max total supply (USD)**: 180,022,683.64
- **Total events**: 1,092
- **Number of users**: 56
- **Number of spikes**: 16

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 7.0 | -0.1147 |
| MarketSupply | 18.0 | -0.0621 |
| MarketBorrow | 9.0 | 0.0048 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 8 |
| MarketWithdraw | 5 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 2 |
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
| MarketSupply | 42.0 | -0.0450 |
| MarketRepay | 108.0 | -0.0240 |
| MarketBorrow | 34.0 | 0.0114 |
| MarketWithdraw | 14.0 | 0.0152 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 39 |
| MarketBorrow,MarketSupplyCollateral | 10 |


---

## eth_mapollo_usdc

- **Max total supply (USD)**: 5,370,054.71
- **Total events**: 578
- **Number of users**: 31
- **Number of spikes**: 15

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 28.0 | -0.1455 |
| MarketRepay | 8.0 | -0.0681 |
| MarketWithdraw | 53.0 | 0.0073 |
| MarketBorrow | 8.0 | 0.0217 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 7 |
| MarketBorrow,MarketSupplyCollateral | 6 |
| MarketBorrow | 2 |


---

## eth_syrupusdc_pyusd

- **Max total supply (USD)**: 30,014,681.10
- **Total events**: 402
- **Number of users**: 26
- **Number of spikes**: 4

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 1.0 | -0.0863 |
| MarketRepay | 3.0 | -0.0699 |
| MarketWithdraw | 1.0 | 0.0111 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketWithdraw | 2 |


---

## eth_PT-reUSD-25JUN2026_usdc

- **Max total supply (USD)**: 54,243,591.24
- **Total events**: 18,971
- **Number of users**: 361
- **Number of spikes**: 28

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 11.0 | -0.0332 |
| MarketSupply | 149.0 | -0.0329 |
| MarketBorrow | 19.0 | 0.0041 |
| MarketWithdraw | 40.0 | 0.0129 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 18 |
| MarketBorrow | 6 |
| MarketBorrow,MarketSupplyCollateral | 4 |


---

## eth_PT-USDe-25SEP2025_usdc

- **Max total supply (USD)**: 418,822,963.58
- **Total events**: 17,897
- **Number of users**: 290
- **Number of spikes**: 73

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 45.0 | -0.0481 |
| MarketSupply | 243.0 | -0.0456 |
| MarketBorrow | 16.0 | 0.0037 |
| MarketWithdraw | 105.0 | 0.0088 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 44 |
| MarketBorrow,MarketSupplyCollateral | 17 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 9 |
| MarketBorrow | 2 |
| MarketBorrow,MarketSupply | 1 |


---

## PT-reUSD-25JUN2026_usdc

- **Max total supply (USD)**: 54,243,591.24
- **Total events**: 13,237
- **Number of users**: 249
- **Number of spikes**: 25

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 9.0 | -0.0352 |
| MarketSupply | 142.0 | -0.0329 |
| MarketBorrow | 17.0 | 0.0042 |
| MarketWithdraw | 37.0 | 0.0131 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 15 |
| MarketBorrow | 6 |
| MarketBorrow,MarketSupplyCollateral | 4 |


---

## eth_PT-stcUSD-29JAN2026_usdc

- **Max total supply (USD)**: 60,017,452.09
- **Total events**: 10,954
- **Number of users**: 175
- **Number of spikes**: 196

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 91.0 | -0.0740 |
| MarketSupply | 426.0 | -0.0616 |
| MarketWithdraw | 268.0 | 0.0130 |
| MarketBorrow | 9.0 | 0.0156 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 177 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 10 |
| MarketSupply,MarketWithdraw | 7 |
| MarketBorrow,MarketSupplyCollateral | 1 |
| MarketBorrow | 1 |


---

## eth_PT-USDe-27MAR2025_dai

- **Max total supply (USD)**: 126,211,463.34
- **Total events**: 3,089
- **Number of users**: 156
- **Number of spikes**: 17

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 46.0 | -0.0714 |
| MarketRepay | 60.0 | -0.0274 |
| MarketWithdraw | 13.0 | 0.0069 |
| MarketBorrow | 40.0 | 0.0073 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 9 |
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
- **Number of spikes**: 129

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 215.0 | -0.1287 |
| MarketRepay | 6.0 | -0.0748 |
| MarketBorrow | 13.0 | 0.0053 |
| MarketWithdraw | 85.0 | 0.0127 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 80 |
| MarketSupply,MarketWithdraw | 30 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 15 |
| MarketBorrow,MarketSupply | 2 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## eth_PT-sNUSD-5MAR2026_usdc

- **Max total supply (USD)**: 11,460,920.52
- **Total events**: 3,474
- **Number of users**: 120
- **Number of spikes**: 35

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 71.0 | -0.0533 |
| MarketRepay | 6.0 | -0.0151 |
| MarketBorrow | 18.0 | 0.0027 |
| MarketWithdraw | 19.0 | 0.0158 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 22 |
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
- **Number of spikes**: 79

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketBorrow | 18.0 | -0.4739 |
| MarketSupply | 134.0 | -0.2471 |
| MarketRepay | 15.0 | -0.0657 |
| MarketWithdraw | 92.0 | 0.0136 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 64 |
| MarketSupply,MarketWithdraw | 8 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |
| MarketBorrow,MarketSupplyCollateral | 2 |
| MarketBorrow | 1 |


---

## eth_PT-slvlUSD-25SEP2025_usdc

- **Max total supply (USD)**: 18,824,491.59
- **Total events**: 7,659
- **Number of users**: 97
- **Number of spikes**: 125

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketBorrow | 6.0 | -0.1457 |
| MarketRepay | 3.0 | -0.0769 |
| MarketSupply | 195.0 | -0.0550 |
| MarketLiquidation | 1.0 | -0.0168 |
| MarketWithdraw | 73.0 | 0.0121 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 105 |
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
- **Number of spikes**: 165

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 256.0 | -0.0905 |
| MarketBorrow | 11.0 | -0.0719 |
| MarketRepay | 21.0 | -0.0414 |
| MarketWithdraw | 78.0 | 0.0125 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 153 |
| MarketBorrow,MarketSupplyCollateral | 6 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 3 |
| MarketRepay,MarketWithdraw,MarketWithdrawCollateral | 2 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_PT-wstUSR-25SEP2025_usdc

- **Max total supply (USD)**: 17,812,907.25
- **Total events**: 4,257
- **Number of users**: 76
- **Number of spikes**: 167

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 12.0 | -0.7872 |
| MarketSupply | 192.0 | -0.0922 |
| MarketBorrow | 7.0 | -0.0322 |
| MarketWithdraw | 29.0 | 0.0135 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 142 |
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
- **Number of spikes**: 67

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketBorrow | 2.0 | -0.0995 |
| MarketSupply | 200.0 | -0.0569 |
| MarketRepay | 9.0 | -0.0031 |
| MarketWithdraw | 123.0 | 0.0111 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 51 |
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
- **Number of spikes**: 59

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketRepay | 1.0 | -0.1224 |
| MarketSupply | 124.0 | -0.0807 |
| MarketBorrow | 1.0 | 0.0000 |
| MarketWithdraw | 61.0 | 0.0174 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 58 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_PT-USDe-27NOV2025_usds

- **Max total supply (USD)**: 265,788,041.17
- **Total events**: 1,062
- **Number of users**: 35
- **Number of spikes**: 26

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 23.0 | -0.0613 |
| MarketRepay | 13.0 | -0.0025 |
| MarketWithdraw | 2.0 | 0.0081 |
| MarketBorrow | 1.0 | 0.0241 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketBorrow,MarketSupplyCollateral | 20 |
| MarketBorrow | 4 |
| MarketWithdraw | 2 |


---

## eth_PT-syrupUSDC-30OCT2025_usdc

- **Max total supply (USD)**: 41,739,570.56
- **Total events**: 4,667
- **Number of users**: 27
- **Number of spikes**: 124

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 197.0 | -0.0703 |
| MarketRepay | 1.0 | -0.0001 |
| MarketWithdraw | 53.0 | 0.0148 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 105 |
| MarketSupply,MarketWithdraw | 8 |
| MarketBorrow,MarketSupply | 6 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 4 |
| MarketBorrow | 1 |


---

## eth_PT-USR-29MAY2025_usdc

- **Max total supply (USD)**: 17,663,436.43
- **Total events**: 1,666
- **Number of users**: 25
- **Number of spikes**: 61

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 84.0 | -0.0769 |
| MarketRepay | 9.0 | -0.0235 |
| MarketWithdraw | 11.0 | 0.0105 |
| MarketBorrow | 19.0 | 0.0201 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 44 |
| MarketBorrow,MarketSupplyCollateral | 7 |
| MarketBorrow | 5 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 4 |
| MarketBorrow,MarketSupply | 1 |


---

## eth_PT-sdeUSD-1753142406_usdc

- **Max total supply (USD)**: 13,003,702.42
- **Total events**: 4,030
- **Number of users**: 23
- **Number of spikes**: 53

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 95.0 | -0.1361 |
| MarketWithdraw | 40.0 | 0.0117 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 52 |
| MarketBorrow,MarketSupplyCollateral | 1 |


---

## PT-siUSD-26MAR2026_usdc

- **Max total supply (USD)**: 2,258,353.08
- **Total events**: 2,135
- **Number of users**: 18
- **Number of spikes**: 123

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 159.0 | -0.0715 |
| MarketBorrow | 5.0 | -0.0118 |
| MarketRepay | 1.0 | -0.0000 |
| MarketWithdraw | 28.0 | 0.0107 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 113 |
| MarketSupply,MarketWithdraw | 8 |
| MarketBorrow,MarketSupplyCollateral | 1 |
| MarketBorrow,MarketSupply,MarketSupplyCollateral | 1 |


---

## eth_PT-stcUSD-23JUL2026_usdc

- **Max total supply (USD)**: 26,840,950.18
- **Total events**: 3,809
- **Number of users**: 15
- **Number of spikes**: 261

#### Action Impact (weighted by volume)

| Action Type | Count | Weighted Mean ΔUtil
|-------------|-------|---------------------|
| MarketSupply | 459.0 | -0.0634 |
| MarketWithdraw | 73.0 | 0.0139 |
#### Top 5 Trigger Event Types

| Event Type | Count |
|------------|-------|
| MarketWithdraw | 253 |
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

