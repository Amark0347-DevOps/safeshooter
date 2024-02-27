# from cryptography.fernet import Fernet
# from fastapi import Depends,HTTPException, status
# from ..core.dependencies import root
# from cryptography.fernet import InvalidToken
# from ..core.config import settings

# # Generate a random 256-bit AES key one time the use This Secret key every encryption
# # key = Fernet.generate_key()
# # print(key)
# #######################################Generate Encryption key#######################################
# secret_key_for_singup = settings.Singuploginkey_secret_key

# async def encrypt_api_key(secret_key_for_singup):
#     ''' Secret Key first method Encryption'''
#     key1 = Fernet(f"{settings.Singuploginkey}=")
#     encrypted_data = key1.encrypt(secret_key_for_singup.encode())
#     return encrypted_data.decode()


# #######################################Decrypt Encryption key#######################################
# async def decrypt_api_key(encrypted_api_key:str = Depends(root)):
#     try:
#         key1 = Fernet(f"{settings.Singuploginkey}=")
#         decrypted_data = key1.decrypt(encrypted_api_key.encode())
#         return decrypted_data.decode()
#     except InvalidToken as c:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="UNAUTHORIZED ACCESS")



# #######################################Check key is True or Not#######################################
# async def authenticate_user(captured_key:str = Depends(decrypt_api_key)):
#     if captured_key == secret_key_for_singup:
#         return True
#     else:
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized you dont Access")
