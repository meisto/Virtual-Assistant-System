""" """
# ======================================================================
# Author: meisto
# Creation Date: Wed 29 Nov 2023 11:41:32 AM CET
# Description: -
# ======================================================================
from datetime import datetime

from pydantic import BaseModel

class LargeLanguageModel(BaseModel):
    """ TODO """
    name: str
    tag: str
    last_modified: datetime
    source: str

class TextToSpeechModel(BaseModel):
    """ TODO """
    name: str
    tag: str
    last_modified: datetime
    source: str

class SpeechSynthesisModel(BaseModel):
    """ TODO """
    name: str
    tag: str
    last_modified: datetime
    source: str
