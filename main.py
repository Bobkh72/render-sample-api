from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
import os
from datetime import datetime

app = FastAPI()

MONGODB_URI = os.getenv("MONGODB_URI")
client = AsyncIOMotorClient(MONGODB_URI)
db = client.myDatabase  # replace with your DB name
products_collection = db.products

@app.get("/")
async def root():
    products_cursor = products_collection.find({})
    products = await products_cursor.to_list(length=100)  # get up to 100 products
    
    # Format products if needed (convert ObjectId to str)
    for p in products:
        p["_id"] = str(p["_id"])
        
    return {
        "datetime": datetime.now().isoformat(),
        "products": products
    }
