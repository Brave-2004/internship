from datetime import datetime, timedelta

import bcrypt
from jose import jwt
from sqlalchemy.orm import Session

from models.models import User
from schemas.schema import UserRegister, UserLogin, TokenResponse
from config import SECRET_KEY

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def hashPassword(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verifyPassword(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())


def createAccessToken(data: dict) -> str:
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({"exp": expire})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verifyToken(token: str) -> dict:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


def register(data: UserRegister, db: Session):
    existing = db.query(User).filter(User.email == data.email).first()
    if existing:
        return None  # email already taken

    new_user = User(
        email=data.email,
        hashed_password=hashPassword(data.password),
        role=data.role,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return "User registered"


def login(data: UserLogin, db: Session):
    user = db.query(User).filter(User.email == data.email).first()
    if not user or not verifyPassword(data.password, user.hashed_password):
        return None  # invalid credentials

    token = createAccessToken({"sub": user.email, "role": user.role, "id": user.id})
    return TokenResponse(access_token=token)
