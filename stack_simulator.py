"""
Bitcoin Script Stack Machine Simulator
Research Notes: Simulating how miners validate a P2PKH transaction.
"""
import hashlib

def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()

def ripemd160(data: bytes) -> bytes:
    h = hashlib.new('ripemd160')
    h.update(data)
    return h.digest()

def hash160(data: bytes) -> bytes:
    return ripemd160(sha256(data))

def simulate_p2pkh(pubkey_hex: str, expected_hash160_hex: str) -> bool:
    """
    Simulates the stack execution of: OP_DUP OP_HASH160 <PubKeyHash> OP_EQUALVERIFY OP_CHECKSIG
    (Assuming the signature was already verified valid).
    """
    stack = []
    
    # 1. ScriptSig execution pushes the signature and public key onto the stack
    stack.append("signature_data") # Mocking the sig
    stack.append(bytes.fromhex(pubkey_hex))
    print(f"1. Stack after ScriptSig: [Sig, PubKey]")
    
    # 2. OP_DUP
    stack.append(stack[-1])
    print("2. OP_DUP executed: [Sig, PubKey, PubKey]")
    
    # 3. OP_HASH160
    top_item = stack.pop()
    hashed_pubkey = hash160(top_item)
    stack.append(hashed_pubkey)
    print(f"3. OP_HASH160 executed: [Sig, PubKey, {hashed_pubkey.hex()}]")
    
    # 4. Push Expected Hash160 (from ScriptPubKey)
    expected_bytes = bytes.fromhex(expected_hash160_hex)
    stack.append(expected_bytes)
    print(f"4. Expected Hash Pushed: [..., {hashed_pubkey.hex()}, {expected_bytes.hex()}]")
    
    # 5. OP_EQUALVERIFY
    item1 = stack.pop()
    item2 = stack.pop()
    if item1 != item2:
        print("❌ OP_EQUALVERIFY FAILED: Hashes do not match!")
        return False
    print("5. OP_EQUALVERIFY passed: Hashes match! Stack: [Sig, PubKey]")
    
    # 6. OP_CHECKSIG (We mock this returning True since we did the math in ecdsa_research.py)
    print("6. OP_CHECKSIG executed: Signature valid. Stack: [True]")
    return True

if __name__ == "__main__":
    print("💻 Bitcoin Stack Machine Simulator")
    print("-" * 65)
    
    test_pubkey = "0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352"
    test_expected_hash = hash160(bytes.fromhex(test_pubkey)).hex()
    
    result = simulate_p2pkh(test_pubkey, test_expected_hash)
    print("-" * 65)
    print(f"Final Result: {'VALID' if result else 'INVALID'} Transaction")
