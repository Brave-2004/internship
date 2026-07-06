from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies import RoleChecker
from schemas.schema import EnrollmentCreate
from services import enrollment_service

router = APIRouter(
    prefix="/enrollment",
    tags=["enrollment"],
)


@router.post("/create")
async def create_enrollment(
        enrollment: EnrollmentCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return enrollment_service.enrollmentCreate(enrollment, db)


@router.get("/enrollmentGet/{enrollment_id}")
async def get_enrollment(
        enrollment_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin", "teacher"]))
):
    return enrollment_service.enrollmentGet(enrollment_id, db)


@router.get("/enrollmentList")
async def get_enrollments(
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin", "teacher"]))
):
    return enrollment_service.enrollmentList(db)


@router.put("/enrollmentUpdate/{enrollment_id}")
async def update_enrollment(
        enrollment_id: int,
        enrollment_update: EnrollmentCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return enrollment_service.enrollmentUpdate(enrollment_update, enrollment_id, db)

@router.delete("/enrollmentDelete/{enrollment_id}")
async def delete_enrollment(
        enrollment_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return enrollment_service.enrollmentDelete(enrollment_id, db)
