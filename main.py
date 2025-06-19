@app.get("/")
def debug_mongo():
    try:
        # Step 1: Check connection
        db_names = client.list_database_names()

        # Step 2: Confirm if MainDataBase exists
        if "MainDataBase" not in db_names:
            return {"error": "Database 'MainDataBase' not found", "databases": db_names}

        # Step 3: List collections in the database
        collections = db.list_collection_names()

        # Step 4: Check if 'wallets' collection exists
        if "wallets" not in collections:
            return {"error": "'wallets' collection not found", "collections": collections}

        # Step 5: Get a sample document
        sample = wallets_collection.find_one()

        return {
            "status": "Connection OK",
            "databases": db_names,
            "collections": collections,
            "sample_wallet": sample
        }

    except Exception as e:
        return {"error": str(e)}
