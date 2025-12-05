from aiogram import Router, F
from aiogram import types

router = Router()


@router.message(F.contact)
async def handle_user_contact_message(message: types.Message):
    await message.answer(
        text=f"your phone number is {message.contact.phone_number}",
    )


@router.message(F.location)
async def handle_user_location_message(message: types.Message):
    await message.answer(
        text=f"Long {message.location.longitude} \n Lat {message.location.latitude}",
    )
