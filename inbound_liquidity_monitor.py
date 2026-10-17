"""
ChainSentry v1.8.1: Inbound Liquidity Heuristics
Research Notes: Tracking channel balance distribution to prevent unpayable invoice states.
"""
def check_inbound_capacity(local_balance: int, remote_balance: int) -> str:
    total_capacity = local_balance + remote_balance
    inbound_ratio = remote_balance / total_capacity if total_capacity > 0 else 0
    
    if inbound_ratio < 0.15:
        print("⚠️ Warning: Inbound liquidity critically low! Node cannot receive external payments.")
        return "Needs Splicing or Loop-In"
    print("✅ Inbound liquidity healthy.")
    return "Optimal"

if __name__ == "__main__":
    check_inbound_capacity(950000, 50000)
