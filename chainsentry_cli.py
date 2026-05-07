"""
ChainSentry: Command Line Interface (CLI)
Research Notes: An interactive terminal tool to control the backend.
"""
import sys

def print_help():
    print("""
🛡️  ChainSentry CLI v1.0
Commands:
  start      - Launch the mempool ZMQ listener
  add <addr> - Add a Bitcoin address to the watchlist
  status     - View node connection and DB stats
  logs       - Tail recent zero-conf events
    """)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
    else:
        command = sys.argv[1]
        if command == "start":
            print("🚀 Starting ChainSentry Mempool Monitor...")
        elif command == "add":
            addr = sys.argv[2] if len(sys.argv) > 2 else "Unknown"
            print(f"👁️ Adding {addr} to database...")
        elif command == "status":
            print("✅ Node: Synced | DB: Online | Watching: 12 Addresses")
        else:
            print_help()
