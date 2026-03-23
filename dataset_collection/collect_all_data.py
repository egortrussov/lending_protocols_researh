from queries import (
    get_actions_query,
)
import requests
import pandas as pd 
from datetime import datetime, timedelta
import time

BATCH_SIZE = 100
MORPHO_GRAPHQL_API = "https://api.morpho.org/graphql"
MARKETS_HASHES = {
    # "eth_cbbtc_usdc": "0x64d65c9a2d91c36d56fbc42d69e979335320169b3df63bf92789e2c8883fcc64",
    # "eth_mapollo_usdc": "0x031c7333014af51e4fd18031d14e4eaada58348cde3f6dc6ea8cca16f7387fb2",
    # "eth_rlp_usdc": "0xe1b65304edd8ceaea9b629df4c3c926a37d1216e27900505c04f14b2ed279f33",
    # "eth_cbbtc_usdt": "0x45671fb8d5dea1c4fbca0b8548ad742f6643300eeb8dbd34ad64a658b2b05bca",

    "eth_wbtc_usdc": "0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49",
    # "eth_wbtc_usdt": "0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99",

    # "eth_wsteth_usdt": "0xe7e9694b754c4d4f7e21faf7223f6fa71abaeb10296a4c43a54a7977149687d2",
    # "eth_wsteth_usdc": "0xb323495f7e4148be5643a4ea4a8221eef163e4bccfdedc2a6f4696baacbc86cc",

    # "eth_weth_usdt": "0xdbffac82c2dc7e8aa781bd05746530b0068d80929f23ac1628580e27810bc0c5",
}

# MARKETS_HASHES = {
    # "base_cbbtc_usdc": "0x9103c3b4e834476c9a62ea009ba2c884ee42e94e6e314a26f04d312434191836",
    # "base_wbtc_usdc": "0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49",
    # "base_cbbtc_usdt": "0x45671fb8d5dea1c4fbca0b8548ad742f6643300eeb8dbd34ad64a658b2b05bca",
    # "base_wbtc_usdt": "0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99",

    # "base_wsteth_usdt": "0xe7e9694b754c4d4f7e21faf7223f6fa71abaeb10296a4c43a54a7977149687d2",
    # "base_wsteth_usdc": "0xb323495f7e4148be5643a4ea4a8221eef163e4bccfdedc2a6f4696baacbc86cc",

    # "base_weth_usdt": "0xdbffac82c2dc7e8aa781bd05746530b0068d80929f23ac1628580e27810bc0c5",
# }



