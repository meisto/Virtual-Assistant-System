""" __init__.py """
# ======================================================================
# Author: meisto
# Creation Date: Wed 06 Dec 2023 12:04:04 AM CET
# Description: -
# ======================================================================
from typing import Dict, List

from fastapi import APIRouter
from api.chat.message import Message

from src.modules.chat.channel import Channel


router = APIRouter(
    prefix="/chat",
    tags=["messages"],
)

channel = Channel("main")

@router.post("/message")
def test_chat(message: Message) -> Message:
    """ TODO """
    return channel.send_message(message)


@router.post("/clear")
def clear_chat_messages():
    """ Clear the message history of the chatbot. """
    channel.reset()

@router.get("/channels")
def get_channels() -> List[str]:
    """ Return all active channels. """
    return ["main"]

@router.post("/set_channel")
def set_channel(channel: str) -> bool:
    """ Set a channel. """
    return True


# @router.get("/get_messages")
# @router.post("/set_messages")
