"""
Bitcoin P2P Network Message Header
Research Notes: The 24-byte header attached to every network message.
"""
import struct

def parse_p2p_header(header_hex: str):
    b = bytes.fromhex(header_hex)
    return {
        "Magic Bytes": b[:4].hex(), # e.g., f9beb4d9 for Mainnet
        "Command": b[4:16].replace(b'\x00', b'').decode('ascii'),
        "Payload Length": struct.unpack('<I', b[16:20])[0],
        "Checksum": b[20:24].hex()
    }
