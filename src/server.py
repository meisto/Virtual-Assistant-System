""" Server module """
# ======================================================================
# Author: meisto
# Creation Date: Mon 20 Nov 2023 05:56:26 PM CET
# Description: -
# ======================================================================
from typing import Annotated
from contextlib import asynccontextmanager
import os
from os.path import join as pjoin
import sys

from fastapi import FastAPI, File, UploadFile

import resources
from util import time_string


@asynccontextmanager
async def lifespan(_: FastAPI):
    """
    Handle lifespan events for the server. This means functions for setting up the server and
    to clear resources after shutting down.
    """
    # Run stuff before server starts
    print("[INFO] Setting up server resources...")
    resources.setup()

    yield

    # Run stuff after server shuts down
    print("[INFO] Clearing resources...")
    resources.teardown()


app = FastAPI(lifespan=lifespan)


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    """Upload a file."""
    try:
        file_content = file.file.read()
        file_name = file.filename

        print(f"File_name: {file_name}")
        assert file_name.endswith(".wav")

        file_name = file_name.replace(".wav", "") + "_" + time_string() + ".wav"
        file_path = pjoin(os.getenv("FILE_PATH"), file_name)
        with open(file_path, mode="wb") as output_file:
            output_file.write(file_content)

        return {"message": "Success."}

    except Exception as err:
        print(err, file=sys.stderr)
        return {"message": "An errror occured during file processing"}
    finally:
        file.file.close()
