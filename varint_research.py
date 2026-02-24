"""
Bitcoin Variable Length Integer (VarInt / CompactSize)
Research Notes on how Bitcoin dynamically sizes integers to save space.
"""
import struct

def encode_varint(i: int) -> bytes:
    """Encodes a standard integer into Bitcoin's compact VarInt bytes."""
    if i < 0xfd:
        return bytes([i]) # 1 byte for numbers under 253
    elif i <= 0xffff:
        return b'\xfd' + struct.pack('<H', i) # 3 bytes (prefix fd + 2 bytes)
    elif i <= 0xffffffff:
        return b'\xfe' + struct.pack('<I', i) # 5 bytes (prefix fe + 4 bytes)
    else:
        return b'\xff' + struct.pack('<Q', i) # 9 bytes (prefix ff + 8 bytes)

def decode_varint(b: bytes) -> tuple:
    """Decodes a VarInt from raw bytes. Returns (value, bytes_consumed)."""
    prefix = b[0]
    if prefix < 0xfd:
        return prefix, 1
    elif prefix == 0xfd:
        return struct.unpack('<H', b[1:3])[0], 3
    elif prefix == 0xfe:
        return struct.unpack('<I', b[1:5])[0], 5
    else:
        return struct.unpack('<Q', b[1:9])[0], 9

if __name__ == "__main__":
    print("📏 Bitcoin VarInt Serialization Engine")
    print("-" * 45)
    
    test_numbers = [5, 252, 255, 65535, 1000000]
    
    for num in test_numbers:
        encoded = encode_varint(num)
        decoded_val, size = decode_varint(encoded)
        print(f"Original: {num:<7} | Hex: {encoded.hex():<10} | Bytes Used: {size}")
