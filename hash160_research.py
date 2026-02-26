"""
Bitcoin Hash160 (SHA256 + RIPEMD160)
Research Notes on how public keys are hashed to create secure receiving addresses.
"""
import hashlib
import sys

# Import our custom Base58Check encoder from yesterday!
try:
    from base58_research import base58check_encode
except ImportError:
    print("Warning: base58_research.py not found. Address generation will be skipped.")
    base58check_encode = None

def hash160(public_key_bytes: bytes) -> bytes:
    """
    Performs RIPEMD160(SHA256(data))
    This is the standard hashing algorithm for Bitcoin public keys.
    """
    # 1. First hash with SHA256
    sha256_hash = hashlib.sha256(public_key_bytes).digest()
    
    # 2. Second hash with RIPEMD160
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_hash)
    
    return ripemd160.digest()

if __name__ == "__main__":
    print("🪪 Bitcoin Hash160 & P2PKH Address Generator")
    print("-" * 60)
    
    # Example: A compressed public key (starts with 02 or 03, 33 bytes long)
    pubkey_hex = "0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352"
    pubkey_bytes = bytes.fromhex(pubkey_hex)
    
    # Generate the Hash160 fingerprint
    h160_bytes = hash160(pubkey_bytes)
    
    print(f"Public Key (Hex) : {pubkey_hex}")
    print(f"Hash160 (Hex)    : {h160_bytes.hex()}")
    print("-" * 60)
    
    # Combine it with yesterday's work to make a real address
    if base58check_encode:
        # 0x00 is the version byte for Mainnet P2PKH
        address = base58check_encode(b'\x00', h160_bytes)
        print(f"Final P2PKH Address: {address}")
        print("(This is what you hand to someone to get paid!)")
