"""
ChainSentry: Raw Transaction Broadcaster
Research Notes: Using the `sendrawtransaction` RPC to inject our PSBTs into the network.
"""
import json

def construct_broadcast_payload(signed_tx_hex: str) -> str:
    """
    Constructs the JSON-RPC payload to push a fully signed transaction to the local node.
    The node will then gossip it to the rest of the Signet network.
    """
    payload = {
        "jsonrpc": "1.0",
        "id": "chainsentry_broadcast",
        "method": "sendrawtransaction",
        "params": [signed_tx_hex]
    }
    return json.dumps(payload, indent=2)

if __name__ == "__main__":
    print("📡 ChainSentry Transaction Broadcaster")
    print("-" * 65)
    
    # Dummy signed hex
    dummy_hex = "0200000000010158e87a21b56daf0c23...00000000"
    
    print("Prepared RPC Payload for Node Injection:")
    print(construct_broadcast_payload(dummy_hex))
    print("-" * 65)
    print("If successful, the node returns the TXID. If it fails, it throws a mempool reject code (e.g., min relay fee not met)!")
