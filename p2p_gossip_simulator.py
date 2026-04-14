"""
ChainSentry: P2P Network Gossip Protocol
Research Notes: Simulating how nodes exchange mempool transactions via inv/getdata/tx.
"""

# Standard Bitcoin protocol inventory types
MSG_TX = 1
MSG_BLOCK = 2
MSG_WITNESS_TX = 0x40000001

def simulate_tx_relay(node_a_mempool: set, node_b_mempool: set, new_txid: str, tx_hex: str):
    """
    Simulates the standard 3-step Bitcoin transaction relay protocol.
    """
    print("📡 Initiating P2P Transaction Relay Protocol")
    print("-" * 65)
    
    # Node A receives a new transaction locally
    node_a_mempool.add(new_txid)
    print(f"[Node A] Received new local TX: {new_txid[:8]}...")
    
    # STEP 1: Node A sends an 'inv' (Inventory) message to Node B
    print(f"\n> Step 1: [Node A] sends 'inv' (Inventory) message")
    inv_payload = {"type": MSG_TX, "hash": new_txid}
    print(f"   Payload: {inv_payload}")
    
    # Node B checks if it already has this transaction
    if new_txid in node_b_mempool:
        print(f"\n> Step 2: [Node B] ignores. Already in mempool.")
        return
        
    # STEP 2: Node B sends a 'getdata' message requesting the full transaction
    print(f"\n> Step 2: [Node B] sends 'getdata' message")
    getdata_payload = {"type": MSG_TX, "hash": new_txid}
    print(f"   Payload: {getdata_payload}")
    
    # STEP 3: Node A responds with the full 'tx' message
    print(f"\n> Step 3: [Node A] sends 'tx' message")
    tx_payload = {"txid": new_txid, "raw": tx_hex}
    print(f"   Payload: Full raw transaction ({len(tx_hex) // 2} bytes)")
    
    # Node B validates and adds to its mempool
    node_b_mempool.add(new_txid)
    print(f"\n✅ [Node B] Validated and added TX to mempool!")

if __name__ == "__main__":
    node_alpha_pool = set()
    node_beta_pool = set()
    
    dummy_txid = "a1b2c3d4e5f607890123456789abcdefa1b2c3d4e5f607890123456789abcdef"
    dummy_raw_tx = "0200000001" + "00"*32 + "ffffffff00ffffffff01" + "00"*8 + "00000000"
    
    simulate_tx_relay(node_alpha_pool, node_beta_pool, dummy_txid, dummy_raw_tx)
    
    print("-" * 65)
    print("This bandwidth-saving handshake is how the Bitcoin network scales globally!")
