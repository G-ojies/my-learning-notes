"""
Bitcoin Wallet Import Format (WIF)
Research Notes on how raw 256-bit private keys are formatted for users.
Demonstrates reusability of our custom Base58Check encoder.
"""
import sys

# Import the Base58Check encoder we built in the last commit!
try:
    from base58_research import base58check_encode
except ImportError:
    print("Error: Ensure base58_research.py is in the same directory.")
    sys.exit(1)

def encode_wif(private_key_hex: str, compressed: bool = True) -> str:
    """
    Converts a raw 32-byte private key into WIF.
    
    Steps:
    1. Add version byte 0x80 (Mainnet Private Key).
    2. Add the 32-byte raw private key.
    3. If the public key will be compressed, append 0x01.
    4. Base58Check encode the whole thing.
    """
    if len(private_key_hex) != 64:
        raise ValueError("Private key must be exactly 64 hex characters (32 bytes).")
        
    version_byte = b'\x80'
    payload = bytes.fromhex(private_key_hex)
    
    # Append suffix if this key will generate a compressed public key
    if compressed:
        payload += b'\x01'
        
    return base58check_encode(version_byte, payload)

if __name__ == "__main__":
    print("🔑 Bitcoin WIF Private Key Generator")
    print("-" * 60)
    
    # Example: A dummy 32-byte private key (NEVER USE THIS WITH REAL FUNDS)
    dummy_priv_key = "0c28fca386c7a227600b2fe50b7cae11ec86d3bf1fbe471be89827e19d72aa1d"
    
    wif_compressed = encode_wif(dummy_priv_key, compressed=True)
    wif_uncompressed = encode_wif(dummy_priv_key, compressed=False)
    
    print(f"Raw Hex Key  : {dummy_priv_key}")
    print(f"WIF (Comp)   : {wif_compressed}")
    print(f"WIF (Uncomp) : {wif_uncompressed}")
    print("-" * 60)
    print("Notice how compressed WIFs start with 'K' or 'L', and uncompressed start with '5'!")
