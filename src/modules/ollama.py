""" ollama module """
# ======================================================================
# Author: meisto
# Creation Date: Wed 29 Nov 2023 11:29:12 AM CET
# Description: -
# ======================================================================
from typing import Optional, List

import requests

from modules.models import LargeLanguageModel

OLLAMA_URL = "http://localhost:11434"


def get_models() -> Optional[List[LargeLanguageModel]]:
    """Get all local models available to ollama"""

    try:
        response = requests.get(OLLAMA_URL + "/api/tags", timeout=30).json()

        def reformat(model_params: dict):
            # Rename keys
            model_params["last_modified"] = model_params.pop("modified_at")

            name = model_params["name"]
            model_params["name"] = name.split(":")[0]
            model_params["tag"] = ":".join(name.split(":")[1:])


            model_params["source"] = "ollama"

            return model_params

        return [LargeLanguageModel(**reformat(x)) for x in response["models"]]

    except requests.exceptions.ConnectionError:
        return None
