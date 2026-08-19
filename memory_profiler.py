"""
ChainSentry v1.5.1: UTXO Memory Profiler
Research Notes: Tracking RAM utilization during massive state synchronization.
"""
import sys

def profile_utxo_memory(utxo_set: dict):
    """Calculates the exact byte size of the UTXO dictionary in memory."""
    mem_bytes = sys.getsizeof(utxo_set)
    print(f"📊 Current UTXO Set RAM Utilization: {mem_bytes / 1024:.2f} KB")
    if mem_bytes > 500000:
        print(" -> [WARNING] Memory threshold exceeded. Recommend flushing to SQLite WAL.")

if __name__ == "__main__":
    mock_utxos = {f"txid_{i}:0": {"amount": 50000, "scriptPubKey": "0014abc..."} for i in range(100)}
    profile_utxo_memory(mock_utxos)
