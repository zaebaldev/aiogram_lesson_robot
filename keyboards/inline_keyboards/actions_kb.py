from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


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


def build_nums_inline_kb():
    builder = InlineKeyboardBuilder()
    for i in range(1, 11):
        builder.button(
            text=f"{i}",
            callback_data=f"inline_kb:{i}", #inline_kb:2
        )
    builder.adjust(2)
    return builder.as_markup()
