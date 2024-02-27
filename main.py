# from app.api.v1.endpoints.users import user
from app.api.v1.endpoints.admins.admin import router_admin
from app.api.v1.endpoints.users.user import router_users
from fastapi import FastAPI
from uvicorn import run
from app.mongodb import mongo
from app.middleware import rate_limiting

app = FastAPI()
# Dependency to connect to MongoDB
app.add_event_handler("startup",mongo.connect_to_mongo)
app.add_event_handler("startup", rate_limiting.connect_Redis_ratelimiter)
app.add_event_handler("shutdown", mongo.close_mongo_connection)
app.add_event_handler("shutdown", rate_limiting.shutdown_redis_ratelimiter)

# app.include_router(user.router_users)
app.include_router(router_users)
app.include_router(router_admin)

if __name__ == "__main__":
    run("main:app", reload=True, host="0.0.0.0", port=4522)



