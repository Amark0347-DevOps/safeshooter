from fastapi import HTTPException, status
from motor.motor_asyncio import AsyncIOMotorClient
from ...models.user_models.admin_model_response import Admin_Login_Response, Admin_SingUp_Response, Add_Trainer_Response
from ...security.jwt_auth import create_access_token
from fastapi.encoders import jsonable_encoder
from datetime import datetime, timedelta
from ...core.config import settings

class AdminService:
    def __init__(self, database: AsyncIOMotorClient):
        self.db = database.get_database("safeshooters")
        self.adminCollection = self.db.get_collection("Admin")
        self.trainersCollection = self.db.get_collection("Trainers")
##########################################################################################################
    async def Singup_Admin(self, singup_data) -> Admin_SingUp_Response:
        '''SingUP ShopKeepar Logic'''
        if await self.adminCollection.find_one({"phone":singup_data.phone}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Number Already Registered")
        elif await self.adminCollection.find_one({"email":singup_data.email}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email Already Registered")
        else:
            result = await self.adminCollection.insert_one(jsonable_encoder(singup_data))
            re1 = await self.adminCollection.find_one({"_id": result.inserted_id})
            data1 = {"firstName": re1["firstName"],"lastName": re1["lastName"],"email": re1["email"],"phone": re1["phone"]}
            token = await create_access_token({"sub":data1},expires_delta=timedelta(minutes=int(settings.Token_expire_minutes)))
            re1["token"] = token
            return Admin_SingUp_Response(**re1)

############################################################################################################################
    async def Login_Admin(self, login_data) -> Admin_Login_Response:
        re1 = await self.adminCollection.find_one({"email":login_data.email})
        if re1:
            if re1["password"]==login_data.password:
                # data1 = {"firstName": re1["firstName"],"lastName": re1["lastName"],"email": re1["email"],"phone": re1["phone"]}
                token = await create_access_token({"sub":re1["phone"]},expires_delta=timedelta(minutes=int(settings.Token_expire_minutes)))
                re1["token"] = token
                return Admin_Login_Response(**re1)
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Password")
        else:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Dont have Permissions")
###########################################################################################################
    async def add_trainer(self, data)-> Add_Trainer_Response:
        if await self.adminCollection.find_one({"Phone":data.Phone}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Number Already Registered")
        elif await self.adminCollection.find_one({"Email":data.Email}):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email Already Registered")
        else:
            re = await self.trainersCollection.insert_one(jsonable_encoder(data))
            if re:
                re1 = await self.trainersCollection.find_one({"_id":re.inserted_id})
                return Add_Trainer_Response(**re1)
            else:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Tariner Not Added Some Issues ")

    # async def add_shop_keepar_details(self, data) -> Shop_Detailes_Model:
    #     ''' Add Shopkeepar Details Logic'''
    #     result = await self.ShopCollection.insert_one(jsonable_encoder(data))
    #     details = await self.ShopCollection.find_one({"_id":result.inserted_id})
    #     return Shop_Detailes_Model(**details)
    
###########################################################################################################

