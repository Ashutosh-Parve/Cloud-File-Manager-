import sqlite3

def create_log_table():
    conn = sqlite3.connect("file_logs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT,
            filename TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def log_action(action, filename):
    conn = sqlite3.connect("file_logs.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logs(action, filename) VALUES (?, ?)", (action, filename))
    conn.commit()
    conn.close()
