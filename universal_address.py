"""
Bitcoin Universal Address Classifier
Research Notes: Quickly identifying address types based on prefixes.
"""
def classify_address(address: str) -> str:
    if address.startswith("1"): return "Legacy P2PKH"
    elif address.startswith("3"): return "Nested SegWit P2SH"
    elif address.startswith("bc1q") and len(address) == 42: return "Native SegWit P2WPKH"
    elif address.startswith("bc1q") and len(address) == 62: return "Native SegWit P2WSH"
    elif address.startswith("bc1p"): return "Taproot P2TR"
    else: return "Unknown / Testnet"

if __name__ == "__main__":
    print(f"Address type: {classify_address('bc1qar0srrr7xfkvy5l643lydnw9re59gtzzwf5mdq')}")
