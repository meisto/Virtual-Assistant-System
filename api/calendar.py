# ======================================================================
# Author: meisto
# Creation Date: Fri 01 Dec 2023 02:06:45 AM CET
# Description: -
# ======================================================================
from typing import Dict, Optional

from fastapi import APIRouter

from src.modules.store import LocalStore

router = APIRouter(prefix="/calendar")

@router.get("/number_events")
def get_number_events() -> int:
    return len(LocalStore.calendar)

@router.get("/get_events")
def get_events(
    weeks: Optional[int] = None,
    days: Optional[int] = None
):
    print(weeks, days)

    if weeks is None and days is None:
        return LocalStore.calendar.events

    days = days or 0
    weeks = weeks or 0

    days = max(days, 7 * weeks)

    return days
