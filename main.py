from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from config import token
import asyncio

my_bot = Bot(token=str(token))
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message):
    await message.answer("hi")


async def main():
    print("I am starting ...")
    await dp.start_polling(my_bot)


if __name__ == "__main__":
    asyncio.run(main())
