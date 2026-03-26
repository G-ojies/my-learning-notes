"""
Bitcoin Bech32 / Native SegWit Address Notes
Research Notes: Understanding the human-readable part (HRP) and data payloads.
"""
def analyze_bech32_address(address: str) -> dict:
    if not address.startswith("bc1"):
        return {"Error": "Not a mainnet Native SegWit address"}
        
    hrp, data = address.split('1', 1)
    # The first character of the data part indicates the SegWit version (q = v0, p = v1/Taproot)
    version_char = data[0]
    
    version = 0 if version_char == 'q' else (1 if version_char == 'p' else "Unknown")
    
    return {
        "HRP (Network)": hrp,
        "Witness Version": version,
        "Data Payload Length": len(data) - 1
    }

if __name__ == "__main__":
    print(analyze_bech32_address("bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq"))
