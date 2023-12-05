# ======================================================================
# Author: meisto
# Creation Date: Fri 01 Dec 2023 01:54:20 AM CET
# Description: -
# ======================================================================
from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel

class CalendarEvent(BaseModel):
    name: str
    event_type: str
    tags: List[str]
    place: Optional[str] = None
    start: Optional[datetime] = None
    end: Optional[datetime] = None
    whole_day: bool
    tags: List[str]
    description: str


