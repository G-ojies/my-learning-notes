"""
ChainSentry: Database CRUD Operations
Research Notes: Functions to write and read from the ChainSentry SQLite backend.
"""
import sqlite3
import time

def add_to_watchlist(cursor, address: str, label: str):
    """Adds a new Bitcoin address to the monitoring watch list."""
    try:
        cursor.execute('''
            INSERT INTO watch_list (address, label, added_timestamp)
            VALUES (?, ?, ?)
        ''', (address, label, int(time.time())))
        print(f"👁️ Added {address} ({label}) to Watch List.")
    except sqlite3.IntegrityError:
        print(f"⚠️ Address {address} is already being watched.")

def log_mempool_event(cursor, txid: str, address: str, amount_sats: int, is_rbf: bool):
    """Logs a detected zero-conf transaction to the database."""
    cursor.execute('''
        INSERT INTO mempool_events (txid, address, amount_sats, is_rbf, detected_timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (txid, address, amount_sats, is_rbf, int(time.time())))
    print(f"💾 Logged TXID {txid[:8]}... to database.")

def fetch_recent_events(cursor, limit: int = 5):
    """Retrieves the most recent mempool events."""
    cursor.execute('''
        SELECT txid, address, amount_sats, is_rbf FROM mempool_events
        ORDER BY detected_timestamp DESC LIMIT ?
    ''', (limit,))
    return cursor.fetchall()

if __name__ == "__main__":
    # Test the CRUD operations using an in-memory database
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    
    # Initialize schema (mocking Sunday's script)
    c.execute('CREATE TABLE watch_list (address TEXT UNIQUE, label TEXT, added_timestamp INTEGER)')
    c.execute('CREATE TABLE mempool_events (txid TEXT, address TEXT, amount_sats INTEGER, is_rbf BOOLEAN, detected_timestamp INTEGER)')
    
    print("🛠️ Testing ChainSentry CRUD Operations")
    print("-" * 65)
    
    add_to_watchlist(c, "bc1q_cold_storage", "Cold Wallet")
    log_mempool_event(c, "a1b2c3d4...", "bc1q_cold_storage", 50000000, False)
    
    print("\nRecent Events in DB:")
    for event in fetch_recent_events(c):
        print(f"  TX: {event[0]} | Addr: {event[1]} | Sats: {event[2]} | RBF: {event[3]}")
