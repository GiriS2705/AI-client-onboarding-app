import sqlite3

conn = sqlite3.connect("clients.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    phone TEXT,
    status TEXT
)
""")

def insert_client(name, email, phone):
    cursor.execute("INSERT INTO clients (name, email, phone, status) VALUES (?, ?, ?, ?)",
                   (name, email, phone, "Pending"))
    conn.commit()

def get_clients():
    cursor.execute("SELECT * FROM clients")
    return cursor.fetchall()

def update_status(client_id, status):
    cursor.execute("UPDATE clients SET status=? WHERE id=?", (status, client_id))
    conn.commit()