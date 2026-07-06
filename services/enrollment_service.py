from sqlalchemy.orm import Session

from models.models import Enrollment
from schemas.schema import EnrollmentCreate


def enrollmentCreate(enrollmentCreate: EnrollmentCreate, db: Session):
    new_enrollment = Enrollment(**enrollmentCreate.model_dump(by_alias=False))
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return "Enrollment created"


def enrollmentList(db: Session):
    return db.query(Enrollment).all()


def enrollmentGet(enrollment_id: int, db: Session):
    return db.query(Enrollment).get(enrollment_id)


def enrollmentUpdate(enrollmentUpdate: EnrollmentCreate, enrollment_id: int, db: Session):
    enrollment = db.query(Enrollment).get(enrollment_id)
    enrollment.student_id = enrollmentUpdate.student_id
    enrollment.course_id = enrollmentUpdate.course_id
    enrollment.semester = enrollmentUpdate.semester
    enrollment.grade = enrollmentUpdate.grade
    db.add(enrollment)
    db.commit()
    return "Enrollment updated"


def enrollmentDelete(enrollment_id: int, db: Session):
    enrollment = db.query(Enrollment).get(enrollment_id)
    db.delete(enrollment)
    db.commit()
    return "Enrollment deleted"
