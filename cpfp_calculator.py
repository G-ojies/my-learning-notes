"""
ChainSentry v1.1.0: CPFP (Child Pays For Parent) Balance Estimator
Research Notes: Evaluating the combined effective fee rate of dependent tx packages.
"""

def calculate_package_fee_rate(parent_fee: int, parent_vsize: int, child_fee: int, child_vsize: int) -> float:
    """
    Calculates the aggregate package fee rate. Miners evaluate transaction packages 
    together if the child spends an unconfirmed output from the unconfirmed parent.
    """
    total_fees = parent_fee + child_fee
    total_vsize = parent_vsize + child_vsize
    return round(total_fees / total_vsize, 2)

if __name__ == "__main__":
    print("📈 Child Pays For Parent (CPFP) Package Monitor")
    print("-" * 65)
    
    # Parent is stuck: low fee
    p_fee, p_size = 500, 140
    # Child bumps it: high fee
    c_fee, c_size = 8500, 110
    
    effective_rate = calculate_package_fee_rate(p_fee, p_size, c_fee, c_size)
    print(f"Parent Fee Rate    : {round(p_fee/p_size, 2)} sats/vB (Stuck in mempool)")
    print(f"Effective Package Rate: {effective_rate} sats/vB (Miner incentives unlocked!)")
