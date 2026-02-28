"""
Bitcoin 80-byte Block Header Parser
Research Notes on the core structure hashed by miners.
"""
import struct

def parse_block_header(header_hex: str) -> dict:
    """
    Parses an 80-byte block header into its 6 core components.
    Note: Hashes are displayed in little-endian (reversed) format.
    """
    if len(header_hex) != 160:
        return {"Error": "Block header must be exactly 80 bytes (160 hex characters)."}
        
    header_bytes = bytes.fromhex(header_hex)
    
    # 1. Version (4 bytes, Little-Endian)
    version = struct.unpack('<I', header_bytes[0:4])[0]
    
    # 2. Previous Block Hash (32 bytes, reversed for display)
    prev_block = header_bytes[4:36][::-1].hex()
    
    # 3. Merkle Root (32 bytes, reversed for display)
    merkle_root = header_bytes[36:68][::-1].hex()
    
    # 4. Timestamp (4 bytes, Little-Endian Epoch)
    timestamp = struct.unpack('<I', header_bytes[68:72])[0]
    
    # 5. Bits / Target Difficulty (4 bytes)
    bits = header_bytes[72:76].hex()
    
    # 6. Nonce (4 bytes, Little-Endian)
    nonce = struct.unpack('<I', header_bytes[76:80])[0]
    
    return {
        "Version": version,
        "Previous Block": prev_block,
        "Merkle Root": merkle_root,
        "Timestamp (Epoch)": timestamp,
        "Bits (Difficulty)": bits,
        "Nonce": nonce
    }

if __name__ == "__main__":
    # The Genesis Block Header (80 bytes)
    genesis_header = (
        "01000000"
        "0000000000000000000000000000000000000000000000000000000000000000"
        "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a"
        "29ab5f49"
        "ffff001d"
        "1dac2b7c"
    )
    
    print("🧱 Parsing Genesis Block Header:")
    print("-" * 65)
    for key, value in parse_block_header(genesis_header).items():
        print(f"{key:<20}: {value}")
