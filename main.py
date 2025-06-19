from fastapi import FastAPI
from pymongo import MongoClient
from bson.json_util import dumps
from fastapi.responses import JSONResponse

app = FastAPI()

MONGO_URI = "mongodb+srv://bobkhoury72:DRhqkTqJFlRsBkRf@cluster0.uz5b1qf.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client["MainDataBase"]
collection = db["walletHolders"]

@app.get("/items")
def read_items():
    try:
        items = list(collection.find({}, {
            "_id": 0,  # exclude MongoDB internal ID
            "holderName": 1,
            "walletId": 1,
            "walletNumber": 1,
            "BalanceDB_LBP": 1,
            "BalanceDB_USD": 1
        }))
        return JSONResponse(content=dumps(items), media_type="application/json")
    except Exception as e:
        return {"error": str(e)}
