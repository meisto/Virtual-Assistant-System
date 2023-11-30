""" Main module """
# ======================================================================
# Author: meisto
# Creation Date: Mon 20 Nov 2023 05:53:18 PM CET
# Description: -
# ======================================================================
import os
from os.path import join as pjoin

from dotenv import load_dotenv

def setup():
    """ Set up ressources. """
    load_dotenv()

    data_path = os.getenv("DATA_DIR")
    assert data_path is not None
    assert os.path.isdir(data_path)

    print(f"Data Dir: {data_path}")
    data_path = pjoin(data_path, "assistant_data")
    file_path = pjoin(data_path, "files")

    if not os.path.exists(data_path):
        os.mkdir(data_path)
        os.mkdir(file_path)

    # Write to environment
    os.environ["DATA_PATH"] = data_path
    os.environ["FILE_PATH"] = file_path



def teardown():
    """ Free resources. """
