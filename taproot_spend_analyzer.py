"""
ChainSentry v1.5.2: Taproot Spend Path Analyzer
Research Notes: Detecting whether a P2TR output was spent via Key Path (default) or Script Path (complex logic).
"""
def analyze_p2tr_spend(witness_stack: list) -> str:
    """
    If a Taproot output is spent via Key Path, the witness stack contains exactly one element (the signature).
    If spent via Script Path, it contains multiple elements (script inputs, the script itself, and the control block).
    """
    if len(witness_stack) == 1:
        return "🔑 Key Path Spend detected. Looks like a standard single-sig transaction!"
    elif len(witness_stack) > 1:
        return "📜 Script Path Spend detected. Executing hidden smart contract logic (e.g., multisig or timelock)."
    return "❌ Invalid Witness"

if __name__ == "__main__":
    print("🔍 Taproot (BIP 341) Spend Path Monitor")
    print("-" * 65)
    print(analyze_p2tr_spend(["signature_only"]))
    print(analyze_p2tr_spend(["sig1", "sig2", "multisig_script", "control_block"]))
