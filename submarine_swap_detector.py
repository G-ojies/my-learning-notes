"""
ChainSentry v1.1.0: Submarine Swap Detector
Research Notes: Identifying on-chain HTLCs used for Layer 1 to Layer 2 atomic swaps.
"""

def detect_submarine_swap(script_pubkey_asm: str) -> dict:
    """
    Submarine swaps rely on HTLCs to ensure funds are not stolen during the L1/L2 transfer.
    We scan the raw Script assembly for the cryptographic hashlock and the timelock branches.
    """
    # Heuristics for finding a standard HTLC pattern
    has_hashlock = "OP_HASH160" in script_pubkey_asm and "OP_EQUALVERIFY" in script_pubkey_asm
    has_timelock = "OP_CHECKLOCKTIMEVERIFY" in script_pubkey_asm or "OP_CHECKSEQUENCEVERIFY" in script_pubkey_asm
    has_branches = "OP_IF" in script_pubkey_asm and "OP_ELSE" in script_pubkey_asm
    
    is_htlc = has_hashlock and has_timelock and has_branches
    
    return {
        "Script Type": "HTLC Contract" if is_htlc else "Standard Transfer",
        "Is Submarine Swap": is_htlc,
        "L2 Implications": "Atomic transfer to/from Lightning Network detected." if is_htlc else "None."
    }

if __name__ == "__main__":
    print("🌊 ChainSentry Submarine Swap Analyzer")
    print("-" * 65)
    
    # Example of a raw HTLC script translated to assembly
    mock_htlc_script = (
        "OP_HASH160 <Hash> OP_EQUALVERIFY "
        "OP_IF <PubKey_Alice> OP_CHECKSIG "
        "OP_ELSE <BlockHeight> OP_CHECKLOCKTIMEVERIFY OP_DROP <PubKey_Bob> OP_CHECKSIG OP_ENDIF"
    )
    
    result = detect_submarine_swap(mock_htlc_script)
    
    for key, val in result.items():
        print(f"{key:<20}: {val}")
        
    print("-" * 65)
    print("Detecting this allows ChainSentry to track liquidity moving off-chain in real-time!")
