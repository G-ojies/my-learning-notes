"""
Bitcoin P2P Network: Ping & Pong Protocol
Research Notes: How nodes measure latency and keep connections alive.
"""
import struct
import os

def generate_ping_payload() -> bytes:
    """
    Generates an 8-byte random nonce for a ping message.
    """
    # os.urandom provides cryptographically secure random bytes
    return os.urandom(8)

def parse_ping_pong(payload_bytes: bytes, message_type: str) -> dict:
    """
    Parses the 8-byte payload of a ping or pong message.
    """
    if len(payload_bytes) != 8:
        return {"Error": f"Invalid {message_type} payload length. Must be exactly 8 bytes."}
        
    # Unpack the 8 bytes as an unsigned long long (little-endian)
    nonce = struct.unpack('<Q', payload_bytes)[0]
    
    return {
        "Message Type": message_type.upper(),
        "Raw Hex Payload": payload_bytes.hex(),
        "Decoded Nonce (Int)": nonce
    }

if __name__ == "__main__":
    print("🏓 Bitcoin P2P Heartbeat (Ping/Pong) Simulator")
    print("-" * 65)
    
    # Node A generates a ping
    ping_bytes = generate_ping_payload()
    ping_data = parse_ping_pong(ping_bytes, "ping")
    
    print("Node A sends:")
    for key, val in ping_data.items():
        print(f"  {key:<20}: {val}")
        
    print("\n" + "-" * 65 + "\n")
    
    # Node B receives the ping and MUST send the exact same bytes back as a pong
    pong_bytes = ping_bytes
    pong_data = parse_ping_pong(pong_bytes, "pong")
    
    print("Node B replies with:")
    for key, val in pong_data.items():
        print(f"  {key:<20}: {val}")
        
    print("-" * 65)
    
    if ping_data["Decoded Nonce (Int)"] == pong_data["Decoded Nonce (Int)"]:
        print("✅ SUCCESS: Nonces match! The connection is kept alive.")
    else:
        print("❌ FAILED: Nonces do not match. Node connection will be dropped.")
