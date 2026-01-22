from datetime import datetime, timedelta, timezone
from typing import Annotated
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from sqlmodel import Session, select

from app.core.sequrity import get_password_hashed, get_user_by_email, verify_password
from app.core.config import settings
from app.databases.session import get_session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

oauth2_schema = OAuth2PasswordBearer(tokenUrl="/api/auth/token")
    
def authenticate_user(session: Session, email: str, password: str):
    user = get_user_by_email(session, email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    
    return user

def create_access_token(
    user_id: int, 
    expires_delta: timedelta | None = None
):
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    payload = {
        "sub": str(user_id),
        "exp": expire
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(
    token: Annotated[str, Depends(oauth2_schema)], 
    session: Session = Depends(get_session)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
    
    user = session.get(User, int(user_id))
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive User")
    return current_user

def create_user(session: Session, user_in: UserCreate) -> User:
    existing_user = session.exec(
        select(User).where(User.name == user_in.name)
    ).first()
    
    if existing_user:
        raise ValueError("Username already exist")
    
    user = User(
        name=user_in.name,
        email=user_in.email,
        hashed_password=get_password_hashed(user_in.password)
    )
    
    session.add(user)
    session.commit()
    session.refresh(user)
    return user