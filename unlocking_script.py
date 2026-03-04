"""
Bitcoin Unlocking Script (ScriptSig) Builder
Research Notes: Combining a DER Signature and a Public Key to unlock a UTXO.
"""

def build_p2pkh_scriptsig(der_sig_hex: str, pubkey_hex: str) -> str:
    """
    Constructs a standard P2PKH ScriptSig.
    Format: [Sig Length] [DER Signature + SIGHASH] [PubKey Length] [Public Key]
    """
    # 1. Get the length of the signature in bytes (hex length / 2)
    sig_len_hex = hex(len(der_sig_hex) // 2)[2:].zfill(2)
    
    # 2. Get the length of the public key in bytes
    pubkey_len_hex = hex(len(pubkey_hex) // 2)[2:].zfill(2)
    
    # 3. Concatenate everything
    script_sig = f"{sig_len_hex}{der_sig_hex}{pubkey_len_hex}{pubkey_hex}"
    
    return script_sig

if __name__ == "__main__":
    print("🔑 Bitcoin ScriptSig Builder")
    print("-" * 65)
    
    # Example DER Signature (with 01 SIGHASH_ALL appended)
    der_sig = "304402206162636465666768696a6b6c6d6e6f707172737475767778797a3031323334350220363738396162636465666768696a6b6c6d6e6f707172737475767778797a303101"
    # Example Compressed Public Key
    pubkey = "0250863ad64a87ae8a2fe83c1af1a8403cb53f53e486d8511dad8a04887e5b2352"
    
    script_sig = build_p2pkh_scriptsig(der_sig, pubkey)
    
    print(f"DER Signature : {der_sig}")
    print(f"Public Key    : {pubkey}")
    print(f"\nFinal ScriptSig: {script_sig}")
