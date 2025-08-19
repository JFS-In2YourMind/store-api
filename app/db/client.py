from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config

MONGO_URI = config("MONGO_URI", default="mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_URI)
db = client.store_db
product_collection = db.get_collection("products")
