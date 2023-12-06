# ======================================================================
# Author: meisto
# Creation Date: Sun 03 Dec 2023 09:55:24 PM CET
# Description: -
# ======================================================================
from pydantic import BaseModel

class Message(BaseModel):
    id: int
    source: str
    timestamp: str
    content: str
