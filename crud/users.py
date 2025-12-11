from typing import Tuple
import aiosqlite
from config import my_db


async def get_all_users() -> list[Tuple]:
    db = await aiosqlite.connect(my_db)
    cursor = await db.execute("SELECT * FROM users")
    rows = await cursor.fetchall()
    await cursor.close()
    await db.close()
    return rows


async def add_user(first_name: str) -> None:
    db = await aiosqlite.connect(my_db)
    cursor = await db.execute("INSERT INTO users (username) VALUES (?)", (first_name,))
    await cursor.close()
    await db.close()


async def delete_user(user_id: int) -> None:
    db = await aiosqlite.connect(my_db)
    cursor = await db.execute("DELETE FROM  users WHERE id= (?)", (user_id,))
    await cursor.close()
    await db.close()
