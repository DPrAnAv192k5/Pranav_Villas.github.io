import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create Users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

print("✅ Database initialized successfully!")
