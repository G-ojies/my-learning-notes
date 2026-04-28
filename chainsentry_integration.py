"""
ChainSentry: Full Mempool -> Database Integration
Research Notes: Tying the transaction detector to the local storage engine.
"""
import sqlite3
import time

def process_mempool_stream(cursor, mock_tx_stream: list):
    """
    Simulates a live ZMQ stream, checking against the database watch list.
    """
    print("🔄 Connecting to Mempool Stream...")
    
    # Fetch addresses we care about from the DB
    cursor.execute('SELECT address FROM watch_list')
    watched_addresses = {row[0] for row in cursor.fetchall()}
    
    for tx in mock_tx_stream:
        time.sleep(0.3) # Simulate network latency
        
        # Check outputs (Receiving funds)
        for output_addr in tx.get("outputs", []):
            if output_addr in watched_addresses:
                print(f"🚨 INFLOW DETECTED: {tx['txid'][:8]}...")
                # Log to DB!
                cursor.execute('''
                    INSERT INTO mempool_events (txid, address, amount_sats, is_rbf, detected_timestamp)
                    VALUES (?, ?, ?, ?, ?)
                ''', (tx['txid'], output_addr, tx['amount_sats'], tx.get('is_rbf', False), int(time.time())))

if __name__ == "__main__":
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('CREATE TABLE watch_list (address TEXT UNIQUE, label TEXT, added_timestamp INTEGER)')
    c.execute('CREATE TABLE mempool_events (txid TEXT, address TEXT, amount_sats INTEGER, is_rbf BOOLEAN, detected_timestamp INTEGER)')
    
    # Add a target to watch
    c.execute("INSERT INTO watch_list (address, label) VALUES ('bc1q_target', 'Main Wallet')")
    
    print("🛡️ ChainSentry Live Monitor Activated")
    print("-" * 65)
    
    mock_stream = [
        {"txid": "11112222", "outputs": ["1RandomAddress"], "amount_sats": 1000},
        {"txid": "99998888", "outputs": ["bc1q_target"], "amount_sats": 2500000, "is_rbf": True} # Should trigger!
    ]
    
    process_mempool_stream(c, mock_stream)
    
    print("-" * 65)
    print("Verifying Database State:")
    c.execute('SELECT txid, is_rbf FROM mempool_events')
    for row in c.fetchall():
         print(f"  -> Logged TX: {row[0]} | RBF Flagged: {bool(row[1])}")
