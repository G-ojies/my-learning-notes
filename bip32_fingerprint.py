"""
Bitcoin BIP32 Parent Fingerprint Calculator
Research Notes: Calculating the 4-byte fingerprint used to link child keys to their parents.
"""
import hashlib

def hash160(data: bytes) -> bytes:
    """Standard RIPEMD160(SHA256(data))"""
    sha256_hash = hashlib.sha256(data).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_hash)
    return ripemd160.digest()

def get_parent_fingerprint(parent_pubkey_hex: str) -> str:
    """
    The fingerprint is simply the first 4 bytes of the parent's Hash160.
    """
    pubkey_bytes = bytes.fromhex(parent_pubkey_hex)
    
    # 1. Hash160 the public key
    identifier = hash160(pubkey_bytes)
    
    # 2. Slice the first 4 bytes
    fingerprint = identifier[:4]
    
    return fingerprint.hex()

if __name__ == "__main__":
    print("🧬 BIP32 Parent Fingerprint Extractor")
    print("-" * 65)
    
    # Example Compressed Public Key
    pubkey = "0339a36013301597daef41fbe593a02cc513d0b55527ec2df1050e2e8ff49c85c2"
    
    fingerprint = get_parent_fingerprint(pubkey)
    
    print(f"Parent Public Key: {pubkey}")
    print(f"4-Byte Fingerprint: {fingerprint}")
    print("-" * 65)
    print("This 4-byte hex is embedded into every extended child key (xpub/xprv)!")
