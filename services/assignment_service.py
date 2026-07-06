from dns.immutable import Dict
from sqlalchemy.orm import Session

from models.models import Assignment, User
from schemas.schema import AssignmentCreate


def assignmentCreate(assignmentCreate: AssignmentCreate, db: Session):
    new_assignment = Assignment(**assignmentCreate.model_dump(by_alias=False))
    db.add(new_assignment)
    db.commit()
    db.refresh(new_assignment)
    return "Assignment created"


def assignmentList(db: Session):
    return db.query(Assignment).all()


def assignmentGet(assignment_id: int, db: Session):
    return db.query(Assignment).get(assignment_id)


def assignmentsByLesson(lesson_id: int, db: Session):
    return db.query(Assignment).filter(Assignment.lesson_id == lesson_id).all()


def assignmentUpdate(assignmentUpdate: AssignmentCreate, assignment_id: int, db: Session):
    assignment = db.query(Assignment).get(assignment_id)
    assignment.title = assignmentUpdate.title
    assignment.description = assignmentUpdate.description
    assignment.deadline = assignmentUpdate.deadline
    assignment.max_score = assignmentUpdate.max_score
    assignment.lesson_id = assignmentUpdate.lesson_id
    assignment.course_id = assignmentUpdate.course_id
    assignment.teacher_id = assignmentUpdate.teacher_id
    db.add(assignment)
    db.commit()
    return "Assignment updated"


def assignmentDelete(assignment_id: int, db: Session):
    assignment = db.query(Assignment).get(assignment_id)
    db.delete(assignment)
    db.commit()
    return "Assignment deleted"
