from aiogram import Router
from .info_cmd import router as info_router
from .acrions_cmd import router as actions_router
from .user_cmd import router as user_router

router = Router()
router.include_routers(
    info_router,
    actions_router,
    user_router,
)
