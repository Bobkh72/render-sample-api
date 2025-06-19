from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "datetime": datetime.now().isoformat(),
        "products": [
            {"id": 1, "name": "Laptop", "price": 999.99},
            {"id": 2, "name": "Smartphone", "price": 699.99},
            {"id": 3, "name": "Headphones", "price": 150.99}
        ]
    }
