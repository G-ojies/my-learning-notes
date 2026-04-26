"""
ChainSentry: SQLite Database Schema
Research Notes: Backend tables for tracking target wallets and unconfirmed UTXOs.
"""
import sqlite3

def init_db():
    conn = sqlite3.connect(':memory:') # In-memory for research
    cursor = conn.cursor()
    
    # Table to store addresses ChainSentry is watching
    cursor.execute('''
        CREATE TABLE watch_list (
            id INTEGER PRIMARY KEY,
            address TEXT UNIQUE NOT NULL,
            label TEXT,
            added_timestamp INTEGER
        )
    ''')
    
    # Table to log zero-conf mempool sightings
    cursor.execute('''
        CREATE TABLE mempool_events (
            id INTEGER PRIMARY KEY,
            txid TEXT NOT NULL,
            address TEXT NOT NULL,
            amount_sats INTEGER,
            is_rbf BOOLEAN,
            detected_timestamp INTEGER,
            FOREIGN KEY(address) REFERENCES watch_list(address)
        )
    ''')
    
    print("🗄️ ChainSentry Database Schema Initialized Successfully!")

if __name__ == "__main__":
    init_db()
