from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime

app = FastAPI()  # 👈 Make sure this line comes BEFORE any @app.get()

MONGO_URI = "mongodb+srv://bobkhoury72:DRhqkTqJFlRsBkRf@cluster0.uz5b1qf.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client["MainDataBase"]
wallets_collection = db["wallets"]

@app.get("/")
def read_wallets():
    wallets = list(wallets_collection.find({}, {"_id": 0}).limit(10))
    return {
        "datetime": datetime.now().isoformat(),
        "wallets": wallets
    }
