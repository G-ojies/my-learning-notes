"""
Bitcoin Transaction ID (TXID) Calculator
Research Notes on Double SHA-256 and Little-Endian byte reversal.
"""
import hashlib

def calculate_txid(raw_tx_hex: str) -> str:
    """
    Calculates the standard TXID from a raw transaction hex.
    
    Steps:
    1. Convert the raw hex string into bytes.
    2. Perform SHA-256(SHA-256(bytes)).
    3. Reverse the resulting bytes (Little-Endian) for display.
    """
    try:
        raw_tx_bytes = bytes.fromhex(raw_tx_hex)
    except ValueError:
        return "Invalid hex string provided."
        
    # 1st Hash
    first_hash = hashlib.sha256(raw_tx_bytes).digest()
    
    # 2nd Hash
    second_hash = hashlib.sha256(first_hash).digest()
    
    # Reverse the bytes! Bitcoin Core stores hashes internally in little-endian,
    # so we must reverse the big-endian hash output to match block explorers.
    txid_bytes = second_hash[::-1]
    
    return txid_bytes.hex()

if __name__ == "__main__":
    print("🆔 Bitcoin TXID Generator")
    print("-" * 65)
    
    # Example: A very simple legacy transaction (raw hex)
    # This is the coinbase transaction from Block 1!
    block_1_coinbase_tx = (
        "01000000010000000000000000000000000000000000000000000000000000000000000000"
        "ffffffff0704ffff001d0104ffffffff0100f2052a0100000043410496b538e853519c726a"
        "2c91e61ec11600ae1390813a627c66fb8be7947be63c52da7589379515d4e0a604f8141781"
        "e62294721166bf621e73a82cbf2342c858eeac00000000"
    )
    
    expected_txid = "0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098"
    calculated_txid = calculate_txid(block_1_coinbase_tx)
    
    print(f"Raw Tx Hex Length : {len(block_1_coinbase_tx)} characters")
    print(f"Calculated TXID   : {calculated_txid}")
    print(f"Expected TXID     : {expected_txid}")
    print("-" * 65)
    
    if calculated_txid == expected_txid:
        print("✅ SUCCESS: Byte reversal applied correctly!")
    else:
        print("❌ FAILED: TXIDs do not match.")
