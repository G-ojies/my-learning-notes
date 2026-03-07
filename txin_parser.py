"""
Bitcoin Transaction Input (TxIn) Parser
Research Notes: How Bitcoin points to previous UTXOs to spend them.
"""
import struct

def parse_tx_input(hex_str: str) -> dict:
    """
    Parses a single raw Bitcoin Transaction Input.
    
    Structure:
    1. Previous TXID (32 bytes, Little-Endian)
    2. Previous Output Index / Vout (4 bytes, Little-Endian)
    3. Script Length (VarInt) - We'll assume 1 byte for this simple script
    4. ScriptSig (Variable length) - The unlocking script/signature
    5. Sequence (4 bytes, Little-Endian)
    """
    try:
        raw_bytes = bytes.fromhex(hex_str)
    except ValueError:
        return {"Error": "Invalid hex string."}
        
    # 1. Previous TXID (Reverse from Little-Endian to Big-Endian for block explorers)
    prev_txid = raw_bytes[0:32][::-1].hex()
    
    # 2. Previous Output Index (Vout)
    vout = struct.unpack('<I', raw_bytes[32:36])[0]
    
    # 3. Script Length (Assuming 1 byte VarInt for standard P2PKH)
    script_len = raw_bytes[36]
    
    # 4. ScriptSig (The actual signature + public key)
    start_script = 37
    end_script = start_script + script_len
    script_sig = raw_bytes[start_script:end_script].hex()
    
    # 5. Sequence (Used for Locktime, RBF, etc.)
    sequence = raw_bytes[end_script:end_script+4].hex()
    
    return {
        "Previous TXID": prev_txid,
        "Vout Index": vout,
        "Script Length": f"{script_len} bytes",
        "ScriptSig (Hex)": script_sig,
        "Sequence": sequence
    }

if __name__ == "__main__":
    print("📥 Bitcoin TxIn (Input) Parser")
    print("-" * 65)
    
    # Example: A standard P2PKH input hex
    sample_txin = (
        "b10c538466e01768461ab109968eb1e40fb871887e224e2c908f9c2d1b11ce15" # TXID (Reversed)
        "00000000" # Vout (0)
        "6a" # Script Length (106 bytes)
        "47304402206162636465666768696a6b6c6d6e6f707172737475767778797a3031323334350220363738396162636465666768696a6b6c6d6e6f707172737475767778797a303101210250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352" # ScriptSig
        "ffffffff" # Sequence
    )
    
    for key, val in parse_tx_input(sample_txin).items():
        print(f"{key:<18}: {val}")
