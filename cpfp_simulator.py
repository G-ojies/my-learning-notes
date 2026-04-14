"""
ChainSentry: Child Pays For Parent (CPFP) Simulator
Research Notes: How a receiver can rescue a stuck, low-fee transaction.
"""

def calculate_cpfp_rescue(parent_vbytes: int, parent_fee: int, child_vbytes: int, target_fee_rate: int) -> dict:
    """
    If a transaction is stuck in the mempool, the receiver can spend their 
    unconfirmed output into a NEW transaction with a massive fee. 
    Miners will calculate the "package fee" of both transactions together.
    """
    # Total size of both transactions combined
    package_vbytes = parent_vbytes + child_vbytes
    
    # What the miners actually want to earn to include the whole package
    required_package_fee = package_vbytes * target_fee_rate
    
    # What the child transaction MUST pay to subsidize the parent
    child_fee_needed = required_package_fee - parent_fee
    
    # Calculate the effective fee rate of the child on its own
    child_effective_rate = child_fee_needed / child_vbytes
    
    return {
        "Parent Tx Size": f"{parent_vbytes} vB",
        "Parent Tx Fee": f"{parent_fee} sats",
        "Target Package Rate": f"{target_fee_rate} sats/vB",
        "Child Fee Needed": f"{child_fee_needed} sats",
        "Child Effective Rate": f"{child_effective_rate:.1f} sats/vB"
    }

if __name__ == "__main__":
    print("🚑 CPFP (Child Pays For Parent) Rescue Simulator")
    print("-" * 65)
    
    # A parent tx is stuck paying only 2 sats/vB (250 vB * 2 = 500 sats)
    # The network is congested and we need 15 sats/vB to clear!
    rescue_plan = calculate_cpfp_rescue(
        parent_vbytes=250, 
        parent_fee=500, 
        child_vbytes=150, 
        target_fee_rate=15
    )
    
    print("Scenario: Rescuing a stuck 250vB transaction to hit 15 sats/vB.")
    for k, v in rescue_plan.items():
        print(f"  {k:<22}: {v}")
        
    print("-" * 65)
    print("Notice how the Child Tx has to pay a massive fee rate just to drag the Parent in!")
