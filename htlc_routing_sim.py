"""
Lightning Network: HTLC (Hashed Timelock Contract) Routing Simulator
Research Notes: How payments are trustlessly routed across multiple nodes.
"""
import hashlib
import time

def simulate_htlc_hop(node_name: str, payment_hash: str, secret: str = None, expiration: int = 0) -> str:
    """
    Simulates a node evaluating an incoming HTLC.
    """
    current_time = int(time.time())
    
    if current_time > expiration:
        return f"❌ [{node_name}] HTLC Expired! Reclaiming funds."
        
    if secret:
        # Verify the secret matches the hash
        calc_hash = hashlib.sha256(secret.encode('utf-8')).hexdigest()
        if calc_hash == payment_hash:
            return f"✅ [{node_name}] Secret validated! Funds unlocked and forwarded."
        return f"❌ [{node_name}] Invalid cryptographic secret provided."
        
    return f"⏳ [{node_name}] HTLC locked. Awaiting secret before block {expiration}..."

if __name__ == "__main__":
    print("⚡ Lightning Network HTLC Routing")
    print("-" * 65)
    
    # Alice wants to pay Carol through Bob
    preimage_secret = "chainsentry_super_secret_routing_key"
    payment_hash = hashlib.sha256(preimage_secret.encode('utf-8')).hexdigest()
    
    expiry_time = int(time.time()) + 3600 # 1 hour from now
    
    print(simulate_htlc_hop("Bob", payment_hash, expiration=expiry_time))
    print(simulate_htlc_hop("Carol", payment_hash, secret=preimage_secret, expiration=expiry_time))
