# test_connection.py
import asyncio
from src.db.connection import check_connection, users_collection

async def main():
    # test connection
    await check_connection()

    # insert a test user
    result = await users_collection.insert_one({"name": "Shiva", "email": "shiva.test@example.com"})
    print("✅ Inserted test user with _id:", result.inserted_id)

    # find the same user
    user = await users_collection.find_one({"email": "shiva.test@example.com"})
    print("✅ Found user in DB:", user)

asyncio.run(main())
