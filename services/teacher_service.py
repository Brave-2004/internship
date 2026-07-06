from sqlalchemy.orm import Session

from models.models import Teacher
from schemas.schema import TeacherCreate


def teacherCreate(db: Session, teacher: TeacherCreate):
    new_teacher = Teacher(**teacher.model_dump(by_alias=False))
    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)
    return "Teacher created"


def teacherUpdate(teacherUpdate: TeacherCreate, teacher_id: int, db: Session):
    teacher = db.query(Teacher).get(teacher_id)
    teacher.first_name = teacherUpdate.first_name
    teacher.last_name = teacherUpdate.last_name
    teacher.email = teacherUpdate.email
    teacher.salary = teacherUpdate.salary
    teacher.department_id = teacherUpdate.department_id
    db.add(teacher)
    db.commit()
    return "Teacher updated"


def teacherDelete(teacher_id: int, db: Session):
    teacher = db.query(Teacher).get(teacher_id)
    db.delete(teacher)
    db.commit()
    return "Teacher deleted"


def teacherList(db: Session):
    return db.query(Teacher).all()


def teacherGet(db: Session, teacher_id: int):
    return db.query(Teacher).get(teacher_id)
