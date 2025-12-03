from aiogram import Router
from .media_handlers import router as media_router
from .commands import router as commands_router
from .admin_handlers import router as admin_router

router = Router()
router.include_routers(
    media_router,
    commands_router,
    admin_router,
)
