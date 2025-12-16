from config import my_db
import aiosqlite


async def init_db():
    db = await aiosqlite.connect(my_db)
    cursor = await db.cursor()
    await cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                tg_id TEXT UNIQUE NOT NULL
            );
            """
    )
    await db.commit()
    await cursor.close()
    await db.close()
