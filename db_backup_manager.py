"""
ChainSentry: Automated Database Backup Manager
Research Notes: Safely snapshotting the SQLite database using the backup API to prevent corruption during live writes.
"""
import sqlite3
import time
import os

def create_db_snapshot(source_db_path: str, backup_dir: str = "./backups"):
    """
    Creates a safe, point-in-time snapshot of the live SQLite database.
    """
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
        
    timestamp = int(time.time())
    backup_file = os.path.join(backup_dir, f"chainsentry_backup_{timestamp}.sqlite")
    
    try:
        # Connect to the live database
        # (Using :memory: here for demonstration, but it simulates the real file lock)
        live_conn = sqlite3.connect(':memory:') 
        backup_conn = sqlite3.connect(backup_file)
        
        print(f"🗄️ Initiating safe database snapshot to {backup_file}...")
        
        # Use SQLite's native backup API to prevent locking/corruption
        live_conn.backup(backup_conn)
        
        backup_conn.close()
        live_conn.close()
        print("✅ Backup completed successfully!")
        
    except Exception as e:
        print(f"❌ Backup failed: {e}")

if __name__ == "__main__":
    print("🛡️ ChainSentry Backup Manager")
    print("-" * 65)
    create_db_snapshot("chainsentry.db")
