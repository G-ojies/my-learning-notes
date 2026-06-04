"""
ChainSentry: Mempool Eviction Simulator
Research Notes: How Bitcoin Core drops transactions when the default 300MB RAM limit is reached.
"""

def simulate_eviction(mempool_txs: list, max_capacity: int) -> list:
    """
    Simulates node mempool limits. When full, transactions with the lowest 
    fee rate (sats/vB) are evicted entirely.
    """
    # Sort transactions by fee rate (lowest first)
    sorted_mempool = sorted(mempool_txs, key=lambda tx: tx['fee_rate'])
    
    current_size = sum(tx['size'] for tx in sorted_mempool)
    evicted = []
    
    print(f"Current Mempool Size: {current_size} vB | Max Capacity: {max_capacity} vB\n")
    
    # Evict until we are under the memory limit
    while current_size > max_capacity and sorted_mempool:
        dropped_tx = sorted_mempool.pop(0) # Remove lowest fee rate
        evicted.append(dropped_tx)
        current_size -= dropped_tx['size']
        print(f"🗑️ Evicted TX: {dropped_tx['txid']} (Fee Rate: {dropped_tx['fee_rate']} sats/vB)")
        
    return sorted_mempool

if __name__ == "__main__":
    print("🌊 Node Mempool Eviction Protocol")
    print("-" * 65)
    
    mock_mempool = [
        {"txid": "tx_alpha", "size": 250, "fee_rate": 1.2},
        {"txid": "tx_beta",  "size": 180, "fee_rate": 5.0},
        {"txid": "tx_gamma", "size": 300, "fee_rate": 1.0} # Target for eviction
    ]
    
    # Set a tiny max capacity of 500 vB to force an eviction
    simulate_eviction(mock_mempool, max_capacity=500)
