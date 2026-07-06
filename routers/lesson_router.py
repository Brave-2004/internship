from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies import RoleChecker, get_current_user
from schemas.schema import LessonCreate
from services import lesson_service

router = APIRouter(
    prefix="/lesson",
    tags=["lesson"],
)


@router.post("/create")
async def lessonCreate(
        lesson: LessonCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin", "teacher"]))
):
    return lesson_service.lessonCreate(lesson, db)


@router.get("/list")
async def lessonList(
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return lesson_service.lessonList(db)


@router.get("/byCourse/{course_id}")
async def lessonsByCourse(
        course_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return lesson_service.lessonsByCourse(course_id, db)


@router.get("/{lesson_id}")
async def lessonGet(
        lesson_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return lesson_service.lessonGet(lesson_id, db)


@router.put("/update/{lesson_id}")
async def lessonUpdate(
        lesson_id: int,
        lesson: LessonCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin", "teacher"]))
):
    return lesson_service.lessonUpdate(lesson, lesson_id, db)


@router.delete("/delete/{lesson_id}")
async def lessonDelete(
        lesson_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin", "teacher"]))
):
    return lesson_service.lessonDelete(lesson_id, db)
