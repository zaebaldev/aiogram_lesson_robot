from aiogram import Bot, Dispatcher
from config import token
import asyncio
from routers import router
from db import init_db
import logging

logger = logging.getLogger(__name__)

my_bot = Bot(token=str(token))
dp = Dispatcher()


async def main():

    logging.basicConfig(
        level=logging.INFO,
    )
    try:
        2 / 0
    except Exception as e:
        logger.error(e)
    logger.info("info log")
    await init_db()
    dp.include_routers(router)
    await dp.start_polling(my_bot)


if __name__ == "__main__":
    asyncio.run(main())
