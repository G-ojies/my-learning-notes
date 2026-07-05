"""
ChainSentry v1.2.0: SQLite WAL Mode
"""
import sqlite3
def enable_wal(db_path: str):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA journal_mode=WAL;")
    print("🚀 Write-Ahead Logging (WAL) enabled for high concurrency!")
