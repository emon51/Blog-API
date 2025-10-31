'''
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Collections
users_collection = db["users"]
posts_collection = db["posts"]
comments_collection = db["comments"]
'''

from motor.motor_asyncio import AsyncIOMotorClient 
from dotenv import load_dotenv
import os

# Load environment variables from .env.
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# Connect to MongoDB asynchronously
client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]

# Collections.
posts_collection = db["posts"]   # Stores posts
comments_collection = db["comments"]    # Stores comments.

# Optional (Database connection test).
try:
    client.admin.command('ping')
    print("Successfully connected to MongoDB!")
except Exception as e:
    print(e)