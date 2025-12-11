import aiosqlite
from config import my_db


async def init_db():
    db = await aiosqlite.connect(my_db)
    query = """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE
        );
        """
    cursor = await db.execute(query)
    await cursor.close()
    await db.close()
