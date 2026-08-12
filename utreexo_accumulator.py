"""
ChainSentry: Utreexo UTXO State Minimization
Research Notes: Condensing the entire Bitcoin UTXO set into a few kilobytes using Merkle forests.
"""
import hashlib

def generate_utreexo_proof(utxo_set: list):
    """
    Mocking the dynamic accumulator where old UTXOs are deleted and 
    full nodes only store the roots of the Merkle forest.
    """
    root_hash = hashlib.sha256("".join(utxo_set).encode()).hexdigest()
    print(f"🌲 Utreexo Forest Root Computed: {root_hash[:16]}...")
    print(" -> Node RAM usage reduced from gigabytes to kilobytes!")

if __name__ == "__main__":
    generate_utreexo_proof(["utxo_1", "utxo_2", "utxo_3"])
