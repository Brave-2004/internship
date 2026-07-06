from datetime import datetime

from database_mongo import comments_collection
from schemas.schema import CommentCreate


def _serialize(doc) -> dict:
    doc["id"] = str(doc.pop("_id"))
    return doc


def commentCreate(data: CommentCreate):
    comment = {
        "lesson_id": data.lesson_id,
        "user_id": data.user_id,
        "content": data.content,
        "created_at": datetime.utcnow(),
    }
    comments_collection.insert_one(comment)
    return "Comment created"


def commentsByLesson(lesson_id: int):
    docs = comments_collection.find({"lesson_id": lesson_id})
    return [_serialize(doc) for doc in docs]


def commentDelete(comment_id: str):
    comments_collection.delete_one({"_id": comment_id})
    return "Comment deleted"
