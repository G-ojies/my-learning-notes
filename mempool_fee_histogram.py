"""
ChainSentry v1.1.0: Mempool Fee Histogram Generator
Research Notes: Aggregating unconfirmed transactions into fee tiers for congestion visualization.
"""

def generate_fee_histogram(mempool_txs: list) -> dict:
    """
    Groups transactions into industry-standard fee brackets (sats/vB)
    and counts the total virtual size (vBytes) waiting in each tier.
    """
    # Define fee tiers: (min_fee, max_fee, label)
    tiers = [
        (0, 5, "1-5 sats/vB (Minimum/Eco)   "),
        (5, 15, "5-15 sats/vB (Low Priority) "),
        (15, 40, "15-40 sats/vB (Medium Pri)  "),
        (40, 100, "40-100 sats/vB (High Pri)   "),
        (100, float('inf'), "100+ sats/vB (Extreme/RBF)  ")
    ]
    
    histogram = {label: {"count": 0, "total_vsize": 0} for _, _, label in tiers}
    
    for tx in mempool_txs:
        rate = tx["fee_rate"]
        vsize = tx["vsize"]
        
        for low, high, label in tiers:
            if low <= rate < high:
                histogram[label]["count"] += 1
                histogram[label]["total_vsize"] += vsize
                break
                
    return histogram

def print_ascii_chart(histogram: dict):
    print("📊 Mempool Congestion Tier Distribution")
    print("-" * 65)
    
    for tier, data in histogram.items():
        vsize_kb = data["total_vsize"] / 1000
        # Create a basic ASCII bar representation (1 block per 50KB)
        blocks = "█" * int(vsize_kb / 50) if vsize_kb > 0 else ""
        print(f"{tier} | {data['count']:<4} txs | {vsize_kb:>6.2f} vKB {blocks}")

if __name__ == "__main__":
    # Mocking a live mempool state with varying traffic spikes
    mock_mempool = [
        {"txid": "tx1", "vsize": 250, "fee_rate": 2.5},
        {"txid": "tx2", "vsize": 180, "fee_rate": 12.0},
        {"txid": "tx3", "vsize": 500, "fee_rate": 25.5},
        {"txid": "tx4", "vsize": 120, "fee_rate": 85.0},
        {"txid": "tx5", "vsize": 300, "fee_rate": 140.0},
        {"txid": "tx6", "vsize": 1100, "fee_rate": 22.0},
        {"txid": "tx7", "vsize": 450, "fee_rate": 8.0},
        {"txid": "tx8", "vsize": 150, "fee_rate": 4.5},
    ]
    
    # Artificially inflate sizes for a clear visual chart
    for tx in mock_mempool:
        tx["vsize"] *= 400 
        
    hist_data = generate_fee_histogram(mock_mempool)
    print_ascii_chart(hist_data)
