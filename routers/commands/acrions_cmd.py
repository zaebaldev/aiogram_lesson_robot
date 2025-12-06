from aiogram import Router
from aiogram import types
from aiogram.filters import Command
from keyboards import build_actions_kb

router = Router()


@router.message(Command("actions"))
async def actions_cmd(message: types.Message):

    await message.answer(
        text="Choose an action:",
        reply_markup=build_actions_kb(),
    )
