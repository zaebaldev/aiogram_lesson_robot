from aiogram import Router, F
from aiogram import types
from aiogram.filters import CommandStart, Command
from config import admin_ids
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton

router = Router()


@router.message(CommandStart())
async def handle_start(message: types.Message):
    print(message.from_user.id)
    btn1 = KeyboardButton(text="test")
    btn2 = KeyboardButton(text="some text")
    btn3 = KeyboardButton(text="something")
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [btn1, btn2],
            [btn3],
        ],
        resize_keyboard=True,
    )
    await message.answer(
        text=f"Добро  пожаловать, {message.from_user.full_name}",
        reply_markup=keyboard,
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
