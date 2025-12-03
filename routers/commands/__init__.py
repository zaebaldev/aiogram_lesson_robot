from aiogram import Router
from .info_cmd import router as info_router

router = Router()
router.include_routers(info_router)
