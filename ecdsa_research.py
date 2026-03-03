"""
Bitcoin ECDSA Signature Generation
Research Notes: How a private key signs a transaction hash to produce (r, s).
"""
import hashlib
import os

# SECP256k1 Curve Parameters
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141 # Curve Order

# Import scalar multiplication from yesterday's script!
try:
    from secp256k1_research import scalar_multiply, G_X, G_Y, inverse_mod
except ImportError:
    print("Error: secp256k1_research.py not found. We need yesterday's math!")
    exit()

def generate_signature(private_key_hex: str, message_hash_hex: str) -> tuple:
    """
    Signs a message hash using ECDSA.
    Returns the signature as a tuple of two integers: (r, s).
    """
    d = int(private_key_hex, 16)
    z = int(message_hash_hex, 16)
    
    # ECDSA requires a random/deterministic nonce (k) for EVERY signature.
    # WARNING: In production, use RFC6979 for deterministic k. 
    # For this research script, we use a secure random number.
    k = int.from_bytes(os.urandom(32), 'big') % N
    if k == 0:
        k = 1
        
    # Step 1: Calculate the curve point (x1, y1) = k * G
    x1, y1 = scalar_multiply(k, (G_X, G_Y))
    
    # Step 2: Calculate r = x1 mod N
    r = x1 % N
    if r == 0:
        raise ValueError("r cannot be 0, generate a new k")
        
    # Step 3: Calculate s = (z + r * d) / k mod N
    # We use modular inverse to do division in elliptic curve cryptography
    k_inv = inverse_mod(k, N)
    s = (k_inv * (z + r * d)) % N
    
    if s == 0:
        raise ValueError("s cannot be 0, generate a new k")
        
    # Bitcoin Improvement Proposal (BIP) 62 enforces "Low S" values to prevent transaction malleability.
    if s > N // 2:
        s = N - s
        
    return r, s

if __name__ == "__main__":
    print("✍️  Bitcoin ECDSA Signature Generator")
    print("-" * 65)
    
    # Example Private Key and a fake Transaction Hash
    priv_key = "0c28fca386c7a227600b2fe50b7cae11ec86d3bf1fbe471be89827e19d72aa1d"
    tx_hash  = "b10c538466e01768461ab109968eb1e40fb871887e224e2c908f9c2d1b11ce15"
    
    r, s = generate_signature(priv_key, tx_hash)
    
    print(f"Message Hash (z): {tx_hash}")
    print(f"Signature (r)   : {hex(r)}")
    print(f"Signature (s)   : {hex(s)}")
    print("-" * 65)
    print("These two values (r, s) are what miners verify to authorize a payment!")
