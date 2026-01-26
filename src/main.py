import requests
import pandas as pd
import time
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# --- CONFIGURATION ---
SNOWFLAKE_CONFIG = {
    "user": "MY_USERNAME",
    "password": "MY_PASSWORD",
    "account": "MY_ACCOUNT",
    "warehouse": "MY_WH",
    "database": "MY_DB",
    "schema": "DEFI_ANALYTICS"
}

PROTOCOLS = [
    "hyperlend", "hypurrfi", "project-x", "kinetiq", "hybra", 
    "sentiment", "hyperpie", "valantis", "felix", 
    "laminar", "upshift", "morpho", "hyperswap"
]

# --- EXTRACTION & TRANSFORMATION ---
tvl_data = []
token_data = []

print("Starting data extraction from DefiLlama...")

for slug in PROTOCOLS:
    url = f"https://api.llama.fi/updatedProtocol/{slug}"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        
        target_chain = None
        if 'chainTvls' in data:
            for chain in data['chainTvls'].keys():
                if "Hyper" in chain:
                    target_chain = chain
                    break
        
        if target_chain:
            # 1. TVL Master
            entries = data['chainTvls'][target_chain].get('tvl', [])
            for entry in entries:
                current_date = pd.to_datetime(entry['date'], unit='s').date()
                val = entry.get('totalLiquidityUSD') or entry.get('totalLiquidity')
                if val is not None:
                    tvl_data.append({
                        "DATE": current_date,
                        "PROTOCOL": slug,
                        "TVL_USD": float(val)
                    })
            
# 2. Tokens Detailed
            token_entries = data['chainTvls'][target_chain].get('tokensInTvl') or \
                           data['chainTvls'][target_chain].get('tokens') or []
            
            for entry in token_entries:
                current_date = pd.to_datetime(entry['date'], unit='s').date()
                tokens_dict = entry.get('tokens', {})
                if tokens_dict:
                    for t_symbol, t_value in tokens_dict.items():
                        token_data.append({
                            "DATE": current_date,
                            "PROTOCOL": slug,
                            "TOKEN": t_symbol,
                            "VALUE": float(t_value)
                        })
            print(f"Successfully processed: {slug}")
        else:
            print(f"No Hyperliquid chain data found for: {slug}")
            
    except Exception as e:
        print(f"Extraction error for {slug}: {e}")
    time.sleep(0.5)

df_tvl = pd.DataFrame(tvl_data)
df_tokens = pd.DataFrame(token_data)

# --- SNOWFLAKE LOADING ---
if df_tvl.empty:
    print("No data collected. Check protocol slugs or API response.")
else:
    print(f"Connecting to Snowflake to upload {len(df_tvl)} TVL rows and {len(df_tokens)} token rows...")
    conn = snowflake.connector.connect(**SNOWFLAKE_CONFIG)
    try:
        # Load TVL
        success_tvl, nchunks_tvl, nrows_tvl, _ = write_pandas(conn, df_tvl, "TVL_MASTER")
        if success_tvl:
            print(f"SUCCESS: Uploaded {nrows_tvl} rows to TVL_MASTER")
        
        # Load Tokens
        if not df_tokens.empty:
            success_tokens, nchunks_tokens, nrows_tokens, _ = write_pandas(conn, df_tokens, "TOKENS_DETAILED")
            if success_tokens:
                print(f"SUCCESS: Uploaded {nrows_tokens} rows to TOKENS_DETAILED")
                
    except Exception as e:
        print(f"Snowflake upload error: {e}")
    finally:
        conn.close()
        print("Snowflake connection closed.")
