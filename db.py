from config import my_db
import sqlite3


def init_db():
    conn = sqlite3.connect(my_db)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE
        );
        """
    )
    conn.commit()
    conn.close()
