"""
ChainSentry: Taproot Leaf Node Calculator
Research Notes: Hashing individual scripts for a MAST (Merkelized Alternative Script Tree).
"""
import hashlib

def tagged_hash(tag: str, data: bytes) -> bytes:
    """BIP 340 tagged hash: SHA256(SHA256(tag) || SHA256(tag) || data)"""
    tag_hash = hashlib.sha256(tag.encode('utf-8')).digest()
    return hashlib.sha256(tag_hash + tag_hash + data).digest()

def calc_tapleaf_hash(script_hex: str, leaf_version: bytes = b'\xc0') -> str:
    """
    Calculates the TapLeaf hash as defined in BIP 341.
    Tag = "TapLeaf"
    Data = leaf_version || compact_size(script) || script
    """
    script_bytes = bytes.fromhex(script_hex)
    
    # Simplified for research: assuming script is < 252 bytes so length fits in 1 byte
    script_len = len(script_bytes).to_bytes(1, 'little')
    
    payload = leaf_version + script_len + script_bytes
    
    return tagged_hash("TapLeaf", payload).hex()

if __name__ == "__main__":
    print("🌳 Taproot MAST Leaf Calculator (BIP 341)")
    print("-" * 65)
    
    # Dummy script: OP_CHECKSIG (ac)
    mock_script = "ac"
    leaf_hash = calc_tapleaf_hash(mock_script)
    
    print(f"Script (Hex)  : {mock_script}")
    print(f"TapLeaf Hash  : {leaf_hash}")
    print("-" * 65)
    print("This hash becomes a leaf in the Taproot Merkle Tree, keeping complex smart contracts highly private!")
