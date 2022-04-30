from fastapi import FastAPI

from settings import settings
import api


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description
)

app.include_router(api.router)