def query_aave_graphql(query):
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': 'https://sandbox.embed.apollographql.com',
        'Access-Control-Allow-Credentials': 'true'
    }

    # print(query)

    CNT = 0
    for I in range(10):
        response = requests.post(
            MORPHO_GRAPHQL_API,
            json={'query': query},
            headers=headers,
            timeout=100,
        )


        
        if response.status_code == 200:
            # print(response.json())
            return response.json()
        print(f"Retrying, attempt {I+1}")
        time.sleep(5 + 5 * (I // 3))
    raise Exception(f"Query failed with status {response.status_code}: {response.text}")


def get_result_df(result, market):
    df = pd.DataFrame({
        "hash": [],
        "type": [],
        "timestamp": [],
        "user_address": [],
        "assets": [],
        "assets_usd": [],
        "liquidated_assets": [],
        "liquidated_assets_usd": [],
    })
    for transaction in result["data"]["transactions"]["items"]:
        if transaction["type"] == "MarketLiquidation":
            new_row = {
                "hash": transaction["hash"],
                "type": transaction["type"],
                "timestamp": transaction["timestamp"],
                "user_address": transaction["user"]["address"],
                "assets": transaction["data"]["repaidAssets"],
                "assets_usd": transaction["data"]["repaidAssetsUsd"],
                "liquidated_assets": transaction["data"]["seizedAssets"],
                "liquidated_assets_usd": transaction["data"]["seizedAssetsUsd"],
                
            }
        else:
            new_row = {
                "hash": transaction["hash"],
                "type": transaction["type"],
                "timestamp": transaction["timestamp"],
                "user_address": transaction["user"]["address"],
                "assets": transaction["data"]["assets"],
                "assets_usd": transaction["data"]["assetsUsd"],
                "liquidated_assets": 0,
                "liquidated_assets_usd": 0,
            }
        df.loc[len(df)] = new_row
    df["market"] = market
    return df


def get_actions_history(
        start_timestamp,
        end_timestamp,
        market,
        skip=0,
):
    """
    Get market data for a specific chain
    Returns reserves (assets), rates, liquidity, etc.
    """
    
    query = get_actions_query(
        start_timestamp=start_timestamp,
        end_timestamp=end_timestamp,
        market=MARKETS_HASHES[market],
        skip=skip,
    )
    result = query_aave_graphql(query)

    result_df = get_result_df(result, market=market)
    return result_df

# hist = get_actions_history()


def process_date_range(start_date_str, end_date_str, market, csv_file_path):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")
    
    all_data = []
    current_end = end_date
    
    print(f"Processing {market} from {start_date_str} to {end_date_str}")
    
    current_start = start_date
    
    start_ts = int(current_start.timestamp())
    end_ts = int(current_end.timestamp())
    skip = 0
    pages = 0
    
    while 1:
        pages += 1
        
        daily_df = get_actions_history(start_ts, end_ts, market, skip)
        if daily_df is not None and not daily_df.empty:
            all_data.append(daily_df)
        print(f"Page {pages}, cnt = {len(daily_df)} max date {pd.to_datetime(daily_df['timestamp'].max(), unit='s')}")
        if len(daily_df) == 0 or len(daily_df) < BATCH_SIZE:
            break
        skip += len(daily_df)

        if pages % 30 == 0:
            combined_df = pd.concat(all_data, ignore_index=True)
            combined_df['datetime'] = pd.to_datetime(combined_df['timestamp'], unit='s').dt.strftime('%Y-%m-%d %H:%M:%S')
            combined_df["market_address"] = MARKETS_HASHES[market]
            combined_df.to_csv(csv_file_path, index=False)
            print(f"Saved CHECKPOINT {len(combined_df)} total events to {csv_file_path}")

    print(f"  {current_start.strftime('%Y-%m-%d')}: {len(daily_df)} events in {pages} pages")
    
    current_end = current_start
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        combined_df['datetime'] = pd.to_datetime(combined_df['timestamp'], unit='s').dt.strftime('%Y-%m-%d %H:%M:%S')
        combined_df["market_address"] = MARKETS_HASHES[market]
        combined_df.to_csv(csv_file_path, index=False)
        print(f"Saved {len(combined_df)} total events to {csv_file_path}")
        return combined_df
    
    print("No data found for the period")
    return pd.DataFrame()


def save_to_csv(dataframe, file_path):
    dataframe.to_csv(file_path, index=False)


def save_partial_data(dataframes, file_path):
    """Save partial data in case of errors"""
    if dataframes:
        partial_df = pd.concat(dataframes, ignore_index=True)
        backup_path = file_path.replace('.csv', f'_partial_{int(time.time())}.csv')
        partial_df.to_csv(backup_path, index=False)
        print(f"Partial data saved to: {backup_path}")


def get_file_size(file_path):
    """Get file size in human readable format"""
    try:
        import os
        size_bytes = os.path.getsize(file_path)
        
        # Convert to human readable format
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"
    except:
        return "Unknown"
    

import sys

MARKETS_HASHES = {
    # "eth_cbbtc_usdc": "0x64d65c9a2d91c36d56fbc42d69e979335320169b3df63bf92789e2c8883fcc64",
    # "eth_mapollo_usdc": "0x031c7333014af51e4fd18031d14e4eaada58348cde3f6dc6ea8cca16f7387fb2",
    # "eth_rlp_usdc": "0xe1b65304edd8ceaea9b629df4c3c926a37d1216e27900505c04f14b2ed279f33",
    # "eth_cbbtc_usdt": "0x45671fb8d5dea1c4fbca0b8548ad742f6643300eeb8dbd34ad64a658b2b05bca",

    # "eth_wbtc_usdc": "0x3a85e619751152991742810df6ec69ce473daef99e28a64ab2340d7b7ccfee49",
    # "eth_wbtc_usdt": "0xa921ef34e2fc7a27ccc50ae7e4b154e16c9799d3387076c421423ef52ac4df99",

    # "eth_wsteth_usdt": "0xe7e9694b754c4d4f7e21faf7223f6fa71abaeb10296a4c43a54a7977149687d2",
    # "eth_wsteth_usdc": "0xb323495f7e4148be5643a4ea4a8221eef163e4bccfdedc2a6f4696baacbc86cc",

    # "eth_weth_usdt": "0xdbffac82c2dc7e8aa781bd05746530b0068d80929f23ac1628580e27810bc0c5",

    "base_cbbtc_usdc": "0x9103c3b4e834476c9a62ea009ba2c884ee42e94e6e314a26f04d312434191836",
}

# MARKETS_HASHES = { # Yield-bearing tokens
#     # "PT-siUSD-26MAR2026_usdc": "0xaac3ffcdf8a75919657e789fa72ab742a7bbfdf5bb0b87e4bbeb3c29bbbbb05c",
#     "eth_reusd_usdc": "0x4565ac05d38b19374ccbb04c17cca60ca9353cd41824f0803d0fc7704f60eaed",

# }

# MARKETS_HASHES = { # Principal tokens
#     "eth_PT-USDe-25SEP2025_dai": "0x45d97c66db5e803b9446802702f087d4293a2f74b370105dc3a88a278bf6bb21",  # Max borrow 452,132,525.75834537 (True, 'usde')
#     "eth_PT-USDe-25SEP2025_usdc": "0x7a5d67805cb78fad2596899e0c83719ba89df353b931582eb7d3041fd5a06dc8",  # Max borrow 330,973,931.915632 (True, 'usde')
#     "eth_PT-USDe-27NOV2025_usds": "0x8cdb63a27a48ac27fadc0f158a732104bcc4e10bb61c9a5095ea7c127204e26c",  # Max borrow 243,526,360.43353495 (True, 'usde')
#     "eth_PT-USDe-27MAR2025_dai": "0xab0dcab71e65c05b7f241ea79a33452c87e62db387129e4abe15e458d433e4d8",  # Max borrow 97,377,815.0482268 (True, 'usde')
#     "eth_PT-USD0++-27MAR2025_usdc": "0x8411eeb07c8e32de0b3784b6b967346a45593bfd8baeb291cc209dc195c7b3ad",  # Max borrow 71,031,506.885819 (True, 'usd0++')
#     "eth_PT-syrupUSDC-28AUG2025_usdc": "0xa3819a7d2aee958ca0e7404137d012b51ea47d051db69d94656956eff8c80c23",  # Max borrow 57,772,451.663415 (True, 'syrupusdc')
#     "eth_PT-USDe-25SEP2025_usdt": "0xb0a9ac81a8c6a5274aa1a8337aed35a2cb2cd4feb5c6d3b39d41f234fbf2955b",  # Max borrow 49,432,163.909336 (True, 'usde')
#     "eth_PT-stcUSD-29JAN2026_usdc": "0x03f715ef1ae508ab3e1faf4dffdbf2a077d1f0ad10c5aad42cf4438d5e3328af",  # Max borrow 45,336,898.768978 (True, 'stcusd')
#     "eth_PT-reUSD-25JUN2026_usdc": "0x9bc98c2f20ac58287ef2c860eea53a2fdc27c17a7817ff1206c0b7840cc7cd79",  # Max borrow 42,900,617.97058 (True, 'reusd')
#     "eth_PT-syrupUSDC-30OCT2025_usdc": "0xb8afc953c3cc8077b4a4bf459bede8d3f80be45ca1f244e4bca13b7b1030eed5",  # Max borrow 35,727,105.086454 (True, 'syrupusdc')
#     "eth_PT-wstUSR-27MAR2025_usdc": "0xcc63ab57cdcd6dd24cd42db3ebe829fb1b56da89fcd17cea6202cf6b69d02393",  # Max borrow 31,001,300.844454 (True, 'wstusr')
#     "eth_PT-mHYPER-20NOV2025_usdc": "0x1ca75949a91c157183f53282d73c37191e7cd84002310f6632047d874aad4a0f",  # Max borrow 30,754,584.993924 (True, 'mhyper')
#     "eth_PT-csUSDL-31JUL2025_usdc": "0x544b0a093b130a3fb01b72a1279ab848575f049c73da3b5c9c718f9350a1519c",  # Max borrow 19,541,130.4488 (True, 'csusdl')
#     "eth_PT-stcUSD-23JUL2026_usdc": "0x2fb3713487c7812e7309935b034f40228841666f6b048faf31fd2110ae674f20",  # Max borrow 17,918,802.355725 (True, 'stcusd')
#     "eth_PT-USD0++-27MAR2025_usdc": "0x147977320f168afc651b7e5a1849cc1b1e64e329e1bf0212fa49dcb2856074a4",  # Max borrow 17,122,092.345604 (True, 'usd0++')
#     "eth_PT-slvlUSD-29MAY2025_usdc": "0xeb3e4a68c675d88f5a4378eab966e717bdee6a0f38c5ca6da2560ac5d1534f60",  # Max borrow 15,693,280.022799 (True, 'slvlusd')
#     "eth_PT-lvlUSD-29MAY2025_usdc": "0x185df29d35001b5657c9c964284ddbeee83a40c83e6c6e89432463e2157e075c",  # Max borrow 15,527,877.281869 (True, 'lvlusd')
#     "eth_PT-USR-29MAY2025_usdc": "0x278290bf72ec20495f3f57910bebac7f2f6a6aeff9e9d550f225b4ba26454fe0",  # Max borrow 13,873,392.432399 (True, 'usr')
#     "eth_PT-wstUSR-27MAR2025_usr": "0x1e1ae51d4be670307788612599a46a73649ef85e28bab194d3ae00c3cd693ea7",  # Max borrow 12,476,202.26509033 (True, 'wstusr')
#     "eth_PT-slvlUSD-25SEP2025_usdc": "0x4005ba6eb7d2221fe58102bd320aa6d83c47b212771bc950ab71c5074d9ab0ec",  # Max borrow 9,554,992.482185 (True, 'slvlusd')
#     "eth_PT-wstUSR-27MAR2025_usdc": "0x9940da579c167e13a14f07ba4a38e54cb8fa2abb35a3976ec1af07f77e972268",  # Max borrow 9,225,399.452 (True, 'wstusr')
#     "eth_PT-wstUSR-25SEP2025_usdc": "0xeec6c7e2ddb7578f2a7d86fc11cf9da005df34452ad9b9189c51266216f5d71b",  # Max borrow 9,172,560.608873 (True, 'wstusr')
#     "eth_PT-reUSD-18DEC2025_usdc": "0xf5de1cd86d1b96dae889356d9515a1ccfd6caae8570f8d6d49c218bb203d045d",  # Max borrow 8,904,601.87174 (True, 'reusd')
#     "eth_PT-USDe-31JUL2025_dai": "0x760b14c9003f08ac4bf0cfb02596ee4d6f0548a4fde5826bfd56befb9ed62ae9",  # Max borrow 8,766,519.073482687 (True, 'usde')
#     "eth_PT-sdeUSD-1753142406_usdc": "0x4ef32e4877329436968f4a29b0c8285531d113dad29b727d88beafe5ed45be6a",  # Max borrow 8,218,290.652325 (True, 'sdeusd')
#     "eth_PT-USD0++-31OCT2024_usdc": "0x2daab4eb520e7eab0a6d432d2edfb11775c9544a6b5e441c2e0f74abcd48f975",  # Max borrow 7,847,083.043088 (True, 'usd0++')
#     "eth_PT-sNUSD-5MAR2026_usdc": "0x2a9a5c436719badcfadbad3ad8e8179a160ded758603eaa03a883f922a1790d3",  # Max borrow 7,720,438.345611 (True, 'snusd')
#     "eth_PT-syrupUSDC-28AUG2025_usdc": "0x3bdb58058b41bb700458ba3df317e254244ddec7fc35fec93d2d53475cc6ebdc",  # Max borrow 7,025,051.027719 (True, 'syrupusdc')
#     "eth_PT-RLP-4SEP2025_usdc": "0xcc611d3ca8ce8dcc63e4e8c3cd17c9acb2ca1768eeb143b71e2dc8e6a98c3f65",  # Max borrow 6,822,088.52603 (True, 'rlp')
# }

# MARKETS_HASHES = {
#     "eth_usd0++_usdc": "0x1eda1b67414336cab3914316cb58339ddaef9e43f939af1fed162a989c98bc20",  # Max borrow 252,518,126.546969 
#     "eth_usde_dai": "0xc581c5f70bd1afa283eed57d1418c6432cbff1d862f94eaf58fdd4e46afbb67f",  # Max borrow 134,201,486.79947482 
#     "eth_rlp_usdc": "0xe1b65304edd8ceaea9b629df4c3c926a37d1216e27900505c04f14b2ed279f33",  # Max borrow 130,292,931.169511 
#     "eth_mhyper_usdc": "0x95c28d447950ca6c8bbfd25fc05b80b1fd7a1cdd17a3610b4b3f1ffc8dc2e2ed",  # Max borrow 121,157,336.705373 
#     "eth_sdeusd_usdc": "0x0f9563442d64ab3bd3bcb27058db0b0d4046a4c46f0acd811dacae9551d2b129",  # Max borrow 96,325,154.583152 
#     "eth_usr_usdc": "0x8e7cc042d739a365c43d0a52d5f24160fa7ae9b7e7c9a479bd02a56041d4cf77",  # Max borrow 92,806,567.78819 
#     "eth_wsrusd_usdc": "0x1590cb22d797e226df92ebc6e0153427e207299916e7e4e53461389ad68272fb",  # Max borrow 89,961,932.034185 
#     "eth_siusd_usdc": "0xbbf7ce1b40d32d3e3048f5cf27eeaa6de8cb27b80194690aab191a63381d8c99",  # Max borrow 78,123,231.339473 
#     "eth_syrupusdc_usdc": "0x729badf297ee9f2f6b3f717b96fd355fc6ec00422284ce1968e76647b258cf44",  # Max borrow 69,362,513.840166 
#     "eth_stcusd_usdc": "0xeb17955ea422baeddbfb0b8d8c9086c5be7a9cfdefb292119a102e981a30062e",  # Max borrow 58,626,206.93644 
#     "eth_csusdl_usdc": "0x83b7ad16905809ea36482f4fbf6cfee9c9f316d128de9a5da1952607d5e4df5e",  # Max borrow 39,700,238.599257 
#     "eth_slvlusd_usdc": "0x8b1bc4d682b04a16309a8adf77b35de0c42063a7944016cfc37a79ccac0007b6",  # Max borrow 35,704,680.169402 
#     "eth_fxsave_usdc": "0x43e925e52d7873fa8acac90dd5f246087d55b3a34c344b71884a6352491ff459",  # Max borrow 28,965,276.113905 
#     "eth_syrupusdc_pyusd": "0xc9629945524f3fde56c7e8854a6c3d48e76b9d97236abbe73c750fcc7aeb8501",  # Max borrow 26,838,689.226312 
#     "eth_wstusr_usdc": "0xd9e34b1eed46d123ac1b69b224de1881dbc88798bc7b70f504920f62f58f28cc",  # Max borrow 24,804,097.367934 

#     # "eth_wsrusd_usdt": "0xa9f70093360419b4544f17a4553ac5847d896be23f020295bd95c24af4df700e",  # Max borrow 23,105,174.409531 
#     # "eth_csusdl_usdt": "0xf9e56386e74f06af6099340525788eec624fd9c0fc0ad9a647702d3f75e3b6a9",  # Max borrow 20,866,425.276589 
#     # "eth_wstusr_usr": "0xcfe8238ad5567886652ced15ee29a431c161a5904e5a6f380baaa1b4fdc8e302",  # Max borrow 19,081,618.784205798 
#     # "eth_mmev_usdc": "0xbf6687cb042a09451e66ebc11d7716c49fb8ccc75f484f7fab0eed6624bd5838",  # Max borrow 18,903,693.406678 
#     # "eth_weeth_rlusd": "0xea4bfb18df0ee6bffb7b3f0270899a8adb92ab6b684709634c8276128813cfd4",  # Max borrow 18,323,965.911399774 
#     # "eth_usde_dai": "0xfd8493f09eb6203615221378d89f53fcd92ff4f7d62cca87eece9a2fff59e86f",  # Max borrow 18,232,862.078259524 
#     # "eth_wsrusd_ausd": "0x08bd0186c5d6ee272f973a307815ac9a8f5ed42bc8308d4b109f254011776c34",  # Max borrow 10,265,119.184856 
#     # "eth_lvlusd_usdc": "0x5f5bfaa51137098abc90b249c93b6051987877ada76135bb3dd7502b10d184a3",  # Max borrow 10,214,037.218914 
#     # "eth_snusd_usdc": "0xae60b71b407e0517ead445b7113a7ffa07ea4a9379d526ade541a3e9ec777cb4",  # Max borrow 10,099,265.825635 
#     # "eth_usde_dai": "0xdb760246f6859780f6c1b272d47a8f64710777121118e56e0cdb4b8b744a3094",  # Max borrow 9,556,320.815146511 
#     # "eth_rlp_susds": "0x13dd22c3111106f703052d5f9166812f0bf1f4679f3db7dfd82037971ce5468f",  # Max borrow 9,147,038.467956917 
#     # "eth_susdf_usdc": "0xbed987dd46049adb1ff34de8ef761a9da3b08890fa7fff629ea9b66d049de823",  # Max borrow 8,705,974.267239 
#     # "eth_lbtc_usdc": "0xbf02d6c6852fa0b8247d5514d0c91e6c1fbde9a168ac3fd2033028b5ee5ce6d0",  # Max borrow 6,506,183.499037 
#     # "eth_rlp_ausd": "0x4b86442549b52826e0fc11770ec5154450cb3c5c14dc751a761d81dcfbe7a7b2",  # Max borrow 6,100,769.407769 
#     # "eth_reusd_usdc": "0x4565ac05d38b19374ccbb04c17cca60ca9353cd41824f0803d0fc7704f60eaed",  # Max borrow 5,778,564.986495 
#     # "eth_susdf_usdf": "0xe8c9d076ee7e6fcadd34165c44c08fe61533e7ab4accbed76d7e7f7d5a011708",  # Max borrow 5,221,234.7263819 

# }

# MARKETS_HASHES = {
#     "base_cbbtc_usdc_full": "0x9103c3b4e834476c9a62ea009ba2c884ee42e94e6e314a26f04d312434191836",
# }

if '-raw' in sys.argv:
    print("Fetching raw parameters...")
    for market in MARKETS_HASHES.keys():
        process_date_range(
            start_date_str="2025-11-26 17:21:02",
            # start_date_str="2022-01-01 00:00:00",
            end_date_str="2027-02-01 00:00:00",
            market=market,
            csv_file_path=f"./data/markets_raw/{market}6.csv",
        )
        # break

if '-markets' in sys.argv:
    print("fetching market data...")
    import subprocess
    subprocess.run(['python3', 'common_data.py'])

if '-assets' in sys.argv:
    print("fetching assets data...")
    import subprocess
    subprocess.run(['python3', 'get_assets_data.py'])

if '-market-metrics' in sys.argv:
    print("Creating market metrics changes df...")
    import subprocess
    subprocess.run(['python3', 'compute_market_metrics_changes_df.py', '--markets', ' '.join(MARKETS_HASHES.keys())])




# for market in MARKETS_HASHES.keys():
#     process_date_range(
#         start_date_str="2023-03-31 17:26:24",
#         end_date_str="2027-02-01 00:00:00",
#         market=market,
#         csv_file_path=f"./data/markets_raw/{market}.csv",
#     )
#     # break
