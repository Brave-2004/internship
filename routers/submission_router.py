from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies import RoleChecker, get_current_user
from schemas.schema import SubmissionCreate, SubmissionGrade
from services import submission_service

router = APIRouter(
    prefix="/submission",
    tags=["submission"],
)


@router.post("/create")
async def submissionCreate(
        submission: SubmissionCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["student"]))
):
    return submission_service.submissionCreate(submission, db)


@router.get("/list")
async def submissionList(
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin", "teacher"]))
):
    return submission_service.submissionList(db)


@router.get("/byAssignment/{assignment_id}")
async def submissionsByAssignment(
        assignment_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin", "teacher"]))
):
    return submission_service.submissionsByAssignment(assignment_id, db)


@router.get("/{submission_id}")
async def submissionGet(
        submission_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return submission_service.submissionGet(submission_id, db)


@router.put("/grade/{submission_id}")
async def submissionGrade(
        submission_id: int,
        grade: SubmissionGrade,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin", "teacher"]))
):
    return submission_service.submissionGrade(submission_id, grade, db)


@router.delete("/delete/{submission_id}")
async def submissionDelete(
        submission_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin", "teacher"]))
):
    return submission_service.submissionDelete(submission_id, db)
