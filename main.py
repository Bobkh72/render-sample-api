from fastapi import FastAPI
from pymongo import MongoClient
from bson.json_util import dumps
import os

app = FastAPI()

# MongoDB connection string
MONGO_URI = "mongodb+srv://bobkhoury72:DRhqkTqJFlRsBkRf@cluster0.uz5b1qf.mongodb.net/"
client = MongoClient(MONGO_URI)

# Select the database and collection
db = client["MainDataBase"]  # <-- Replace with your database name
collection = db["walletHolders"]  # <-- Replace with your collection name

@app.get("/items")
def read_items():
    items = list(collection.find())
    return dumps(items)
