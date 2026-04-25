"""
Bitcoin Miner Revenue Calculator
Research Notes: Total Block Reward = Subsidy + Mempool Fees.
"""
def calculate_block_revenue(block_height: int, total_fees_sats: int) -> float:
    halvings = block_height // 210000
    subsidy_sats = (50 * 100_000_000) >> halvings
    total_revenue_btc = (subsidy_sats + total_fees_sats) / 100_000_000
    return total_revenue_btc

if __name__ == "__main__":
    print(f"Block 840,000 Revenue: {calculate_block_revenue(840000, 45000000)} BTC")
