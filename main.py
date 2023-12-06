# ======================================================================
# Author: meisto
# Creation Date: Wed 29 Nov 2023 11:53:51 AM CET
# Description: -
# ======================================================================
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import uvicorn

from api.calendar import router as calendar_router
from api.messages import router as messages_router
from api.chat import router as chat_router

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

@app.get("/")
def homepage():
    """ Redirect to gui website."""
    return RedirectResponse(url="/static/index.html")

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
