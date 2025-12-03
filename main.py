from aiogram import Bot, Dispatcher
from config import token
import asyncio
from routers import router

my_bot = Bot(token=str(token))
dp = Dispatcher()


async def main():
    print("I am starting ...")
    dp.include_routers(router)
    await dp.start_polling(my_bot)


if __name__ == "__main__":
    asyncio.run(main())
