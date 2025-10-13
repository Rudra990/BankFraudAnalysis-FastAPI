
import os, sys
print("CWD:", os.getcwd())
print("__name__:", __name__)
print("__package__:", __package__)
print("sys.path[0]:", sys.path[0])

from fastapi import FastAPI

from .core.config import settings
from .api.main import api_router


app = FastAPI(
  title = settings.PROJECT_NAME,
  description= settings.PROJECT_DESCRIPTION,
  docs_url = f"{settings.API_V1_STR}/docs",
  redoc_url = f"{settings.API_V1_STR}/redoc",
  openapi_url=f"{settings.API_V1_STR}/openapi.json",


)
app.include_router(api_router, prefix=settings.API_V1_STR)

