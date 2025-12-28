"""
ChainSentry Foundation: Bitcoin Core Fee Estimation Algorithm
Research Notes: Simulating the exponential moving average decay for historical fee buckets.
"""
def apply_block_decay(historical_buckets: dict, decay_factor: float = 0.998):
    """
    Every time a block is found, historical fee tracking counters are multiplied 
    by 0.998, giving more weight to recent mempool activity (346-block half-life).
    """
    for bucket in historical_buckets:
        historical_buckets[bucket] *= decay_factor
    print("📉 Applied 0.998 exponential decay to historical fee buckets.")
    return historical_buckets

if __name__ == "__main__":
    apply_block_decay({"10_sats_vb": 500, "20_sats_vb": 150})
