from sqlalchemy.orm import Session

from models.models import Lesson
from schemas.schema import LessonCreate


def lessonCreate(lessonCreate: LessonCreate, db: Session):
    new_lesson = Lesson(**lessonCreate.model_dump(by_alias=False))
    db.add(new_lesson)
    db.commit()
    db.refresh(new_lesson)
    return "Lesson created"


def lessonList(db: Session):
    return db.query(Lesson).all()


def lessonGet(lesson_id: int, db: Session):
    return db.query(Lesson).get(lesson_id)


def lessonsByCourse(course_id: int, db: Session):
    return db.query(Lesson).filter(Lesson.course_id == course_id).all()


def lessonUpdate(lessonUpdate: LessonCreate, lesson_id: int, db: Session):
    lesson = db.query(Lesson).get(lesson_id)
    lesson.title = lessonUpdate.title
    lesson.description = lessonUpdate.description
    lesson.order = lessonUpdate.order
    lesson.course_id = lessonUpdate.course_id
    db.add(lesson)
    db.commit()
    return "Lesson updated"


def lessonDelete(lesson_id: int, db: Session):
    lesson = db.query(Lesson).get(lesson_id)
    db.delete(lesson)
    db.commit()
    return "Lesson deleted"
