from fastapi import Depends, HTTPException, Request, status
# from ..security.jwt_auth import decode_jwt_token
##################################################################################
# async def root(request: Request):
#     re = request.headers.get("Authorization")
#     if re:
#         return re.removeprefix("Bearer ")
#     else:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized Request")
async def root(request: Request):
    re = request.headers.get("Authorization")
    if re is None:
        raise HTTPException(detail="unauthorized Access", status_code=status.HTTP_401_UNAUTHORIZED)
    else:
        return re.removeprefix("Bearer ")

##################################################################################
# async def get_current_user(token: str = Depends(root)):
#     credentials_exception = HTTPException(
#         status_code=401,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     print(f"one token", token)
#     payload = await decode_jwt_token(token)
#     if payload:
#         print(payload)
#         # print(payload["sub"]["phone"])
#     else:
#         raise credentials_exception
##################################################################################