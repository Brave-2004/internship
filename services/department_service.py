from sqlalchemy.orm import Session

from models.models import Department
from schemas.schema import DepartmentCreate


def departmentCreate(department: DepartmentCreate, db: Session):
    department = Department(**department.model_dump())
    db.add(department)
    db.commit()
    db.refresh(department)
    return "Department created"

def departmentUpdate(departmentUpdate: DepartmentCreate, id:int, db: Session):
    department = db.query(Department).get(id)
    department.name = departmentUpdate.name
    db.add(department)
    db.commit()
    return "Department updated"

def departmentDelete(id:int, db: Session):
    department = db.query(Department).get(id)
    db.delete(department)
    db.commit()
    return "Department deleted"

def departmentList(db: Session):
    return db.query(Department).all()

def departmentGet(db: Session, id:int):
    return db.query(Department).get(id)



