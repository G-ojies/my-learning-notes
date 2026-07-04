"""
ChainSentry v1.2.0: CoinJoin Anomaly Filter
"""
def is_coinjoin(outputs: list) -> bool:
    """Detects WabiSabi/Whirlpool by checking for many equal-value outputs."""
    values = [out['value'] for out in outputs]
    return len(values) > 5 and len(set(values)) == 1 # All outputs are identical
