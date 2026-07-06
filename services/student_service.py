from sqlalchemy.orm import Session

from models.models import Student
from schemas.schema import StudentCreate


def studentCreate(studentCreate: StudentCreate, db: Session):
    new_student = Student(**studentCreate.model_dump(by_alias=False))
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return "Student created"


def studentGetAll(db: Session):
    return db.query(Student).all()


def studentGet(db: Session, student_id: int):
    return db.query(Student).get(student_id)


def studentUpdate(db: Session, student_id: int, studentUpdate: StudentCreate):
    student = db.query(Student).get(student_id)
    student.first_name = studentUpdate.first_name
    student.last_name = studentUpdate.last_name
    student.email = studentUpdate.email
    student.age = studentUpdate.age
    student.department_id = studentUpdate.department_id
    db.add(student)
    db.commit()
    db.refresh(student)
    return "Student updated"


def studentDelete(db: Session, student_id: int):
    student = db.query(Student).get(student_id)
    db.delete(student)
    db.commit()
    return "Student deleted"
