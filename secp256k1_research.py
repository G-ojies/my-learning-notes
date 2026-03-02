"""
Bitcoin SECP256k1 Elliptic Curve Cryptography
Research Notes: Deriving a Public Key from a Private Key using pure math.
Equation: y^2 = x^3 + 7
"""

# SECP256k1 Curve Parameters
P = 2**256 - 2**32 - 977 # Finite field prime
G_X = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798 # Generator X
G_Y = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8 # Generator Y

def inverse_mod(k: int, p: int) -> int:
    """Returns the modular inverse of k modulo p using Fermat's Little Theorem."""
    if k == 0:
        raise ZeroDivisionError('division by zero')
    if k < 0:
        return p - (-k % p)
    return pow(k, p - 2, p)

def point_add(p1: tuple, p2: tuple) -> tuple:
    """Adds two points on the elliptic curve."""
    if p1 is None: return p2
    if p2 is None: return p1
    
    x1, y1 = p1
    x2, y2 = p2
    
    if x1 == x2 and y1 != y2:
        return None # Point at infinity
        
    if x1 == x2:
        # Point doubling
        m = (3 * x1 * x1) * inverse_mod(2 * y1, P) % P
    else:
        # Point addition
        m = (y1 - y2) * inverse_mod(x1 - x2, P) % P
        
    x3 = (m * m - x1 - x2) % P
    y3 = (y1 + m * (x3 - x1)) % P
    
    return (x3, -y3 % P)

def scalar_multiply(k: int, point: tuple) -> tuple:
    """Multiplies a point on the curve by a scalar (the private key)."""
    result = None
    addend = point
    
    while k:
        if k & 1:
            result = point_add(result, addend)
        addend = point_add(addend, addend)
        k >>= 1
        
    return result

def get_public_key(private_key_hex: str, compressed: bool = True) -> str:
    """Derives the public key from a private key."""
    priv_key_int = int(private_key_hex, 16)
    
    # Multiply the Generator point by our private key
    pubkey_point = scalar_multiply(priv_key_int, (G_X, G_Y))
    pub_x, pub_y = pubkey_point
    
    if not compressed:
        # Uncompressed starts with 04 + X + Y
        return "04" + f"{pub_x:064x}" + f"{pub_y:064x}"
    
    # Compressed starts with 02 if Y is even, 03 if Y is odd + X
    prefix = "02" if pub_y % 2 == 0 else "03"
    return prefix + f"{pub_x:064x}"

if __name__ == "__main__":
    print("📈 Bitcoin SECP256k1 Public Key Derivation")
    print("-" * 65)
    
    # Example Private Key
    priv_key = "0c28fca386c7a227600b2fe50b7cae11ec86d3bf1fbe471be89827e19d72aa1d"
    
    uncompressed = get_public_key(priv_key, compressed=False)
    compressed = get_public_key(priv_key, compressed=True)
    
    print(f"Private Key : {priv_key}")
    print(f"Uncompressed: {uncompressed}")
    print(f"Compressed  : {compressed}")
    print("-" * 65)
    print("Notice how the compressed key is half the size! It only stores the X coordinate.")
