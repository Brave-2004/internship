from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas.schema import UserRegister, UserLogin
from services import auth_service

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register")
async def register(
        data: UserRegister,
        db: Session = Depends(get_db),
):
    result = auth_service.register(data, db)
    if result is None:
        raise HTTPException(status_code=400, detail="Email already registered")
    return result


@router.post("/login")
async def login(
        data: UserLogin,
        db: Session = Depends(get_db),
):
    result = auth_service.login(data, db)
    if result is None:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return result
