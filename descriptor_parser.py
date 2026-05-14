"""
ChainSentry: Bitcoin Output Descriptor Parser
Research Notes: Standardizing how we define wallets (e.g., wpkh(xpub.../0/*))
"""
import re

def analyze_descriptor(descriptor: str) -> dict:
    """Parses standard output descriptors to determine script types."""
    if descriptor.startswith("wpkh("):
        script_type = "Native SegWit (P2WPKH)"
    elif descriptor.startswith("sh(wpkh("):
        script_type = "Nested SegWit (P2SH-P2WPKH)"
    elif descriptor.startswith("tr("):
        script_type = "Taproot (P2TR)"
    else:
        script_type = "Legacy or Custom Script"
        
    # Extract the derivation path if present
    path_match = re.search(r'/([0-9]+)/(\*)', descriptor)
    path = f"/{path_match.group(1)}/*" if path_match else "Hardcoded"
    
    return {"Type": script_type, "Derivation": path}

if __name__ == "__main__":
    print("📜 Output Descriptor Analyzer")
    desc = "wpkh([d34db33f/84'/0'/0']xpub6ERApnVw.../0/*)#c2n6j00g"
    for k, v in analyze_descriptor(desc).items(): print(f"{k}: {v}")
