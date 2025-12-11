import sqlite3
from typing import Iterable, Tuple
import aiosqlite
from config import my_db


async def get_all_users() -> Iterable[Tuple]:
    db = await aiosqlite.connect(my_db)
    cursor = await db.execute("SELECT * FROM users")
    rows = await cursor.fetchall()
    await cursor.close()
    await db.close()
    return rows


def add_user(first_name: str) -> None:
    db = sqlite3.connect(my_db)
    cursor = db.execute("INSERT INTO users (username) VALUES (?)", (first_name,))
    db.commit()
    cursor.close()
    db.close()


def delete_user(user_id: int) -> None:
    db = sqlite3.connect(my_db)
    cursor = db.execute("DELETE FROM  users WHERE id = (?)", (user_id,))
    db.commit()
    cursor.close()
    db.close()
