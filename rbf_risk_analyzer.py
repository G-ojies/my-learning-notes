"""
ChainSentry: Zero-Conf RBF Risk Analyzer
Research Notes: Detecting BIP125 Replace-By-Fee signaling to prevent double-spend attacks.
"""

def analyze_rbf_risk(tx_inputs: list) -> dict:
    """
    Checks the 'sequence' field of every input in an unconfirmed transaction.
    If ANY input signals RBF (sequence < 0xffffffff - 1), the entire tx is replaceable.
    """
    is_replaceable = False
    flagged_inputs = []
    
    # BIP125 RBF Opt-in threshold
    RBF_THRESHOLD = 0xffffffff - 1
    
    for idx, sequence_hex in enumerate(tx_inputs):
        # Convert the hex sequence to an integer
        sequence_int = int(sequence_hex, 16)
        
        if sequence_int <= RBF_THRESHOLD:
            is_replaceable = True
            flagged_inputs.append(idx)
            
    risk_level = "CRITICAL" if is_replaceable else "LOW"
    action = "DO NOT TRUST UNTIL CONFIRMED" if is_replaceable else "SAFE FOR ZERO-CONF"
    
    return {
        "Risk Level": risk_level,
        "Is Replaceable (BIP125)": is_replaceable,
        "Flagged Input Indices": flagged_inputs,
        "Recommended Action": action
    }

if __name__ == "__main__":
    print("🚨 ChainSentry RBF Double-Spend Analyzer")
    print("-" * 65)
    
    # Example 1: Standard non-replaceable transaction (Sequence = ffffffff)
    safe_tx_inputs = ["ffffffff", "ffffffff"]
    
    # Example 2: Attacker transaction signaling RBF (Sequence = fdffffff)
    attacker_tx_inputs = ["ffffffff", "fdffffff"]
    
    print("Testing Safe Transaction:")
    for k, v in analyze_rbf_risk(safe_tx_inputs).items():
        print(f"  {k}: {v}")
        
    print("\nTesting Attacker Transaction:")
    for k, v in analyze_rbf_risk(attacker_tx_inputs).items():
        print(f"  {k}: {v}")
    
    print("-" * 65)
    print("ChainSentry must instantly flag any RBF transactions to protect users!")
