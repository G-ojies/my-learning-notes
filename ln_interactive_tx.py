"""
ChainSentry v1.5.3: Lightning Dual-Funded Channel Constructor
Research Notes: BOLT protocol extension for interactive-tx negotiation allowing both peers to contribute capital.
"""
def construct_dual_funding_proposal(peer_a_contrib: int, peer_b_contrib: int, feerate: int) -> dict:
    total_capacity = peer_a_contrib + peer_b_contrib
    print(f"🤝 Dual-Funding Proposal Initialized:")
    print(f" -> Local Contribution : {peer_a_contrib} sats")
    print(f" -> Remote Contribution: {peer_b_contrib} sats")
    print(f" -> Total Capacity     : {total_capacity} sats @ {feerate} sat/vB")
    return {
        "capacity": total_capacity,
        "peer_a_balance": peer_a_contrib,
        "peer_b_balance": peer_b_contrib,
        "status": "Awaiting Interactive-Tx Collateral Signatures"
    }

if __name__ == "__main__":
    construct_dual_funding_proposal(500000, 500000, 15)
