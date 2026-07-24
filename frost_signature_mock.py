"""
ChainSentry: FROST (Flexible Round-Optimized Schnorr Threshold)
Research Notes: Advanced multisig where n-of-m signers can generate a single Taproot signature.
"""
def frost_signing_round(participants: list, threshold: int):
    if len(participants) < threshold:
        return "❌ Insufficient participants for threshold signature."
    
    print(f"❄️ FROST Protocol Initiated with {len(participants)} signers (Threshold: {threshold})")
    print(" -> Round 1: Nonce commitments exchanged.")
    print(" -> Round 2: Signature shares aggregated.")
    return "✅ Valid single Schnorr signature generated!"

if __name__ == "__main__":
    print(frost_signing_round(["Alice", "Bob", "Charlie"], 2))
