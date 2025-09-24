from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv()

# Mongo URI and DB name
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

if not MONGO_URI:
    raise ValueError("❌ MONGO_URI is missing in .env")
if not DB_NAME:
    raise ValueError("❌ DB_NAME is missing in .env")

# Create async client
try:
    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DB_NAME]

    # Collections
    users_collection = db["users"]
    sessions_collection = db["sessions"]
    attendance_collection = db["attendance"]

    logging.info(f"✅ Connected to MongoDB database: {DB_NAME}")

except Exception as e:
    logging.error(f"❌ MongoDB connection failed: {e}")
    raise
