"""
Bitcoin Multisig Simulator
Research Notes: Understanding bare multisig (M-of-N) logic.
"""

def simulate_multisig(m: int, n: int, provided_sigs: int) -> bool:
    """
    Simulates OP_CHECKMULTISIG execution.
    Requires M valid signatures out of N possible public keys.
    """
    if provided_sigs < m:
        print(f"❌ Execution Failed: {provided_sigs} sigs provided, {m} required.")
        return False
    print(f"✅ Execution Passed: {m}-of-{n} Multisig unlocked successfully.")
    return True

if __name__ == "__main__":
    print("🔐 OP_CHECKMULTISIG Simulator")
    simulate_multisig(m=2, n=3, provided_sigs=1) # Fails
    simulate_multisig(m=2, n=3, provided_sigs=2) # Passes
