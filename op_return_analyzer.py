"""
ChainSentry: OP_RETURN Payload Analyzer
Research Notes: How arbitrary data (like Rollups, timestamping) is anchored on-chain.
"""

def analyze_op_return(script_pubkey_hex: str) -> dict:
    """
    Parses an OP_RETURN (0x6a) output to extract the data payload.
    """
    if not script_pubkey_hex.startswith("6a"):
        return {"Error": "Not an OP_RETURN script"}
        
    # The next byte is usually the pushdata length
    length_hex = script_pubkey_hex[2:4]
    payload_len = int(length_hex, 16)
    
    # The actual payload
    payload_hex = script_pubkey_hex[4:4 + (payload_len * 2)]
    
    try:
        decoded_text = bytes.fromhex(payload_hex).decode('utf-8')
    except UnicodeDecodeError:
        decoded_text = "<Binary Data>"
        
    return {
        "Payload Length": f"{payload_len} bytes",
        "Raw Hex": payload_hex,
        "Decoded Text": decoded_text
    }

if __name__ == "__main__":
    print("💾 OP_RETURN Data Extractor")
    print("-" * 65)
    # 6a (OP_RETURN) + 0e (Push 14 bytes) + 436861696e53656e74727920312e30 (Hex for "ChainSentry 1.0")
    dummy_script = "6a0e436861696e53656e74727920312e30"
    
    for k, v in analyze_op_return(dummy_script).items():
        print(f"{k:<15}: {v}")
