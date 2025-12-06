from aiogram import Router
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
    text = message.text
    if text.isalpha():
        await state.update_data(name=text)
        await message.answer(
            text="What is your surname?",
        )
        await state.set_state(Survey.surname)
    else:
        await message.answer(
            text="Please, enter correct name",
        )


@router.message(Survey.surname)
async def handle_survey_surname_state(
    message: types.Message,
    state: FSMContext,
):
    await state.update_data(surname=message.text)
    await state.set_state(Survey.age)
