from fastapi import APIRouter, Depends, HTTPException
from app.schemas.user import UserCreate, UserOut
from app.services.user_service import UserService
from app.core.security import get_current_user

router = APIRouter()

@router.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, service: UserService = Depends()):
    return service.create_user(user)

@router.get("/users/me/", response_model=UserOut)
def read_user_me(current_user: UserOut = Depends(get_current_user)):
    return current_user