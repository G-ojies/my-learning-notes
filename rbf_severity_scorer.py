"""
ChainSentry v1.1.0: RBF Severity Scorer
Research Notes: Dynamically adjusting RBF warning severity based on network fee averages.
"""

def calculate_rbf_severity(replacement_fee_rate: float, network_target_fee: float) -> dict:
    """
    Determines the intent behind an RBF transaction.
    If the replacement pays 3x the network rate, it is likely a malicious double-spend attempt.
    If it just matches the target fee, it is likely a benign fee-bump.
    """
    severity = "LOW"
    intent = "Benign Fee-Bump"
    
    # Heuristic thresholds for attack classification
    if replacement_fee_rate >= (network_target_fee * 3):
        severity = "CRITICAL"
        intent = "Aggressive Double-Spend Attempt"
    elif replacement_fee_rate >= (network_target_fee * 1.5):
        severity = "MEDIUM"
        intent = "Urgent Transaction Replacement"
        
    return {
        "Replacement Rate": f"{replacement_fee_rate} sats/vB",
        "Network Target": f"{network_target_fee} sats/vB",
        "Calculated Severity": severity,
        "Assumed Intent": intent
    }

if __name__ == "__main__":
    print("🚨 Dynamic RBF Severity Engine")
    print("-" * 65)
    
    # Scenario: Network needs 20 sats/vB to clear.
    # Attacker replaces a 5 sats/vB tx with a massive 80 sats/vB tx to jump the line.
    result = calculate_rbf_severity(replacement_fee_rate=80.0, network_target_fee=20.0)
    
    for k, v in result.items():
        print(f"{k:<20}: {v}")
        
    print("-" * 65)
    print("ChainSentry will use this logic to filter out noise and only trigger Webhooks for critical attacks!")
