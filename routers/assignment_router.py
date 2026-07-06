from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies import RoleChecker, get_current_user
from schemas.schema import AssignmentCreate
from services import assignment_service

router = APIRouter(
    prefix="/assignment",
    tags=["assignment"],
)


@router.post("/create")
async def assignmentCreate(
        assignment: AssignmentCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin", "teacher"]))
):
    return assignment_service.assignmentCreate(assignment, db)


@router.get("/list")
async def assignmentList(
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return assignment_service.assignmentList(db)


@router.get("/byLesson/{lesson_id}")
async def assignmentsByLesson(
        lesson_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return assignment_service.assignmentsByLesson(lesson_id, db)


@router.get("/{assignment_id}")
async def assignmentGet(
        assignment_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return assignment_service.assignmentGet(assignment_id, db)


@router.put("/update/{assignment_id}")
async def assignmentUpdate(
        assignment_id: int,
        assignment: AssignmentCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin", "teacher"]))
):
    return assignment_service.assignmentUpdate(assignment, assignment_id, db)


@router.delete("/delete/{assignment_id}")
async def assignmentDelete(
        assignment_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin", "teacher"]))
):
    return assignment_service.assignmentDelete(assignment_id, db)
