@app.get("/")
def read_wallets():
    try:
        wallets = list(wallets_collection.find().limit(10))  # no projection
        return {
            "datetime": datetime.now().isoformat(),
            "wallets": wallets
        }
    except Exception as e:
        return {"error": str(e)}
