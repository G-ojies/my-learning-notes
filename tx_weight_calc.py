"""
Bitcoin Transaction Weight (WU) Calculator
Research Notes: Calculating the exact block space usage of SegWit transactions.
Weight = (Base Size * 3) + Total Size
"""
def calculate_wu(base_bytes: int, total_bytes: int) -> dict:
    witness_bytes = total_bytes - base_bytes
    weight_units = (base_bytes * 3) + total_bytes
    vbytes = weight_units / 4
    
    return {
        "Base (Legacy) Bytes": base_bytes,
        "Witness Bytes": witness_bytes,
        "Total Weight (WU)": weight_units,
        "Virtual Bytes (vB)": vbytes
    }

if __name__ == "__main__":
    print(calculate_wu(base_bytes=100, total_bytes=150))
