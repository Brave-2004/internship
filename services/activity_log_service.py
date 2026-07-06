from datetime import datetime

from database_mongo import activity_logs_collection


def logActivity(user_id: int, action: str, ip_address: str = "unknown"):
    log = {
        "user_id": user_id,
        "action": action,
        "ip_address": ip_address,
        "created_at": datetime.utcnow(),
    }
    activity_logs_collection.insert_one(log)


def getLogs(user_id: int):
    docs = activity_logs_collection.find({"user_id": user_id})
    return [
        {
            "id": str(doc["_id"]),
            "user_id": doc["user_id"],
            "action": doc["action"],
            "ip_address": doc["ip_address"],
            "created_at": doc["created_at"],
        }
        for doc in docs
    ]
