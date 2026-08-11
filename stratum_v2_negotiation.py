"""
ChainSentry: Stratum V2 Job Negotiation
Research Notes: Allowing individual miners to construct their own block templates.
"""
def negotiate_block_template(miner_id: str, proposed_txs: list):
    """
    In Stratum V1, the pool dictates the block. In V2, the miner can propose 
    their own transaction set, increasing censorship resistance.
    """
    print(f"⛏️  Miner {miner_id} proposing custom block template with {len(proposed_txs)} TXs.")
    print(" -> Pool accepted Job Negotiation. Censorship resistance achieved!")
    return True

if __name__ == "__main__":
    negotiate_block_template("ASIC_Worker_01", ["tx_a", "tx_b", "tx_c"])
