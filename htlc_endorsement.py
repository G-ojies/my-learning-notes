"""
ChainSentry: Local Reputation and HTLC Endorsement
Research Notes: Mitigating jamming by requiring peers to build reputation before allocating liquidity slots.
"""
def evaluate_htlc_endorsement(peer_reputation: int, requested_amount: int):
    if peer_reputation < 50 and requested_amount < 1000:
        return "❌ Rejected: Untrusted peer attempting dust HTLC routing."
    return "✅ Endorsed: Peer has sufficient routing history."

if __name__ == "__main__":
    print(evaluate_htlc_endorsement(20, 500))
