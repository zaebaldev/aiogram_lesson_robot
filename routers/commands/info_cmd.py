from aiogram import Router, F
from aiogram import types
from aiogram.filters import CommandStart, Command
from config import admin_ids
from keyboards import (
    create_info_kb_builder,
    create_info_kb_markup,
    request_user_phone_number_and_location,
)
from db import cursor, conn

router = Router()


@router.message(CommandStart())
async def handle_start(message: types.Message):
    first_name = message.from_user.first_name
    cursor.execute("INSERT INTO users (username) VALUES (?)", (first_name,))
    conn.commit()
    await message.answer(
        text=f"Добро  пожаловать, {first_name}",
        reply_markup=request_user_phone_number_and_location(),
    )


@router.message(Command("info", prefix="!/"))
async def hanle_info(message: types.Message):
    await message.answer(
        text="Это тестовый бот для изучения aiogram",
        reply_markup=create_info_kb_markup(),
    )


@router.message(F.from_user.id.in_(admin_ids) & (F.text == "admin"))
async def handle_exact_users_message(message: types.Message):
    await message.answer(
        text="secret message",
    )


@router.message(Command("users", prefix="!/"))
async def hanle_users_cmd(message: types.Message):
    users = cursor.execute("SELECT username  FROM user")
    # users = cursor.execute("SELECT username  FROM users WHERE id=6")
    users = users.fetchall()
    print(users)
    for user in users:
        user_name = user[0]
        print(user_name)
        await message.answer(user_name)
