from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from database import get_db
from dependencies import RoleChecker, get_current_user
from schemas.schema import DepartmentCreate
from services import department_service

router = APIRouter(
    prefix="/department",
    tags=["department"],
)


@router.post("/createDepartment")
async def departmentCreate(
        department: DepartmentCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return department_service.departmentCreate(department, db)


@router.get("/allDepartments")
async def departments(
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return department_service.departmentList(db)


@router.get("/departments/get/{department_id}")
async def departmentGet(
        department_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(get_current_user)
):
    return department_service.departmentGet(db, department_id)


@router.put("/departments/update/{department_id}")
async def departmentUpdate(
        department_id: int,
        department: DepartmentCreate,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return department_service.departmentUpdate(department,department_id, db)


@router.delete("/departments/{department_id}")
async def departmentDelete(
        department_id: int,
        db: Session = Depends(get_db),
        current_user: dict = Depends(RoleChecker(["admin"]))
):
    return department_service.departmentDelete(department_id, db)
