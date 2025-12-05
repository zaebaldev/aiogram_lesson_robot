from aiogram import Router, F
from aiogram import types
from aiogram.filters import CommandStart, Command
from config import admin_ids
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

router = Router()


@router.message(CommandStart())
async def handle_start(message: types.Message):
    print(message.from_user.id)
    # btn1 = KeyboardButton(text="test")
    # btn2 = KeyboardButton(text="some text")
    # btn3 = KeyboardButton(text="something")
    # keyboard = ReplyKeyboardMarkup(
    #     keyboard=[
    #         [btn1, btn2],
    #         [btn3],
    #     ],
    #     resize_keyboard=True,
    # )
    builder = ReplyKeyboardBuilder()
    for i in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
        builder.button(
            text=f"Set {i}",
        )
    # builder.add(btn1, btn2, btn3)
    builder.adjust(3)
    await message.answer(
        text=f"Добро  пожаловать, {message.from_user.full_name}",
        reply_markup=builder.as_markup(),
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
