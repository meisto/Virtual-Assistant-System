# ======================================================================
# Author: meisto
# Creation Date: Fri 01 Dec 2023 02:05:36 AM CET
# Description: -
# ======================================================================
from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from api.calendar import router as calendar_router
from api.messages import router as messages_router
from api.chat import router as chat_router

router = APIRouter(prefix="/api")

router.include_router(calendar_router)
router.include_router(messages_router)
router.include_router(chat_router)



@router.get("/ping")
def ping():
    """ Simple function to check if a modules is alive. Just return pong. """

    return "pong"
