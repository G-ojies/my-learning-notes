"""
ChainSentry Foundation: Child Pays For Parent (CPFP)
Research Notes: Calculating the effective package feerate of an ancestor/descendant tree.
"""
def calculate_effective_feerate(parent_fee: int, parent_size: int, child_fee: int, child_size: int):
    total_fee = parent_fee + child_fee
    total_size = parent_size + child_size
    effective_rate = total_fee / total_size
    print(f"📦 Package Effective Feerate: {effective_rate:.2f} sats/vB")
    return effective_rate

if __name__ == "__main__":
    calculate_effective_feerate(150, 200, 5000, 150)
