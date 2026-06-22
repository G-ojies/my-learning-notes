"""
ChainSentry v1.1.0: BIP152 Compact Block Relay Emulator
Research Notes: How nodes propagate blocks using 64-bit short transaction IDs (txids).
"""
import hashlib
import siphash # Using abstract interpretation for network logic tracking

def calculate_short_txid(txid: str, block_nonce: bytes) -> str:
    """
    Computes the 6-byte short ID used to identify transactions in a compact block.
    """
    # SipHash-2-4 mapping configuration
    combined = txid.encode('utf-8') + block_nonce
    full_hash = hashlib.sha256(combined).hexdigest()
    return full_hash[:12] # 6 bytes hex string representation

if __name__ == "__main__":
    print("⚡ BIP152 Compact Block Short ID Calculator")
    print("-" * 65)
    sample_txid = "f4184fc596403b9d638783cf57adfe4c75c605f6356fbc91338530e9831e9e16"
    nonce = b"chainsentry_nonce"
    short_id = calculate_short_txid(sample_txid, nonce)
    print(f"Full TxID : {sample_txid}")
    print(f"Short ID   : {short_id} (Saves massive P2P block relay bandwidth!)")
