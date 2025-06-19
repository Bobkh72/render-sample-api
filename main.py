@app.get("/count")
def count_wallets():
    count = wallets_collection.count_documents({})
    return {"count": count}
