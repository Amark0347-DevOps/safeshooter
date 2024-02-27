# from ..core.config import settings
import aioredis
import asyncio
# async def RedisCaching():
#     redis_pool = await aioredis.create_redis_pool(settings.Redis_url)
#     await redis_pool.set("")
async def main():
    # Create a Redis connection pool
    redis_pool = await aioredis.create_redis_pool('redis://localhost:6379/0')

    # Example: Set a key-value pair
    await redis_pool.set('my_key', 'my_value')

    # Example: Get the value for a key
    result = await redis_pool.get('my_key')
    print(f"Value for 'my_key': {result.decode('utf-8')}")

    # Close the Redis connection pool
    redis_pool.close()
    await redis_pool.wait_closed()

# Run the asyncio event loop
asyncio.run(main())