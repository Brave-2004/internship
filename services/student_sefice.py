from sqlalchemy.orm import Session

from models.models import Student
from schemas.schema import StudentCreate


def studentCreate(studentCreate: StudentCreate, db: Session):
    student = Student(**studentCreate.model_dump())
    db.add(student)
    db.commit()
    db.refresh(student)
    return "Student created"

def studentGetAll(db: Session):
    return db.query(Student).all()

def studentDelete(db: Session, id: int):
    student = db.query(Student).get(id)
    db.delete(student)
    db.commit()
    return "Student deleted"

def studentGet(db: Session, id: int):
    student = db.query(Student).get(id)
    return student

def studentUpdate(db: Session, id: int, studentUpdate: StudentCreate):
    student = db.query(Student).get(id)
    student.name = studentUpdate.name
    student.email = studentUpdate.email
    student.age = studentUpdate.age
    student.department_id = studentUpdate.department_id
    db.add(student)
    db.commit()
    db.refresh(student)
    return "Student updated"
