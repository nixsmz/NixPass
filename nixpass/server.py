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
    return {"message": "C'est le pass qui te permet d'entrer dans une faille spatio-temporelle de l'helicopter-kiting."}
