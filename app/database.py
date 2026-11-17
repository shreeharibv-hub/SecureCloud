import sqlite3
import os


DB_PATH = "/data/securecloud.db"


def get_db_connection(db_name=DB_PATH):
    os.makedirs(os.path.dirname(db_name), exist_ok=True)

    conn = sqlite3.connect(db_name)
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()