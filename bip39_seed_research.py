"""
Bitcoin BIP39 Mnemonic to Seed Generator
Research Notes: How 12/24 English words are cryptographically stretched into a master seed.
"""
import hashlib
import binascii

def generate_seed_from_mnemonic(mnemonic: str, passphrase: str = "") -> str:
    """
    Converts a BIP39 mnemonic phrase into a 64-byte (512-bit) seed.
    
    Standard:
    - Algorithm: PBKDF2 (Password-Based Key Derivation Function 2)
    - Hash: HMAC-SHA512
    - Iterations: 2048
    - Salt: "mnemonic" + optional user passphrase
    """
    # Clean up the mnemonic just in case of extra spaces
    mnemonic = " ".join(mnemonic.split())
    
    # The salt is explicitly defined by the BIP39 standard
    salt = ("mnemonic" + passphrase).encode("utf-8")
    
    # Perform the 2048 rounds of HMAC-SHA512 stretching
    seed_bytes = hashlib.pbkdf2_hmac(
        hash_name="sha512",
        password=mnemonic.encode("utf-8"),
        salt=salt,
        iterations=2048
    )
    
    return seed_bytes.hex()

if __name__ == "__main__":
    print("🌱 Bitcoin BIP39 Mnemonic Seed Generator")
    print("-" * 65)
    
    # A standard test vector mnemonic (Do not use for real funds!)
    test_mnemonic = "legal winner thank year wave sausage worth useful recipe silver script ward"
    
    # Test 1: No passphrase (default)
    seed_no_passphrase = generate_seed_from_mnemonic(test_mnemonic)
    
    # Test 2: With a BIP39 passphrase (the "13th/25th word")
    seed_with_passphrase = generate_seed_from_mnemonic(test_mnemonic, passphrase="TREZOR_TEST_PASSWORD")
    
    print(f"Mnemonic Phrase: {test_mnemonic}\n")
    
    print(f"Seed (No Passphrase)  : \n{seed_no_passphrase}\n")
    print(f"Seed (With Passphrase): \n{seed_with_passphrase}")
    print("-" * 65)
    print("This 512-bit seed is the root of the entire HD (Hierarchical Deterministic) Wallet!")
