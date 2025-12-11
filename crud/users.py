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


async def add_user(first_name: str) -> None:
    db = await aiosqlite.connect(my_db)
    cursor = await db.cursor()
    await cursor.execute("INSERT INTO users (username) VALUES (?)", (first_name,))
    await db.commit()
    await cursor.close()
    await db.close()


async def delete_user(user_id: int) -> None:
    # without db.close because 'async with' close it automaticaly
    async with aiosqlite.connect(my_db) as db:
        cursor = await db.cursor()
        await cursor.execute("DELETE FROM  users WHERE id = (?)", (user_id,))
        await db.commit()
