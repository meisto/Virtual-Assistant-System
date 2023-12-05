# ======================================================================
# Author: meisto
# Creation Date: Wed 29 Nov 2023 11:53:51 AM CET
# Description: -
# ======================================================================
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uvicorn

from api import router as api_router
from config import Config


app = FastAPI()
app.include_router(api_router)

# Add this to remove CORS problems
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve GUI
app.mount("/static", StaticFiles(directory="gui"), name="gui")


def main():
    """ Main function. """
    uvicorn.run(
        app="main:app",
        host=Config.HOST,
        port=Config.PORT,
        log_level="info",
        reload=True,
    )

    print("Server started.")



if __name__ == "__main__":
    main()
