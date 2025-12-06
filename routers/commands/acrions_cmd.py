from aiogram import Router, F
from aiogram import types
from aiogram.filters import Command
from keyboards import build_actions_kb, build_nums_inline_kb

router = Router()


@router.message(Command("actions"))
async def actions_cmd(message: types.Message):

    await message.answer(
        text="Choose an action:",
        reply_markup=build_nums_inline_kb(),
    )


@router.callback_query(F.data.startswith("inline_kb"))
async def handle_num_inline_kb(callback: types.CallbackQuery):
    data = callback.data
    num = data.split(":")[1]
    text = f"You pressed {num} button"
    # await callback.answer(text)
    await callback.message.answer(text)
    await callback.answer(
        text,
        show_alert=True,
    )
