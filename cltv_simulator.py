"""
Bitcoin OP_CHECKLOCKTIMEVERIFY (CLTV) Simulator
Research Notes: How Bitcoin enforces absolute timelocks in scripts.
"""
def simulate_cltv(tx_nlocktime: int, script_locktime: int) -> bool:
    """
    CLTV fails if the transaction's nLockTime is less than the script's specified locktime.
    """
    if tx_nlocktime < script_locktime:
        print(f"❌ Execution Failed: Tx Locktime ({tx_nlocktime}) < Script Requirement ({script_locktime})")
        return False
    print(f"✅ Execution Passed: UTXO can be spent at time/block {tx_nlocktime}")
    return True

if __name__ == "__main__":
    print("⏳ CLTV (Absolute Timelock) Simulator")
    simulate_cltv(tx_nlocktime=800000, script_locktime=800050) # Fails (Too early)
    simulate_cltv(tx_nlocktime=800100, script_locktime=800050) # Passes
