"""
Bitcoin Transaction Output (TxOut / UTXO) Parser
Research Notes on how Bitcoin stores values and locking scripts.
"""
import sys
import struct

# Import the VarInt decoder we built previously!
try:
    from varint_research import decode_varint
except ImportError:
    print("Warning: varint_research.py not found. Make sure it is in this directory.")
    sys.exit(1)

def parse_tx_output(hex_str: str) -> dict:
    """
    Parses a raw Bitcoin Transaction Output (TxOut).
    
    Structure:
    1. Value (8 bytes, Little-Endian) - Amount in Satoshis.
    2. Script Length (VarInt) - How many bytes the locking script is.
    3. ScriptPubKey (Variable) - The actual locking conditions.
    """
    try:
        raw_bytes = bytes.fromhex(hex_str)
    except ValueError:
        return {"Error": "Invalid hex string provided."}
        
    # 1. Extract the Value (first 8 bytes, little-endian unsigned long long)
    value_bytes = raw_bytes[:8]
    satoshis = struct.unpack('<Q', value_bytes)[0]
    btc = satoshis / 100_000_000
    
    # 2. Extract the Script Length using our custom VarInt decoder
    script_len, varint_bytes_used = decode_varint(raw_bytes[8:])
    
    # 3. Extract the actual ScriptPubKey (locking script)
    start_idx = 8 + varint_bytes_used
    end_idx = start_idx + script_len
    script_pubkey = raw_bytes[start_idx:end_idx]
    
    return {
        "Satoshis": satoshis,
        "BTC Value": f"{btc:.8f} BTC",
        "Script Length": f"{script_len} bytes",
        "ScriptPubKey (Hex)": script_pubkey.hex()
    }

if __name__ == "__main__":
    print("🪙 Bitcoin UTXO / TxOut Parser")
    print("-" * 65)
    
    # Example: A raw transaction output containing exactly 0.5 BTC
    # Value (8 bytes) + Script Length (1 byte) + P2PKH Script (25 bytes)
    sample_txout_hex = "0008fa02000000001976a91489abcdef0123456789abcdef0123456789abcdef88ac"
    
    parsed_data = parse_tx_output(sample_txout_hex)
    
    print(f"Raw TxOut Hex : {sample_txout_hex}\n")
    for key, val in parsed_data.items():
        print(f"{key:<20}: {val}")
    print("-" * 65)
    print("Notice how the 8-byte value '0008fa0200000000' translates to exactly 50,000,000 Satoshis!")
