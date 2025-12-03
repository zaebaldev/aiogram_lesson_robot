from aiogram import Bot, Dispatcher, F
from aiogram import types
from aiogram.filters import CommandStart, Command
from config import token
import asyncio
from aiogram.types import FSInputFile

my_bot = Bot(token=str(token))
dp = Dispatcher()

any_media = F.photo | F.document | F.video


@dp.message(any_media)
async def handle_any_media_message(message: types.Message):
    if message.photo:
        await message.answer_photo(
            photo=message.photo[1].file_id,
        )
    if message.document:
        await message.answer_document(
            document=message.document.file_id,
        )
    if message.video:
        await message.answer_video(
            video=message.video.file_id,
        )

    # await message.copy_to(
    #     chat_id=message.chat.id,
    # )


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    print(message.from_user.id)
    await message.answer(
        f"Добро  пожаловать, {message.from_user.full_name}",
    )


@dp.message(Command("info", prefix="!/"))
async def hanle_info(message: types.Message):
    await message.answer(
        text="Это тестовый бот для изучения aiogram",
    )


@dp.message(Command("photo"))
async def photo_cmd(message: types.Message):
    photo = FSInputFile("/home/alien/Pictures/icon - edid this.png")
    await message.answer_photo(
        photo=photo,
    )


async def main():
    print("I am starting ...")
    await dp.start_polling(my_bot)


if __name__ == "__main__":
    asyncio.run(main())
