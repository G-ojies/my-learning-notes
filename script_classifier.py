"""
Bitcoin ScriptPubKey Classifier
Research Notes on locking script patterns for Chain Lens.
"""

def classify_script(hex_str: str) -> str:
    """
    Identifies the type of Bitcoin address/script from its raw hex.
    
    Patterns:
    - P2PKH: OP_DUP OP_HASH160 <20-byte-hash> OP_EQUALVERIFY OP_CHECKSIG
             Hex: 76 a9 14 <20 bytes> 88 ac (Total 50 chars / 25 bytes)
    - P2SH:  OP_HASH160 <20-byte-hash> OP_EQUAL
             Hex: a9 14 <20 bytes> 87 (Total 46 chars / 23 bytes)
    - Native SegWit (v0 P2WPKH): OP_0 <20-byte-hash>
             Hex: 00 14 <20 bytes> (Total 44 chars / 22 bytes)
    - Native SegWit (v0 P2WSH):  OP_0 <32-byte-hash>
             Hex: 00 20 <32 bytes> (Total 68 chars / 34 bytes)
    - Taproot (v1 P2TR):         OP_1 <32-byte-key>
             Hex: 51 20 <32 bytes> (Total 68 chars / 34 bytes)
    - OP_RETURN: OP_RETURN <data>
             Hex: 6a <length> <data>
    """
    if not hex_str:
        return "unknown"
        
    if hex_str.startswith('76a914') and hex_str.endswith('88ac') and len(hex_str) == 50:
        return "Legacy P2PKH (Pay-to-Public-Key-Hash)"
        
    if hex_str.startswith('a914') and hex_str.endswith('87') and len(hex_str) == 46:
        return "Legacy P2SH (Pay-to-Script-Hash)"
        
    if hex_str.startswith('0014') and len(hex_str) == 44:
        return "SegWit P2WPKH (Pay-to-Witness-Public-Key-Hash)"
        
    if hex_str.startswith('0020') and len(hex_str) == 68:
        return "SegWit P2WSH (Pay-to-Witness-Script-Hash)"
        
    if hex_str.startswith('5120') and len(hex_str) == 68:
        return "Taproot P2TR (Pay-to-Taproot)"
        
    if hex_str.startswith('6a'):
        return "OP_RETURN (Provably Unspendable Data)"
        
    return "Unknown/Non-Standard Script"

if __name__ == "__main__":
    print("🔍 Testing Bitcoin Script Classifier:")
    print("-" * 50)
    
    test_scripts = [
        "76a91489abcdef0123456789abcdef0123456789abcdef88ac", # P2PKH
        "001489abcdef0123456789abcdef0123456789abcdef",       # P2WPKH
        "512089abcdef0123456789abcdef0123456789abcdef0123456789abcdef012345", # Taproot
        "6a08736f622d32303236",                               # OP_RETURN
    ]
    
    for script in test_scripts:
        print(f"Hex:   {script[:16]}...")
        print(f"Type:  {classify_script(script)}\n")
