from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies import RoleChecker
from schemas.schema import StudentCreate
from services import student_service

router = APIRouter(
    prefix="/api/student",
    tags=["Students"],
)


@router.post("/create")
async def studentCreate(
        student: StudentCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return student_service.studentCreate(student, db)


@router.get("/students")
async def studentList(
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin", "teacher"]))
):
    return student_service.studentGetAll(db)


@router.get("/students/{student_id}")
async def studentGet(
        student_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin", "teacher"]))
):
    return student_service.studentGet(db, student_id)


@router.put("/students/{student_id}")
async def studentUpdate(
        student_id: int,
        student: StudentCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return student_service.studentUpdate(db, student_id, student)


@router.delete("/students/{student_id}")
async def studentDelete(
        student_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return student_service.studentDelete(db, student_id)
