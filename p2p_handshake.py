"""
ChainSentry: P2P Network Handshake (version/verack)
Research Notes: Establishing the initial connection with a Bitcoin Core node.
"""
def build_version_payload(my_ip: str, node_ip: str, user_agent: str="/ChainSentry:1.1.0/") -> dict:
    return {
        "version": 70016,
        "services": 0, # NODE_NONE (We don't provide blocks)
        "timestamp": 1650000000,
        "addr_recv": node_ip,
        "addr_from": my_ip,
        "nonce": 841203948123,
        "user_agent": user_agent,
        "start_height": 800000,
        "relay": True
    }
