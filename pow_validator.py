"""
Bitcoin Proof-of-Work (PoW) Validator
Research Notes: Hashing a block header and verifying it meets the difficulty target.
"""
import hashlib

def verify_proof_of_work(header_hex: str, target_int: int) -> bool:
    """
    Verifies that the double SHA-256 hash of the block header is less than the target.
    """
    if len(header_hex) != 160:
        print("Error: Block header must be exactly 80 bytes.")
        return False
        
    header_bytes = bytes.fromhex(header_hex)
    
    # 1. Double SHA-256 the 80-byte header
    first_hash = hashlib.sha256(header_bytes).digest()
    second_hash = hashlib.sha256(first_hash).digest()
    
    # 2. Reverse the bytes (Bitcoin hashes are little-endian internally)
    # and convert to a massive integer for mathematical comparison
    block_hash_int = int.from_bytes(second_hash[::-1], byteorder='big')
    
    print(f"Block Hash (Int): {block_hash_int}")
    print(f"Target     (Int): {target_int}")
    
    # 3. The golden rule of Bitcoin mining: Hash MUST be less than the Target
    return block_hash_int < target_int

if __name__ == "__main__":
    print("⚖️  Bitcoin Proof-of-Work Validator")
    print("-" * 65)
    
    # The Genesis Block Header
    genesis_header = (
        "01000000"
        "0000000000000000000000000000000000000000000000000000000000000000"
        "3ba3edfd7a7b12b27ac72c3e67768f617fc81bc3888a51323a9fb8aa4b1e5e4a"
        "29ab5f49"
        "ffff001d"
        "1dac2b7c"
    )
    
    # The target extracted from the 'ffff001d' bits in the Genesis Block
    genesis_target = 26959535291011309493156476344723991336010898738574164086137773096960
    
    is_valid = verify_proof_of_work(genesis_header, genesis_target)
    
    print("-" * 65)
    if is_valid:
        print("✅ SUCCESS: Block hash is valid and meets the difficulty target!")
    else:
        print("❌ FAILED: Block hash is greater than the target. Invalid PoW.")
