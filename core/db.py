from beanie import init_beanie
from configs import configs
from motor.motor_asyncio import AsyncIOMotorClient
from models import User

async def init_db():
    print("Initializing database...")
    client = AsyncIOMotorClient(configs.mongo_url, uuidRepresentation="standard")
    await init_beanie(database=client["gptbot_db"], document_models=[User])
    print("Database initialized!")
