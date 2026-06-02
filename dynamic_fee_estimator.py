"""
ChainSentry: Dynamic Fee Estimator
Research Notes: Querying the node's `estimatesmartfee` to tag transactions as high/low priority.
"""
import json

def parse_fee_estimate(rpc_response: str) -> dict:
    """
    Converts Bitcoin Core's BTC/kB fee format into human-readable sats/vB.
    """
    data = json.loads(rpc_response)
    
    # Core returns fees in BTC per kilobyte
    feerate_btc_per_kb = data.get("feerate", 0.00001) # Fallback to 1 sat/vB
    
    # Convert BTC/kB to sats/vByte:
    # 1 BTC = 100,000,000 sats
    # 1 kB = 1000 vBytes
    sats_per_vbyte = (feerate_btc_per_kb * 100_000_000) / 1000
    
    return {
        "Target Blocks": data.get("blocks"),
        "Raw BTC/kB": feerate_btc_per_kb,
        "Estimated Sats/vB": max(1, int(sats_per_vbyte)) # Enforce minimum relay fee
    }

if __name__ == "__main__":
    print("📈 ChainSentry Dynamic Fee Estimation")
    print("-" * 65)
    
    # Mocking the JSON response from `bitcoin-cli estimatesmartfee 2`
    mock_rpc_response = '{"feerate": 0.00045000, "blocks": 2}'
    
    result = parse_fee_estimate(mock_rpc_response)
    
    for key, val in result.items():
        print(f"{key:<20}: {val}")
        
    print("-" * 65)
    print("ChainSentry will use this to flag if an RBF replacement actually has enough fee to confirm!")
