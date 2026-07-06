from pymongo import MongoClient

from config import MONGO_URL

client = MongoClient(MONGO_URL)

db = client["university_db"]

activity_logs_collection = db["activity_logs"]
notifications_collection = db["notifications"]
comments_collection = db["comments"]