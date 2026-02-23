"""
Bitcoin SegWit Weight & vBytes Calculator
Research Notes on BIP141 Implementation
"""
import math

def calculate_tx_metrics(base_size: int, total_size: int):
    """
    Calculates Weight Units (WU) and vBytes for a Bitcoin transaction.
    
    According to BIP141:
    - Base data (legacy data) is multiplied by 4 Weight Units.
    - Witness data (signatures) is multiplied by 1 Weight Unit.
    - weight = (base_size * 3) + total_size
    - vBytes = ceil(weight / 4)
    """
    # The witness size is the difference between total and base
    witness_size = total_size - base_size
    
    # Calculate exact weight
    weight = (base_size * 3) + total_size
    
    # Calculate vbytes (using math.ceil to match Bitcoin Core's rounding up)
    vbytes = math.ceil(weight / 4)
    
    # Calculate how much weight was saved compared to a legacy transaction
    legacy_weight = total_size * 4
    savings_pct = round(((legacy_weight - weight) / legacy_weight) * 100, 2)
    
    return {
        "Base Size (bytes)": base_size,
        "Witness Size (bytes)": witness_size,
        "Total Size (bytes)": total_size,
        "Weight (WU)": weight,
        "vBytes (vB)": vbytes,
        "SegWit Savings": f"{savings_pct}%"
    }

if __name__ == "__main__":
    # Example using a standard 1-input, 2-output P2WPKH transaction
    print("🧪 Testing SegWit Math Logic:")
    print("-" * 30)
    
    # Typical sizes for a Native SegWit transaction
    example_base = 115
    example_total = 222
    
    metrics = calculate_tx_metrics(example_base, example_total)
    
    for key, value in metrics.items():
        print(f"{key}: {value}")
