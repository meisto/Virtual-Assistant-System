# ======================================================================
# Author: meisto
# Creation Date: Fri 01 Dec 2023 01:29:41 AM CET
# Description: -
# ======================================================================
import os

from dotenv import load_dotenv
from pydantic import BaseModel

class AppConfiguration(BaseModel):
    HOST: str
    PORT: int

# Load local .env file if it exists
if os.path.isfile(".env"):
    load_dotenv(dotenv_path=".env")

Config = AppConfiguration(**os.environ)
