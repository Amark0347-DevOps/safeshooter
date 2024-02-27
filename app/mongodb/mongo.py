from fastapi import HTTPException, status
from pymongo.errors import ServerSelectionTimeoutError
from motor.motor_asyncio import AsyncIOMotorClient
from ..core import config
class MotorDB:
    def __init__(self):
        self.client = AsyncIOMotorClient(config.settings.Mongodb_url, maxPoolSize=10, minPoolSize=5)
motor_db = MotorDB()

async def connect_to_mongo():

    try:
        # motor_db.client = AsyncIOMotorClient(settings.mongodb_url, maxPoolSize=10, minPoolSize=5)
        return motor_db.client
    except ServerSelectionTimeoutError as err:
        print(f"Error connecting to MongoDB: {err}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


async def close_mongo_connection():
    return motor_db.client.close()
