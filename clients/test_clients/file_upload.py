# ======================================================================
# Author: meisto
# Creation Date: Mon 20 Nov 2023 06:21:15 PM CET
# Description: -
# ======================================================================
import requests

URL="http://localhost:8000/uploadfile/"
with open("/tmp/test_record.wav", mode="rb") as input_file:
    file = {"file": input_file}
    resp = requests.post(url=URL, files=file, timeout=30)
    print(resp.json())
