"""
ChainSentry: UTXO Consolidation Economics
Research Notes: Calculating the optimal time to consolidate wallet fragments.
"""

def calculate_consolidation_savings(num_inputs: int, high_fee_rate: int, low_fee_rate: int) -> dict:
    """
    Calculates how many Satoshis are saved by consolidating UTXOs 
    during a low-fee weekend block vs a high-fee weekday spike.
    Assuming Native SegWit inputs (~68 vBytes each).
    """
    input_vbytes = num_inputs * 68
    base_tx_vbytes = 10.5 + 31 # overhead + 1 output
    
    total_vbytes = input_vbytes + base_tx_vbytes
    
    high_cost = total_vbytes * high_fee_rate
    low_cost = total_vbytes * low_fee_rate
    
    savings = high_cost - low_cost
    
    return {
        "UTXOs Consolidated": num_inputs,
        "Total Size": f"{total_vbytes} vB",
        "High Fee Cost": f"{high_cost} sats (@ {high_fee_rate} s/vB)",
        "Low Fee Cost": f"{low_cost} sats (@ {low_fee_rate} s/vB)",
        "Net Savings": f"{savings} sats"
    }

if __name__ == "__main__":
    print("📉 UTXO Consolidation Simulator")
    print("-" * 65)
    res = calculate_consolidation_savings(num_inputs=50, high_fee_rate=80, low_fee_rate=5)
    for k, v in res.items(): print(f"{k:<22}: {v}")
