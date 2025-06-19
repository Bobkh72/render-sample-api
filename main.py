from fastapi import FastAPI
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# MongoDB Connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client["mydb"]            # Change to your database name
collection = db["products"]    # Change to your collection name

app = FastAPI()

@app.get("/")
def read_root():
    products = list(collection.find({}, {"_id": 0}))
    return {
        "datetime": datetime.now().isoformat(),
        "products": products
    }
