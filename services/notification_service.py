from datetime import datetime

from database_mongo import notifications_collection
from schemas.schema import NotificationCreate


def _serialize(doc) -> dict:
    doc["id"] = str(doc.pop("_id"))
    return doc


def notificationCreate(data: NotificationCreate):
    notification = {
        "user_id": data.user_id,
        "message": data.message,
        "is_read": False,
        "created_at": datetime.utcnow(),
    }
    notifications_collection.insert_one(notification)
    return "Notification created"


def notificationList(user_id: int):
    docs = notifications_collection.find({"user_id": user_id})
    return [_serialize(doc) for doc in docs]


def notificationMarkRead(notification_id: str):
    notifications_collection.update_one(
        {"_id": notification_id},
        {"$set": {"is_read": True}},
    )
    return "Notification marked as read"


def notificationDelete(notification_id: str):
    notifications_collection.delete_one({"_id": notification_id})
    return "Notification deleted"
