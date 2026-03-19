"""
Bitcoin Block Subsidy Halving Math
Research Notes: Using right bit-shifts to calculate block rewards.
"""
def get_block_subsidy(block_height: int) -> int:
    INITIAL_SUBSIDY = 50 * 100_000_000 # 50 BTC in Satoshis
    halvings = block_height // 210000
    
    # Bitcoin reward goes to 0 after 64 halvings
    if halvings >= 64: return 0
    
    # Right bit-shift represents dividing by 2
    return INITIAL_SUBSIDY >> halvings
