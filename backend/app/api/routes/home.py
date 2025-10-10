from fastapi import APIRouter

router = APIRouter(prefix="/home")

@router.get("/")
def home():
  return {"message":"WELCOME TO HOMEPAGE!"}