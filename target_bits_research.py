"""
Bitcoin Block Header 'Bits' (Proof-of-Work Target) Decoder
Research Notes on how Bitcoin compresses massive mining difficulty targets into 4 bytes.
"""

def decode_bits_to_target(bits_hex: str) -> int:
    """
    Converts the 4-byte compact 'bits' field into the full 256-bit target.
    
    Structure of 'Bits' (e.g., 1d00ffff):
    - First byte (1d) is the Exponent (size of the number in bytes).
    - Last 3 bytes (00ffff) is the Coefficient (the significant digits).
    
    Formula: Target = Coefficient * 256^(Exponent - 3)
    """
    if len(bits_hex) != 8:
        raise ValueError("Bits must be exactly 4 bytes (8 hex characters).")
        
    # 1. Extract the exponent and coefficient
    exponent = int(bits_hex[:2], 16)
    coefficient = int(bits_hex[2:], 16)
    
    # 2. Calculate the target using Satoshi's formula
    # 256 is 2**8, so shifting by (exponent - 3) bytes is the same as multiplying by 256**(exp-3)
    target = coefficient * (256 ** (exponent - 3))
    
    return target

if __name__ == "__main__":
    print("⛏️  Bitcoin Proof-of-Work Target Calculator")
    print("-" * 65)
    
    # Example: The 'bits' from the Genesis Block (Block 0)
    genesis_bits = "1d00ffff"
    
    target_int = decode_bits_to_target(genesis_bits)
    target_hex = f"{target_int:064x}" # Pad to 64 hex characters (256 bits)
    
    print(f"Compact 'Bits'     : {genesis_bits}")
    print(f"Target (Decimal)   : {target_int}")
    print(f"Target (Full Hex)  : {target_hex}")
    print("-" * 65)
    print("Notice all the leading zeros in the Full Hex!")
    print("A miner's block hash MUST start with at least this many zeros to be valid.")
