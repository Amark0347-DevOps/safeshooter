
from fastapi import HTTPException, status
# import redis.asyncio as myredis
from redis.asyncio import Redis
from redis import RedisError
from fastapi_limiter import FastAPILimiter
from ..core.config import settings
# import httpx

class Myredis:
    def __init__(self) -> None:
        self.client =  Redis.from_url(settings.Redis_url, port=6379)

redisobj = Myredis()
async def connect_Redis_ratelimiter():
    try:
        await FastAPILimiter.init(redisobj.client)
        return await redisobj.client
    except RedisError as err:
        print(f"Error connecting to MongoDB: {err}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
async def shutdown_redis_ratelimiter():
    await redisobj.client.close()