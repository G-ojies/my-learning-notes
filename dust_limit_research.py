"""
ChainSentry: Bitcoin Dust Limit Calculator
Research Notes: Why the mempool rejects tiny transactions to prevent spam.
"""

def calculate_dust_limit(is_segwit: bool, dust_relay_fee_rate: int = 3) -> dict:
    """
    Bitcoin Core considers an output "dust" if the fee required to spend it 
    costs more than ~1/3 of the output's value.
    
    Standard Sizes:
    - Legacy P2PKH Input: ~148 bytes, Output: 34 bytes
    - SegWit P2WPKH Input: ~68 vbytes, Output: 31 vbytes
    """
    if is_segwit:
        input_size = 68
        output_size = 31
    else:
        input_size = 148
        output_size = 34
        
    # Total bytes required to create and then spend this output
    total_lifecycle_bytes = input_size + output_size
    
    # The dust limit threshold in Satoshis
    dust_threshold = total_lifecycle_bytes * dust_relay_fee_rate
    
    return {
        "Type": "Native SegWit (P2WPKH)" if is_segwit else "Legacy (P2PKH)",
        "Lifecycle Size": f"{total_lifecycle_bytes} bytes",
        "Dust Relay Rate": f"{dust_relay_fee_rate} sats/byte",
        "Dust Limit Threshold": f"{dust_threshold} Satoshis"
    }

if __name__ == "__main__":
    print("🧹 Bitcoin Mempool Dust Limit Calculator")
    print("-" * 65)
    
    legacy_dust = calculate_dust_limit(is_segwit=False)
    segwit_dust = calculate_dust_limit(is_segwit=True)
    
    print("Legacy P2PKH:")
    for k, v in legacy_dust.items(): print(f"  {k:<20}: {v}")
    
    print("\nNative SegWit:")
    for k, v in segwit_dust.items(): print(f"  {k:<20}: {v}")
    
    print("-" * 65)
    print("Any output smaller than this threshold will be REJECTED by nodes as spam!")
