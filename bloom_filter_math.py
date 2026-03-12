"""
Bitcoin SPV Node Bloom Filters (BIP37)
Research Notes: Calculating the false positive rate for light clients.
"""
import math

def false_positive_rate(num_items: int, filter_size_bytes: int, num_hash_funcs: int) -> float:
    filter_size_bits = filter_size_bytes * 8
    exponent = -1 * num_hash_funcs * num_items / filter_size_bits
    return (1 - math.exp(exponent)) ** num_hash_funcs

if __name__ == "__main__":
    print(f"Bloom Filter FP Rate: {false_positive_rate(10, 36, 5):.4%}")
