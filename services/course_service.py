from sqlalchemy.orm import Session

from models.models import Course
from schemas.schema import CourseCreate


def courseCreate(courseCreate: CourseCreate, db: Session):
    new_course = Course(**courseCreate.model_dump(by_alias=False))
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
    return "Course created"


def courseList(db: Session):
    return db.query(Course).all()


def courseGetById(course_id: int, db: Session):
    return db.query(Course).get(course_id)


def courseUpdate(courseUpdate: CourseCreate, course_id: int, db: Session):
    course = db.query(Course).get(course_id)
    course.name = courseUpdate.name
    course.credits = courseUpdate.credits
    course.teacher_id = courseUpdate.teacher_id
    course.department_id = courseUpdate.department_id
    db.add(course)
    db.commit()
    return "Course updated"


def courseDelete(course_id: int, db: Session):
    course = db.query(Course).get(course_id)
    db.delete(course)
    db.commit()
    return "Course deleted"
