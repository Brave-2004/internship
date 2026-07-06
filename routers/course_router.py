from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies import RoleChecker, get_current_user
from schemas.schema import CourseCreate
from services import course_service

router = APIRouter(
    prefix="/course",
    tags=["course"],
)


@router.post("/create")
async def create_course(
        course_create: CourseCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return course_service.courseCreate(course_create, db)


@router.get("/courses")
async def get_courses(
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return course_service.courseList(db)


@router.get("/courseById")
async def get_course_by_id(
        course_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return course_service.courseGetById(course_id, db)


@router.put("/courseUpdate")
async def update_course(
        course_update: CourseCreate,
        course_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return course_service.courseUpdate(course_update, course_id, db)

@router.delete("/courseDelete")
async def delete_course(
        course_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return course_service.courseDelete(course_id, db)
