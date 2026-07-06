from fastapi import APIRouter, Depends
from dependencies import get_current_user
from schemas.schema import CommentCreate
from services import comment_service

router = APIRouter(
    prefix="/comment",
    tags=["comment"],
)


@router.post("/create")
async def commentCreate(
    data: CommentCreate,
    current_user: dict = Depends(get_current_user)
):
    return comment_service.commentCreate(data)


@router.get("/byLesson/{lesson_id}")
async def commentsByLesson(
    lesson_id: int,
    current_user: dict = Depends(get_current_user)
):
    return comment_service.commentsByLesson(lesson_id)


@router.delete("/delete/{comment_id}")
async def commentDelete(
    comment_id: str,
    current_user: dict = Depends(get_current_user)
):
    return comment_service.commentDelete(comment_id)
