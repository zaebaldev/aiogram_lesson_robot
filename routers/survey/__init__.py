from aiogram import Router
from .survey_cmd import router as survey_cmd_router

router = Router()
router.include_routers(
    survey_cmd_router,
)
