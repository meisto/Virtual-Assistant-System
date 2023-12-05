# ======================================================================
# Author: meisto
# Creation Date: Fri 01 Dec 2023 02:09:10 AM CET
# Description: -
# ======================================================================
from typing import List

import pydantic

from src.modules.calendar.models import CalendarEvent

class Calendar(pydantic.BaseModel):
    events: List[CalendarEvent] = []


    def __len__(self) -> int:
        return len(self.events)
