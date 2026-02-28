"""
Bitcoin Timestamp & nLockTime Parser
Research Notes on how Bitcoin handles time and absolute timelocks.
"""
import struct
from datetime import datetime, timezone

def parse_bitcoin_time(hex_time_str: str, is_little_endian: bool = True) -> dict:
    """
    Parses a 4-byte Unix epoch time.
    Used in both Block Headers (Timestamp) and Transactions (nLockTime).
    """
    if len(hex_time_str) != 8:
        return {"Error": "Time/Locktime must be exactly 4 bytes (8 hex characters)."}
        
    time_bytes = bytes.fromhex(hex_time_str)
    
    # Unpack the 4 bytes into an integer
    if is_little_endian:
        epoch_time = struct.unpack('<I', time_bytes)[0]
    else:
        epoch_time = struct.unpack('>I', time_bytes)[0]
        
    # In Bitcoin, an nLockTime under 500,000 is interpreted as a Block Height,
    # not a Unix timestamp.
    if epoch_time < 500_000 and epoch_time > 0:
        return {
            "Raw Integer": epoch_time,
            "Type": "Block Height Lock",
            "Meaning": f"Locked until Block #{epoch_time}"
        }
    elif epoch_time == 0:
        return {
            "Raw Integer": epoch_time,
            "Type": "Disabled",
            "Meaning": "Transaction is final immediately."
        }
    else:
        # Convert Unix epoch to human-readable UTC time
        utc_time = datetime.fromtimestamp(epoch_time, timezone.utc)
        return {
            "Raw Integer": epoch_time,
            "Type": "Unix Timestamp",
            "Meaning": utc_time.strftime('%Y-%m-%d %H:%M:%S UTC')
        }

if __name__ == "__main__":
    print("⏳ Bitcoin Timestamp & Locktime Decoder")
    print("-" * 65)
    
    # Example 1: Block Header Timestamp (Little-Endian)
    block_time_hex = "29ab5f49" # Genesis Block Time
    print(f"Decoding Hex: {block_time_hex} (Genesis Block)")
    for k, v in parse_bitcoin_time(block_time_hex).items():
        print(f"  {k}: {v}")
    
    print("-" * 65)
    
    # Example 2: Transaction nLockTime representing a Block Height (e.g., Block 800,000)
    # 800,000 in hex is 0x0c3500. Little endian 4-byte: 00350c00
    lock_time_hex = "00350c00"
    print(f"Decoding Hex: {lock_time_hex} (nLockTime)")
    for k, v in parse_bitcoin_time(lock_time_hex).items():
        print(f"  {k}: {v}")
