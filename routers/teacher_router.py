from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies import RoleChecker, get_current_user
from schemas.schema import TeacherCreate
from services import teacher_service

router = APIRouter(
    prefix="/teacher",
    tags=["teacher"],
)


@router.post("/create")
async def teacherCreate(
        teacher: TeacherCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return teacher_service.teacherCreate(db, teacher)


@router.get("/list")
async def teacherList(
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return teacher_service.teacherList(db)


@router.get("/{teacher_id}")
async def teacherGet(
        teacher_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return teacher_service.teacherGet(db, teacher_id)


@router.put("/update/{teacher_id}")
async def teacherUpdate(
        teacher_id: int,
        teacher: TeacherCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return teacher_service.teacherUpdate(teacher, teacher_id, db)


@router.delete("/delete/{teacher_id}")
async def teacherDelete(
        teacher_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return teacher_service.teacherDelete(teacher_id, db)
