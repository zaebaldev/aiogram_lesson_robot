from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton


def build_actions_kb():
    btn1 = InlineKeyboardButton(
        text="bot link",
        url="https://t.me/aiogram_lesson_robot",
    )
    btn2 = InlineKeyboardButton(
        text="bot code",
        url="https://github.com/zaebaldev/aiogram_lesson_robot",
    )
    btn3 = InlineKeyboardButton(
        text="pavel Durov",
        url="https://t.me/durov",
    )
    kb = InlineKeyboardMarkup(
        inline_keyboard=[[btn1], [btn2, btn3]],
    )
    return kb
