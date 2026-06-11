"""
ChainSentry: Whale Movement & Anomaly Detection
Research Notes: Flagging massive zero-conf transactions in the mempool.
"""

def analyze_transaction_anomaly(txid: str, inputs: list, outputs: list, current_fee_rate: float) -> dict:
    """
    Evaluates an unconfirmed transaction against ChainSentry's anomaly heuristics.
    """
    total_output_sats = sum(out['value'] for out in outputs)
    total_btc = total_output_sats / 100_000_000
    
    flags = []
    
    # Heuristic 1: Massive Value (Whale Movement)
    WHALE_THRESHOLD_BTC = 500.0 
    if total_btc >= WHALE_THRESHOLD_BTC:
        flags.append("🐋 WHALE ALERT: Massive volume transfer detected.")
        
    # Heuristic 2: Insanely High Fee Rate (Panic/Priority)
    if current_fee_rate > 500.0:
        flags.append("🔥 HIGH PRIORITY: Transaction paying extreme block space premium.")
        
    # Heuristic 3: Dust Attack (Massive outputs, tiny values)
    if len(outputs) > 100 and (total_output_sats / len(outputs)) < 1000:
        flags.append("🧹 DUST ANOMALY: Potential UTXO spam attack.")
        
    risk_level = "HIGH" if flags else "NORMAL"
    
    return {
        "TXID": txid,
        "Total Value": f"{total_btc:.2f} BTC",
        "Risk Level": risk_level,
        "Anomaly Flags": flags if flags else ["None"]
    }

if __name__ == "__main__":
    print("🚨 ChainSentry Anomaly Engine")
    print("-" * 65)
    
    mock_outputs = [{"value": 250_000_000_000}, {"value": 1_000_000_000}] # 2,510 BTC total
    res = analyze_transaction_anomaly("abc123def...", [], mock_outputs, current_fee_rate=12.5)
    
    for k, v in res.items():
        print(f"{k:<15}: {v}")
