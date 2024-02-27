from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from os import getenv
load_dotenv()

class Settings(BaseSettings):
    Mongodb_url:str = getenv("MONGODB_URL")

settings = Settings()
# app/core/config.py

from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    Mongodb_url: str = os.getenv("MONGO_URLN")
    jwt_secret_key: str = os.getenv("SECRET_KEY")
    algorithem: str = os.getenv("ALGORITHEM")
    Rate_limit_requests: int = os.getenv("RATE_LIMIT_REQUEST")
    Token_expire_minutes:int = os.getenv("TOKEN_EXPIRE_MINUTES")
    Redis_url:str = os.getenv("REDIS_URL")
settings = Settings()

