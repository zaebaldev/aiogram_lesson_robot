from aiogram import F, Router
from aiogram import types
from aiogram.filters import Command
from aiogram.types import FSInputFile

router = Router()
any_media = F.photo | F.document | F.video


@router.message(F.photo & ~F.caption)
async def handle_any_photo_without_caption(message: types.Message):
    if message.photo:
        await message.answer(
            text="I cant see what in image",
        )


@router.message(any_media)
async def handle_any_media_message(message: types.Message):
    if message.photo:
        await message.answer_photo(
            photo=message.photo[1].file_id,
            caption=message.caption if message.caption else "",
        )
    if message.document:
        await message.answer_document(
            document=message.document.file_id,
        )
    if message.video:
        await message.answer_video(
            video=message.video.file_id,
        )

    # await message.copy_to(
    #     chat_id=message.chat.id,
    # )


@router.message(Command("photo"))
async def photo_cmd(message: types.Message):
    photo = FSInputFile("/home/alien/Pictures/icon - edid this.png")
    await message.answer_photo(
        photo=photo,
        caption="this is a picture",
    )


@router.message(Command("doc"))
async def doc_cmd(message: types.Message):
    doc = FSInputFile("/home/alien/Pictures/icon - edid this.png")
    await message.answer_document(
        document=doc,
        caption="this is a picture",
    )
