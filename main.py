from fastapi import FastAPI
from datetime import datetime
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Connect to MongoDB Atlas
client = MongoClient(os.getenv("MONGO_URI"))
db = client["your_db_name"]          # Replace with your DB name
collection = db["products"]          # Replace with your collection name

app = FastAPI()

@app.get("/")
def read_root():
    # Fetch all products from MongoDB
    products = list(collection.find({}, {"_id": 0}))  # Exclude _id from results
    return {
        "datetime": datetime.now().isoformat(),
        "products": products
    }
