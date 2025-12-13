from aiogram import Router
from aiogram import types
from aiogram.filters import Command
from crud import get_all_users, delete_user, update_user
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class UserUpdate(StatesGroup):
    id = State()
    fistr_name = State()


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


@router.message(Command("update", prefix="!/"))
async def update_user_cmd(
    message: types.Message,
    state: FSMContext,
):
    await message.answer("Enter user ID:")
    await state.set_state(UserUpdate.id)


@router.message(UserUpdate.id)
async def handle_user_update_id(
    message: types.Message,
    state: FSMContext,
):
    text = message.text
    if text and text.isdigit():
        await state.update_data(id=text)
        await message.answer("Enter first name to update")
        await state.set_state(UserUpdate.fistr_name)
    else:
        await message.answer("Enter correct ID")


@router.message(UserUpdate.fistr_name)
async def handle_user_update_fistr_name(
    message: types.Message,
    state: FSMContext,
):
    text = message.text
    user_data = await state.get_data()
    user_id = user_data.get("id")
    if user_data and user_id:
        await update_user(
            user_id=int(user_id),
            first_name=text,
        )
    await state.clear()
    await message.answer("User updated succesfully")
