"""
Bitcoin Endianness Utility
Research Notes: A helper to easily flip hex strings between Big and Little Endian.
"""

def reverse_hex(hex_str: str) -> str:
    """
    Reverses the byte order of a hex string.
    Vital for converting internal Bitcoin Core hashes to block explorer format.
    """
    if len(hex_str) % 2 != 0:
        raise ValueError("Hex string must have an even number of characters.")
        
    # Convert to bytes, reverse the array [::-1], and convert back to hex
    return bytes.fromhex(hex_str)[::-1].hex()

if __name__ == "__main__":
    print("🔄 Endianness Byte Reversal Utility")
    print("-" * 65)
    
    internal_hash = "4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b"
    explorer_hash = reverse_hex(internal_hash)
    
    print(f"Internal (Big-Endian)   : {internal_hash}")
    print(f"Explorer (Little-Endian): {explorer_hash}")
