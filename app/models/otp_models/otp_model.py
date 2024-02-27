from pydantic import BaseModel, ConfigDict
class OTP_Verification(BaseModel):
    OTP:str
    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_schema_extra={
            "example": {
                "OTP": "121530"
            }
        },
    )