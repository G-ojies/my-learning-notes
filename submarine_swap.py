"""
ChainSentry v1.7.0: Submarine Swap Hashlock Simulator
Research Notes: Transferring mainchain BTC into Lightning without trusting a custodian.
"""
import hashlib
import secrets

def create_htlc_hashlock():
    secret = secrets.token_hex(32)
    hashlock = hashlib.sha256(secret.encode()).hexdigest()
    print("🔄 Submarine Swap Initiated")
    print(f" -> Secret generated (keep hidden!): {secret[:12]}...")
    print(f" -> Hashlock (shared condition): {hashlock[:20]}...")
    print(" -> Revealing the secret to claim one payment makes it available to claim the other!")
    return hashlock

if __name__ == "__main__":
    create_htlc_hashlock()
