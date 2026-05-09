"""
ChainSentry: Regtest Network Simulator
Research Notes: Safely generating blocks and transactions locally to test the mempool monitor.
"""
import json

def simulate_regtest_commands():
    print("🛠️ Regtest Setup Commands for ChainSentry Testing:")
    commands = [
        ("Create a new wallet", "bitcoin-cli -regtest createwallet 'test_wallet'"),
        ("Generate an address", "bitcoin-cli -regtest getnewaddress"),
        ("Mine 101 blocks (to mature coinbase)", "bitcoin-cli -regtest -generate 101"),
        ("Send a test transaction", "bitcoin-cli -regtest sendtoaddress <address> 1.5"),
        ("Check the mempool", "bitcoin-cli -regtest getrawmempool")
    ]
    
    for desc, cmd in commands:
        print(f"\n> {desc}")
        print(f"  $ {cmd}")

if __name__ == "__main__":
    simulate_regtest_commands()
    print("\nUsing 'regtest' ensures we never risk real funds while testing ChainSentry!")
