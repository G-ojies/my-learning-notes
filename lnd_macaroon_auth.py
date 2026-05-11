"""
ChainSentry: Lightning Network (LND) Authentication
Research Notes: Connecting to an LND node requires TLS certificates and Macaroons.
"""

def blueprint_lnd_headers(macaroon_hex: str) -> dict:
    """
    LND uses 'Macaroons' instead of standard passwords. 
    They are essentially bearer tokens with cryptographically baked-in permissions (e.g., Read Only).
    """
    headers = {
        "Grpc-Metadata-macaroon": macaroon_hex,
        "Content-Type": "application/json"
    }
    return headers

if __name__ == "__main__":
    print("⚡ Lightning Network RPC Authentication Blueprint")
    
    # Dummy readonly macaroon
    dummy_macaroon = "0201036c6e6402ea01030a101b...000000021"
    
    print("HTTP Headers required for LND REST API:")
    for k, v in blueprint_lnd_headers(dummy_macaroon).items():
        print(f"  {k}: {v[:20]}...")
