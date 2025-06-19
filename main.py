from fastapi import FastAPI
from pymongo import MongoClient
from bson.json_util import dumps
from fastapi.responses import JSONResponse
import os

app = FastAPI()

# MongoDB connection string (use environment variable in production)
MONGO_URI = "mongodb+srv://bobkhoury72:DRhqkTqJFlRsBkRf@cluster0.uz5b1qf.mongodb.net/"
client = MongoClient(MONGO_URI)

# Select the database and collection
db = client["MainDataBase"]
collection = db["walletHolders"]

@app.get("/items")
def read_items():
    try:
        items = list(collection.find())
        return JSONResponse(content=dumps(items), media_type="application/json")
    except Exception as e:
        return {"error": str(e)}
