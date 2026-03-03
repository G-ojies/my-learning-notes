"""
Bitcoin DER Signature Encoder
Research Notes: Packaging raw ECDSA (r, s) values into a broadcastable hex format.
"""

def int_to_der_bytes(val: int) -> bytes:
    """
    Converts an integer to bytes and prepends a 0x00 byte if the first bit is 1.
    Why? DER integers are signed. If the first byte is >= 0x80, it would be read 
    as a negative number, which is invalid for ECDSA signatures!
    """
    # Convert to hex, ensuring even length
    hex_str = hex(val)[2:]
    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str
        
    val_bytes = bytes.fromhex(hex_str)
    
    # Prepend 0x00 if the most significant bit is 1 (>= 128)
    if val_bytes[0] >= 0x80:
        val_bytes = b'\x00' + val_bytes
        
    return val_bytes

def encode_der(r: int, s: int) -> str:
    """
    Encodes the r and s values into a strict DER format.
    Structure:
    [0x30] [Total Length] [0x02] [r Length] [r Bytes] [0x02] [s Length] [s Bytes]
    """
    r_bytes = int_to_der_bytes(r)
    s_bytes = int_to_der_bytes(s)
    
    # 0x02 is the DER marker for an Integer
    r_encoded = b'\x02' + bytes([len(r_bytes)]) + r_bytes
    s_encoded = b'\x02' + bytes([len(s_bytes)]) + s_bytes
    
    sig_body = r_encoded + s_encoded
    
    # 0x30 is the DER marker for a Compound Structure (Sequence)
    der_sig = b'\x30' + bytes([len(sig_body)]) + sig_body
    
    # Bitcoin signatures typically append a Hash Type byte at the very end (e.g., 0x01 for SIGHASH_ALL)
    bitcoin_sig = der_sig + b'\x01'
    
    return bitcoin_sig.hex()

if __name__ == "__main__":
    print("📦 Bitcoin DER Signature Encoder")
    print("-" * 65)
    
    # Example (r, s) values from an ECDSA signature
    r_val = 0x82fca386c7a227600b2fe50b7cae11ec86d3bf1fbe471be89827e19d72aa1d
    s_val = 0x21c81bc3888a51323a9fb8aa4b1e5e4a29ab5f49ffff001d1dac2b7c4a5e1e
    
    der_hex = encode_der(r_val, s_val)
    
    print(f"Raw 'r' (Hex) : {hex(r_val)}")
    print(f"Raw 's' (Hex) : {hex(s_val)}")
    print(f"\nFinal DER Sig : {der_hex}")
    print("-" * 65)
    print("Notice the '30' at the start, the '02's separating the numbers,")
    print("and the '01' (SIGHASH_ALL) appended at the very end!")
