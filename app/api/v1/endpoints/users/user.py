from fastapi import  Depends
from .....models.user_models.user_model import User_SingUp, User_Login
from motor.motor_asyncio import AsyncIOMotorClient
from .....services.user_services.user_service import UserService
from .....mongodb.mongo import connect_to_mongo
# from .....core.dependencies import get_current_user
from fastapi_limiter.depends import RateLimiter
from ...routers.router import router_users
# from .....security.encryption import authenticate_user


@router_users.post("/v1/users/singup", description="User Singup Endpoints",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def create_user(data: User_SingUp, db: AsyncIOMotorClient = Depends(connect_to_mongo)):
    user_service = UserService(db)
    return await user_service.Singup_User(data)

@router_users.post("/v1/users/login", description="User Login Endpoints", dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def read_user(data: User_Login, db: AsyncIOMotorClient = Depends(connect_to_mongo)):
    user_service = UserService(db)
    user = await user_service.Login_User(data)
    return user

# @router_users.get("/v1/users/user", description="Check User details By Phone Number", dependencies=[Depends(RateLimiter(times=50, minutes=10))])
# async def Find_User_By_Phone_Number(db: AsyncIOMotorClient = Depends(connect_to_mongo), token:str = Depends(get_current_user)):
#     # Redis_db:Redis = Depends(connect_Redis_ratelimiter)
#     # url = Redis(host="localhost", port=6379, db=0)
#     # redis_service = Redis_Service()
#     # re = await redis_service.get_data_in_redis(token)
#     # if re != None:
#     #     return re 
#     # else:
#     user_service = UserService(db)
#     user = await user_service.find_user_by_phone(token)
#     # await redis_service.add_data_in_redis(token, user)
#     return user
