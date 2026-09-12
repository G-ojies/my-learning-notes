"""
ChainSentry: Gossip Spam Mitigation
Research Notes: Preventing malicious nodes from flooding the network with fake routing updates.
"""
def enforce_gossip_limits(node_id: str, message_count: int, timeframe_sec: int):
    rate = message_count / timeframe_sec
    if rate > 0.1:  # More than 1 message per 10 seconds
        print(f"🛑 RATE LIMIT EXCEEDED: Node {node_id} is spamming the gossip network!")
        return False
    return True
