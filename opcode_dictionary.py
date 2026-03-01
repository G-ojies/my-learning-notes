"""
Bitcoin Basic Opcode Dictionary
Research Notes: Mapping raw hex bytes to human-readable Script commands.
"""

# A small subset of common Bitcoin Opcodes
OPCODES = {
    0x00: "OP_0",
    0x51: "OP_1",
    0x6a: "OP_RETURN",
    0x76: "OP_DUP",
    0x87: "OP_EQUAL",
    0x88: "OP_EQUALVERIFY",
    0xa9: "OP_HASH160",
    0xac: "OP_CHECKSIG",
    0xad: "OP_CHECKMULTISIG",
}

def decode_simple_script(script_hex: str) -> list:
    """
    Decodes a raw script hex string into a list of readable OP_CODES.
    Note: This is a simplified version and doesn't handle OP_PUSH data lengths.
    """
    script_bytes = bytes.fromhex(script_hex)
    decoded_script = []
    
    for byte in script_bytes:
        if byte in OPCODES:
            decoded_script.append(OPCODES[byte])
        else:
            # If it's not a known opcode, it's likely pushing data (like a pubkey hash)
            decoded_script.append(f"<Data: 0x{byte:02x}...>")
            
    return decoded_script

if __name__ == "__main__":
    print("📜 Bitcoin Basic Script Decoder")
    print("-" * 65)
    
    # Standard P2PKH Locking Script
    # OP_DUP OP_HASH160 <20-byte-hash> OP_EQUALVERIFY OP_CHECKSIG
    # 76     a9         14 (push 20)   88             ac
    p2pkh_script_hex = "76a91489abcdef0123456789abcdef0123456789abcdef88ac"
    
    print(f"Raw Script: {p2pkh_script_hex}")
    print("Decoded   :")
    
    # We will just print the known opcodes for this simple dictionary test
    for byte in bytes.fromhex(p2pkh_script_hex):
        if byte in OPCODES:
            print(f"  {hex(byte)} -> {OPCODES[byte]}")
        elif byte == 0x14:
             print(f"  {hex(byte)} -> [Push 20 Bytes]")
