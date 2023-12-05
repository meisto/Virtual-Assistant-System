# ======================================================================
# Author: meisto
# Creation Date: Sun 03 Dec 2023 09:55:24 PM CET
# Description: -
# ======================================================================
from typing import Dict

from fastapi import APIRouter
from pydantic import BaseModel

from src.modules.chat import send_message, clear_messages

class MessageMessage(BaseModel):
    message: str

router = APIRouter(prefix="/chat")

@router.post("/message")
def test_chat(message: MessageMessage) -> Dict:
    """ TODO """
    response = send_message(message.message)

    print(response)
    return {
        "content": response["response"],
    }

@router.post("/clear")
def clear_chat_messages():
    """ Clear the message history of the chatbot. """
    clear_messages()
