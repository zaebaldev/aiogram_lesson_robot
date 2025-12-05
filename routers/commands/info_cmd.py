from aiogram import Router, F
from aiogram import types
from aiogram.filters import CommandStart, Command
from config import admin_ids
from keyboards import create_info_kb_builder, create_info_kb_markup

router = Router()


@router.message(CommandStart())
async def handle_start(message: types.Message):
    print(message.from_user.id)

    await message.answer(
        text=f"Добро  пожаловать, {message.from_user.full_name}",
        reply_markup=create_info_kb_markup(),
    )


@router.message(Command("info", prefix="!/"))
async def hanle_info(message: types.Message):
    await message.answer(
        text="Это тестовый бот для изучения aiogram",
    )


@router.message(F.from_user.id.in_(admin_ids) & (F.text == "admin"))
async def handle_exact_users_message(message: types.Message):
    await message.answer(
        text="secret message",
    )
