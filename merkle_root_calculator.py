"""
Bitcoin Merkle Root Calculator
Research Notes: How Bitcoin compresses thousands of TXIDs into a single 32-byte hash.
"""
import hashlib

def double_sha256(data: bytes) -> bytes:
    """Standard Bitcoin double SHA-256 hash."""
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()

def calculate_merkle_root(txid_list: list) -> str:
    """
    Calculates the Merkle Root from a list of TXIDs.
    Bitcoin requires TXIDs to be reversed to internal byte order before hashing!
    """
    if not txid_list:
        return ""
        
    # 1. Convert all TXIDs from hex to bytes AND reverse them (Little-Endian to Big-Endian)
    current_level = [bytes.fromhex(tx)[::-1] for tx in txid_list]
    
    # 2. Loop until only 1 hash remains (the Root)
    while len(current_level) > 1:
        next_level = []
        
        # If there is an odd number of hashes, duplicate the last one
        if len(current_level) % 2 != 0:
            current_level.append(current_level[-1])
            
        # Pair them up, concatenate, and double-hash
        for i in range(0, len(current_level), 2):
            left_node = current_level[i]
            right_node = current_level[i + 1]
            
            combined = left_node + right_node
            next_level.append(double_sha256(combined))
            
        current_level = next_level
        
    # 3. Reverse the final root back to display format (Little-Endian)
    merkle_root = current_level[0][::-1].hex()
    return merkle_root

if __name__ == "__main__":
    print("🌳 Bitcoin Merkle Root Calculator")
    print("-" * 65)
    
    # Example: 3 TXIDs (Notice how the 3rd will need to be duplicated to pair up!)
    txids = [
        "8c14f0bc3df8ab1b108b51259e8f4da129a0f44358ce5972844111394c86e089",
        "fff2525b8931402dd09222c50775608f75787bd2b87e56995a7bdd30f79702c4",
        "6359f0868171b1d194cbee1af2f16ea598ae8fad666d9b012c8ed2b79a236ec4"
    ]
    
    print("Input TXIDs:")
    for tx in txids:
        print(f"  - {tx}")
        
    root = calculate_merkle_root(txids)
    
    print("-" * 65)
    print(f"Calculated Merkle Root:\n{root}")
    print("\nThis single hash is what actually gets placed inside the 80-byte Block Header!")
