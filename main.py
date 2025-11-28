from aiogram import Bot, Dispatcher
from aiogram import types
from aiogram.filters import CommandStart, Command
from config import token
import asyncio

my_bot = Bot(token=str(token))
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(
        f"Добро  пожаловать, {message.from_user.full_name}",
    )


@dp.message(Command("info"))
async def hanle_info(message: types.Message):
    await message.answer(
        text="Это тестовый бот для изучения aiogram",
    )


async def main():
    print("I am starting ...")
    await dp.start_polling(my_bot)


if __name__ == "__main__":
    asyncio.run(main())
