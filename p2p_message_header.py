"""
ChainSentry: P2P Message Header Serialization
Research Notes: Every message on the Bitcoin network starts with a 24-byte header.
"""
import hashlib

def create_message_header(magic_bytes: bytes, command: str, payload: bytes) -> bytes:
    # Command must be padded to 12 bytes
    cmd_bytes = command.encode('ascii').ljust(12, b'\x00')
    
    # Length of payload (4 bytes, little-endian)
    payload_len = len(payload).to_bytes(4, 'little')
    
    # Checksum: First 4 bytes of Double SHA256 of the payload
    checksum = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
    
    return magic_bytes + cmd_bytes + payload_len + checksum

if __name__ == "__main__":
    print("🌐 Bitcoin P2P Message Header Constructor")
    print("-" * 65)
    
    signet_magic = bytes.fromhex("0a03cf40")
    command_name = "inv"
    dummy_payload = bytes.fromhex("01000000") # 1 inventory item
    
    header = create_message_header(signet_magic, command_name, dummy_payload)
    print(f"Network Magic : {signet_magic.hex()}")
    print(f"Command       : {command_name}")
    print(f"24-Byte Header: {header.hex()}")
