"""
Bitcoin Transaction Fee Estimator
Research Notes: Calculating bytes, vbytes, and miner fees for transactions.
"""

def estimate_tx_fees(num_inputs: int, num_outputs: int, fee_rate_sats_per_vbyte: int, is_segwit: bool = False) -> dict:
    """
    Estimates the size and fee of a standard Bitcoin transaction.
    Legacy Tx: Size = (Inputs * 148) + (Outputs * 34) + 10 (overhead)
    SegWit Tx: Size = (Inputs * 68) + (Outputs * 31) + 10 (overhead)
    """
    if is_segwit:
        # Native SegWit P2WPKH
        estimated_vbytes = (num_inputs * 68) + (num_outputs * 31) + 10.5
    else:
        # Legacy P2PKH
        estimated_vbytes = (num_inputs * 148) + (num_outputs * 34) + 10
        
    estimated_vbytes = int(estimated_vbytes)
    total_fee_sats = estimated_vbytes * fee_rate_sats_per_vbyte
    total_fee_btc = total_fee_sats / 100_000_000
    
    return {
        "Inputs": num_inputs,
        "Outputs": num_outputs,
        "Is SegWit": is_segwit,
        "Estimated Size (vB)": estimated_vbytes,
        "Fee Rate (sat/vB)": fee_rate_sats_per_vbyte,
        "Total Fee (Sats)": total_fee_sats,
        "Total Fee (BTC)": f"{total_fee_btc:.8f}"
    }

if __name__ == "__main__":
    print("💸 Bitcoin Transaction Fee Estimator")
    print("-" * 65)
    
    # Compare a Legacy vs SegWit transaction with 2 inputs and 2 outputs at 15 sats/vbyte
    legacy_tx = estimate_tx_fees(2, 2, 15, is_segwit=False)
    segwit_tx = estimate_tx_fees(2, 2, 15, is_segwit=True)
    
    print("Legacy P2PKH:")
    for k, v in legacy_tx.items(): print(f"  {k}: {v}")
    
    print("\nNative SegWit P2WPKH:")
    for k, v in segwit_tx.items(): print(f"  {k}: {v}")
    
    savings = legacy_tx["Total Fee (Sats)"] - segwit_tx["Total Fee (Sats)"]
    print("-" * 65)
    print(f"SegWit saves you {savings} Satoshis on this transaction!")
