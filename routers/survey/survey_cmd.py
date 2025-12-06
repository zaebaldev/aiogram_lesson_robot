from aiogram import Router, F
from aiogram import types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

router = Router()


class Survey(StatesGroup):
    name = State()
    surname = State()
    age = State()


@router.message(Command("survey", prefix="!/"))
async def start_survey_cmd(
    message: types.Message,
    state: FSMContext,
):
    await message.answer(
        text="What is your name?",
    )
    await state.set_state(Survey.name)


@router.message(Survey.name)
async def handle_survey_name_state(
    message: types.Message,
    state: FSMContext,
):
    await message.answer(
        text=f"Your name is {message.text}",
    )
    await state.set_state(Survey.surname)
