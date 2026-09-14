"""
ChainSentry v1.6.2: Route Blinding Constructor
Research Notes: Wrapping receiver details in encrypted blobs for the last routing hops.
"""
import hashlib

def generate_blinded_route(receiver_pubkey: str, introduction_node: str):
    blinded_blob = hashlib.sha256((receiver_pubkey + introduction_node).encode()).hexdigest()
    print(f"👻 Blinded Path Constructed via Introduction Node: {introduction_node}")
    print(f" -> Encrypted routing blob: {blinded_blob[:16]}...")
    return blinded_blob

if __name__ == "__main__":
    generate_blinded_route("03_receiver_secret", "02_intro_node")
