"""
Bitcoin Base58Check Encoder
Research Notes on how Bitcoin formats legacy addresses to prevent typos.
The alphabet specifically removes 0, O, I, and l to avoid visual confusion.
"""
import hashlib

# Bitcoin's specific Base58 alphabet
ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def double_sha256(data: bytes) -> bytes:
    """Performs SHA256(SHA256(data))"""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def base58check_encode(version_byte: bytes, payload: bytes) -> str:
    """
    Encodes a payload (like a RIPEMD160 Public Key Hash) into a Base58Check string.
    """
    # 1. Prepend the version byte (e.g., 0x00 for Mainnet P2PKH)
    versioned_payload = version_byte + payload
    
    # 2. Calculate the 4-byte checksum
    checksum = double_sha256(versioned_payload)[:4]
    
    # 3. Append the checksum to the end
    full_payload = versioned_payload + checksum
    
    # 4. Convert the full byte array into a massive integer
    num = int.from_bytes(full_payload, 'big')
    
    # 5. Perform the Base58 math (modulo 58)
    encoded = ""
    while num > 0:
        num, mod = divmod(num, 58)
        encoded = ALPHABET[mod] + encoded
        
    # 6. Handle leading zeros (each leading zero byte becomes a '1' in Base58)
    pad = 0
    for byte in full_payload:
        if byte == 0:
            pad += 1
        else:
            break
            
    return (ALPHABET[0] * pad) + encoded

if __name__ == "__main__":
    print("🔤 Bitcoin Base58Check Address Generator")
    print("-" * 45)
    
    # Example: A random 20-byte Hash160 (Public Key Hash)
    # Version byte 0x00 means it's a mainnet P2PKH address (starts with '1')
    version = b'\x00'
    pubkey_hash = bytes.fromhex("751e76e8199196d454941c45d1b3a323f1433bd6")
    
    address = base58check_encode(version, pubkey_hash)
    
    print(f"Version Byte : 0x{version.hex()}")
    print(f"PubKey Hash  : {pubkey_hash.hex()}")
    print(f"Final Address: {address}")
    print("-" * 45)
    print("Notice how the address starts with '1' because of the 0x00 version byte!")
