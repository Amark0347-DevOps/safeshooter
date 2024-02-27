
from datetime import datetime, timedelta
from jose import JWTError, jwt
# import jwt
from fastapi import Depends
from fastapi import HTTPException
from ..core.config import settings
from fastapi import status
from typing import Optional
import json
from ..core.dependencies import root


#################################################################################################
# async def create_jwt_token(data: dict) -> str:
#     to_encode = data.copy()
#     expire = datetime.utcnow() + timedelta(minutes=settings.Token_expire_minutes)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, settings.Secret_key, algorithm=settings.Algorithm)
#     return encoded_jwt
# ##################################################################################################################
# async def decode_jwt_token(token: str):
#     print(f"two",token)
#     credentials_exception = HTTPException(
#         status_code=401,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, settings.Secret_key, algorithms=settings.Algorithm)
#         username = payload.get("sub")
#         if username is None:
#             raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials toekn is Empty")
#         else:
#             return username
#     except JWTError:
#         raise credentials_exception
# ##############################################################################################################


async def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = (datetime.utcnow() + timedelta(minutes=30))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.jwt_secret_key, algorithm=settings.algorithem)
    return encoded_jwt
##################################################Get Jwt Token using Request and get Current User ###############################


async def get_current_user(token: str = Depends(root)):
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.algorithem])
        username = payload.get("sub")
        print(username)
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="1,not validate credentials")
        return username
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="2,not validate credentials")