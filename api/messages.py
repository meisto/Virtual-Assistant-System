# ======================================================================
# Author: meisto
# Creation Date: Sat 02 Dec 2023 04:12:46 AM CET
# Description: -
# ======================================================================
from typing import List, Optional

from fastapi import APIRouter

from src.modules.store import LocalStore

router = APIRouter(prefix="/messages")

@router.get("/get")
def get_messages(starting_id: Optional[int] = None) -> List:
    return []
