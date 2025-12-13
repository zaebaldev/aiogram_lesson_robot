from aiogram import Router
from aiogram import types
from aiogram.filters import Command
from crud import get_all_users, delete_user

router = Router()


@router.message(Command("users", prefix="!/"))
async def hanle_users_cmd(message: types.Message):
    users = await get_all_users()
    print(users)
    for user in users:
        user_name = user[1]
        await message.answer(text=user_name)


@router.message(Command("delete", prefix="!/"))
async def hanle_delte_user_cmd(message: types.Message):
    text = message.text
    parts = text.split()
    print(parts)
    user_id = parts[1]
    print(user_id)
    await delete_user(user_id=int(user_id))
    await message.answer("User deleted successfully")
