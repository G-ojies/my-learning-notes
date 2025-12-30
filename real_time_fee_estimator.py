"""
ChainSentry Foundation: Mempool-Based Fee Estimation
Research Notes: Evaluating the immediate mempool landscape rather than just historical blocks.
"""
def estimate_next_block_fee(mempool_txs: list):
    """
    Sorts unconfirmed transactions by fee rate to project the lowest inclusion 
    threshold for the upcoming block template.
    """
    sorted_txs = sorted(mempool_txs, key=lambda x: x['feerate'], reverse=True)
    threshold_feerate = sorted_txs[-1]['feerate'] if sorted_txs else 1.0
    print(f"⏱️  Real-time Mempool Check: Minimum next-block inclusion is {threshold_feerate} sats/vB.")
    return threshold_feerate

if __name__ == "__main__":
    estimate_next_block_fee([{"feerate": 25}, {"feerate": 50}, {"feerate": 12}])
