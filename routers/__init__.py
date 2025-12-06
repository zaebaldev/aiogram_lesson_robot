from aiogram import Router
from .media_handlers import router as media_router
from .commands import router as commands_router
from .admin_handlers import router as admin_router
from .phone_handler import router as phone_handler_router
from .survey import router as survey_router

router = Router()
router.include_routers(
    media_router,
    commands_router,
    admin_router,
    phone_handler_router,
    survey_router,
)
