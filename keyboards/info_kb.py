from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def create_info_kb_markup():
    btn1 = KeyboardButton(text="button 1")
    btn2 = KeyboardButton(text="button 2")
    btn3 = KeyboardButton(text="button 3")
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [btn1, btn2],
            [btn3],
        ],
        resize_keyboard=True,
    )
    return keyboard


def create_info_kb_builder():
    builder = ReplyKeyboardBuilder()
    for i in range(1, 11):  # 1,2,3,4,5,6,7,8,9,10
        builder.button(
            text=f"Set {i}",
        )
    builder.adjust(3)
    return builder.as_markup()
