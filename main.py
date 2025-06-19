from fastapi import FastAPI
from pymongo import MongoClient
from bson.json_util import dumps
from fastapi.responses import JSONResponse
from datetime import datetime

app = FastAPI()

# MongoDB connection
MONGO_URI = "mongodb+srv://bobkhoury72:DRhqkTqJFlRsBkRf@cluster0.uz5b1qf.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client["MainDataBase"]  # adjust if your DB name is different
wallets_collection = db["wallets"]

@app.get("/")
def read_wallets():
    try:
        # Get all wallets (limit to first 10 for performance)
        wallets = list(wallets_collection.find({}, {"_id": 0}).limit(10))
        
        return {
            "datetime": datetime.now().isoformat(),
            "wallets": wallets
        }
    except Exception as e:
        return {"error": str(e)}
