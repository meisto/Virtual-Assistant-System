""" Utility functions. """
# ======================================================================
# Author: meisto
# Creation Date: Mon 20 Nov 2023 06:28:13 PM CET
# Description: -
# ======================================================================
import datetime

def time_string() -> str:
    """ Return current time as string. """
    now = datetime.datetime.now()

    date = f"{now.year}{now.month:>02}{now.day:>02}"
    time = f"{now.hour:>02}{now.minute:>02}{now.second:>02}{now.microsecond}"

    return date + "_" + time
