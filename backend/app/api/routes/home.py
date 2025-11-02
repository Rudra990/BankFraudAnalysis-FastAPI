from fastapi import APIRouter
from backend.app.core.logging import get_logger

logger = get_logger()

router = APIRouter(prefix="/home")

@router.get("/")
def home():
  logger.info("Home page accessed")  ##for testing logging
  logger.debug("Home page accessed")
  logger.error("Home page accessed")
  return {"message":"WELCOME TO HOMEPAGE!"}