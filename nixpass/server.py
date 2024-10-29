from . import database, config
from fastapi import FastAPI
import os

nixpass_server = FastAPI()
nixpass_config = config.config_read(os.getenv("SERVER_CONFIG"))
nixpass_db = database.Database(
    host=nixpass_config["database"]["host"],
    port=nixpass_config["database"]["port"],
    user=nixpass_config["database"]["user"],
    password=nixpass_config["database"]["password"],
    name=nixpass_config["database"]["name"]
)

@nixpass_server.get("/")
async def root():
    return {"message": "Hello from NixPass !"}
