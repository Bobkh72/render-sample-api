from fastapi import FastAPI
from pymongo import MongoClient
from datetime import datetime

app = FastAPI()

# MongoDB connection string - specify DB name and options
MONGO_URI = "mongodb+srv://bobkhoury72:DRhqkTqJFlRsBkRf@cluster0.uz5b1qf.mongodb.net/MainDataBase?retryWrites=true&w=majority"
client = MongoClient(MONGO_URI)

# Select your database and collection
db = client["MainDataBase"]
wallets_collection = db["WalletSequences"]

@app.get("/")
def read_wallets():
    try:
        # Fetch up to 10 wallets, excluding MongoDB _id field
        wallets_cursor = wallets_collection.find({}, {"_id": 0}).limit(10)
        wallets = list(wallets_cursor)
        
        print(f"Found {len(wallets)} wallets")  # For debugging in logs
        
        return {
            "datetime": datetime.now().isoformat(),
            "wallets": wallets 
        }
    except Exception as e:
        return {"error": str(e)}

@app.get("/count")
def count_wallets():
    try:
        count = wallets_collection.count_documents({})
        return {"count": count}
    except Exception as e:
        return {"error": str(e)}
