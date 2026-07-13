"""
ChainSentry: Silent Payments (BIP352)
Research Notes: Reusable static addresses that generate unique on-chain outputs without interaction.
"""
import hashlib

def generate_stealth_address(scan_key: str, spend_key: str, shared_secret: str) -> str:
    """
    Simulates the ECDH shared secret derivation for non-interactive stealth addresses.
    """
    tweak = hashlib.sha256(shared_secret.encode('utf-8')).hexdigest()
    print(f"🤫 Derived unique on-chain output using tweak: {tweak[:16]}...")
    return f"bc1p_stealth_{tweak[:8]}"

if __name__ == "__main__":
    print(generate_stealth_address("scan_pub", "spend_pub", "ecdh_secret_123"))
