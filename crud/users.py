import logging
import sqlite3
from typing import Iterable
import aiosqlite
from config import my_db
import logging

logger = logging.getLogger(__name__)


async def get_all_users() -> Iterable[sqlite3.Row]:
    db = await aiosqlite.connect(my_db)
    cursor = await db.cursor()
    await cursor.execute("SELECT * FROM users")
    rows = await cursor.fetchall()
    await cursor.close()
    await db.close()
    return rows


async def add_user(
    first_name: str,
    tg_id: str,
) -> None:
    try:
        db = await aiosqlite.connect(my_db)
        cursor = await db.cursor()
        await cursor.execute(
            "INSERT INTO users (username, tg_id) VALUES (?, ?)",
            (first_name, tg_id),
        )
        await db.commit()
        await cursor.close()
        await db.close()
    except Exception as e:
        logger.error(e)


async def delete_user(user_id: int) -> None:
    # without db.close because 'async with' close it automaticaly
    async with aiosqlite.connect(my_db) as db:
        cursor = await db.cursor()
        await cursor.execute("DELETE FROM  users WHERE id = (?)", (user_id,))
        await db.commit()


async def update_user(user_id: int, first_name: str, z) -> None:
    db = await aiosqlite.connect(my_db)
    cursor = await db.cursor()
    await cursor.execute(
        "UPDATE users  SET username=(?) WHERE id=(?)", (first_name, user_id)
    )
    await db.commit()
    await cursor.close()
    await db.close()


async def check_user(
    user_id: int,
) -> bool:
    db = await aiosqlite.connect(my_db)
    cursor = await db.cursor()
    await cursor.execute("SELECT id  FROM users WHERE id=(?)", (user_id,))
    row = await cursor.fetchone()
    await cursor.close()
    await db.close()
    return True if row else False
