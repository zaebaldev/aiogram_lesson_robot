from aiogram import Router, F
from aiogram import types
from config import admin_ids


router = Router()


@router.message(F.from_user.id.in_(admin_ids) & (F.text == "admin"))
async def handle_exact_users_message(message: types.Message):
    await message.answer(
        text="secret message",
    )
