from fastapi import  Depends
from .....models.user_models.admin_model import Admin_SingUp, Admin_Login, Add_Trainer
from motor.motor_asyncio import AsyncIOMotorClient
from .....services.admin.admins import AdminService
from .....mongodb.mongo import connect_to_mongo
# from .....core.dependencies import get_current_user
from .....security.jwt_auth import get_current_user
from fastapi_limiter.depends import RateLimiter
from ...routers.router import router_admin
# from .....security.encryption import authenticate_user


@router_admin.post("/v1/admin/singup", description="Admin Singup Endpoints",dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def create_user(data: Admin_SingUp, db: AsyncIOMotorClient = Depends(connect_to_mongo)):
    admin_service = AdminService(db)
    return await admin_service.Singup_Admin(data)

@router_admin.post("/v1/admin/login", description="Admin Login Endpoints", dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def read_user(data: Admin_Login, db: AsyncIOMotorClient = Depends(connect_to_mongo)):
    admin_service = AdminService(db)
    user = await admin_service.Login_Admin(data)
    return user

@router_admin.post("/v1/admin/add_trainer", description="Check User details By Phone Number", dependencies=[Depends(RateLimiter(times=50, minutes=10))])
async def Find_User_By_Phone_Number(data:Add_Trainer, db: AsyncIOMotorClient = Depends(connect_to_mongo), token:str = Depends(get_current_user)):
    admin_service = AdminService(db)
    user = await admin_service.add_trainer(data)
    # await redis_service.add_data_in_redis(token, user)
    return user
