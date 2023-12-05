# ======================================================================
# Author: meisto
# Creation Date: Fri 01 Dec 2023 02:12:37 AM CET
# Description: -
# ======================================================================
from src.modules.calendar import Calendar

class Store:

    def __init__(self):
        self.calendar = Calendar()


def load_store() -> Store:
    """ TODO """
    return Store()

LocalStore = load_store()
