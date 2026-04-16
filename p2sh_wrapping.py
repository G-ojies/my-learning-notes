"""
Bitcoin P2SH (Pay-to-Script-Hash) Wrapper
Research Notes: Hiding complex scripts (like multisig) behind a standard 3... address.
"""
import hashlib

def wrap_in_p2sh(redeem_script_hex: str) -> str:
    """
    Hashes the complex redeem script using HASH160.
    The sender only needs to pay to this hash, keeping the UTXO small.
    """
    script_bytes = bytes.fromhex(redeem_script_hex)
    sha256_hash = hashlib.sha256(script_bytes).digest()
    ripemd160 = hashlib.new('ripemd160')
    ripemd160.update(sha256_hash)
    
    script_hash = ripemd160.hexdigest()
    return f"OP_HASH160 {script_hash} OP_EQUAL"

if __name__ == "__main__":
    # Dummy 2-of-3 multisig script
    dummy_redeem_script = "522102...2103...2102...53ae"
    print(f"ScriptPubKey: {wrap_in_p2sh(dummy_redeem_script)}")
