"""
ChainSentry: Mempool Address Monitor (Blueprint)
Research Notes: Simulating real-time wallet activity detection for the ChainSentry backend.
"""
import time

def monitor_mempool(target_address: str, mock_tx_stream: list):
    """
    Simulates scanning incoming mempool transactions for a specific wallet address.
    """
    print(f"🛡️ ChainSentry Active: Monitoring mempool for {target_address}...")
    print("-" * 65)
    
    for tx in mock_tx_stream:
        # Simulate network latency
        time.sleep(0.5)
        
        # Check if our target address is receiving funds (in the outputs)
        if target_address in tx.get("outputs", []):
            print(f"🚨 ALERT (INFLOW): Unconfirmed Tx Detected!")
            print(f"   TXID  : {tx['txid']}")
            print(f"   Value : {tx['amount']} BTC\n")
            
        # Check if our target address is spending funds (in the inputs)
        elif target_address in tx.get("inputs", []):
             print(f"⚠️ ALERT (OUTFLOW): Wallet is spending!")
             print(f"   TXID  : {tx['txid']}")
             print(f"   Value : {tx['amount']} BTC\n")

if __name__ == "__main__":
    # Simulated mempool events
    mock_mempool = [
        {"txid": "abc123def...", "inputs": ["1SomeRandomAddress"], "outputs": ["3AnotherAddress"], "amount": 0.5},
        {"txid": "999888777...", "inputs": ["bc1q_external"], "outputs": ["bc1q_target_wallet"], "amount": 2.1}, # Match!
        {"txid": "444555666...", "inputs": ["bc1q_target_wallet"], "outputs": ["1ExchangeAddr"], "amount": 0.1}   # Match!
    ]
    
    monitor_mempool("bc1q_target_wallet", mock_mempool)
