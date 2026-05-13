"""
ChainSentry: PSBT (Partially Signed Bitcoin Transaction) Decoder
Research Notes: How hardware wallets communicate unsigned transactions via Base64.
"""
import base64

def detect_psbt(base64_string: str) -> dict:
    """
    Decodes a Base64 PSBT string and checks for the magic bytes.
    Magic Bytes: 'psbt' followed by 0xff (0x70736274ff)
    """
    try:
        raw_bytes = base64.b64decode(base64_string)
    except Exception:
        return {"Error": "Invalid Base64 string."}
        
    # Check for magic bytes
    if raw_bytes[:5] == b'psbt\xff':
        return {
            "Valid PSBT": True,
            "Total Size": f"{len(raw_bytes)} bytes",
            "Message": "Ready for hardware wallet signing phase."
        }
    return {"Valid PSBT": False, "Message": "Missing magic bytes."}

if __name__ == "__main__":
    print("🛂 PSBT Magic Byte Detector")
    print("-" * 65)
    
    # A dummy PSBT string (Base64 encoded 'psbt\xff' + dummy data)
    dummy_psbt_b64 = "cHNidP8BAgMEBQ==" 
    
    for k, v in detect_psbt(dummy_psbt_b64).items():
        print(f"{k:<15}: {v}")
