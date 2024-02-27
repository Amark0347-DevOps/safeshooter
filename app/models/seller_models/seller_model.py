from pydantic import BaseModel, ConfigDict, Field, EmailStr
from typing import Optional
#######################################################################################################
class ShopKeepar_Singup_Model(BaseModel):
    ''' This Model is used for Seller SingUp'''
    # id: Optional[PyObjectId] = Field(default_factory=uuid.uuid4, alias="_id")
    Name: str = Field(...)
    Email: EmailStr = Field(...)
    Phone: str = Field(...)
    Password: str = Field(...)
    UserType:Optional[str] = Field(default="Seller")
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "Name": "Jane Doe",
                "Email": "jdoe@gmail.com",
                "Phone": "+919056678462",
                "Password": "Aa@09107811",
                "UserType":"Seller"
            }
        },
    )


#######################################################################################################
class Shop_Detailes_Model(BaseModel):
    '''This Model is Used for Entered The Seller Details'''
    Shop_Name:str                                               
    Description:str
    Full_Address:str
    State:str
    City_Name:str
    PinCode:int
    Gali_No:str
    Nearest_Shop:str
    Categeory:str
    Shop_Image:str
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "Shop_Name":"Tip Top Cloth",                                        
                "Description":"This is very famous Shop",
                "Full_Address":"Punjab/Nawanshahr/Fateh-Nagar/Gali_No-15",
                "State":"Punjab",
                "City_Name":"Nawanshahr",
                "PinCode":144514,
                "Gali_No":"06",
                "Nearest_Shop":"PB32 Wale",
                "Categeory":"Retail",
                "Shop_Image":"http://google.com"
            }
        },
    )