from datetime import datetime

from sqlalchemy.orm import Session

from models.models import Submission
from schemas.schema import SubmissionCreate, SubmissionGrade
from tasks.email_tasks import send_submission_confirmation, send_grade_notification


def submissionCreate(submissionCreate: SubmissionCreate, db: Session):
    new_submission = Submission(
        **submissionCreate.model_dump(by_alias=False),
        submitted_at=datetime.utcnow(),
        status="pending",
    )
    db.add(new_submission)
    db.commit()
    db.refresh(new_submission)

    # Send confirmation email (runs inline due to task_always_eager=True)
    send_submission_confirmation.delay(
        student_email=f"student_{new_submission.student_id}@uni.edu",
        assignment_title=f"Assignment #{new_submission.assignment_id}",
    )

    return "Submission created"


def submissionList(db: Session):
    return db.query(Submission).all()


def submissionGet(submission_id: int, db: Session):
    return db.query(Submission).get(submission_id)


def submissionsByAssignment(assignment_id: int, db: Session):
    return db.query(Submission).filter(Submission.assignment_id == assignment_id).all()


def submissionGrade(submission_id: int, grade: SubmissionGrade, db: Session):
    submission = db.query(Submission).get(submission_id)
    submission.score = grade.score
    submission.feedback = grade.feedback
    submission.status = "graded"
    db.add(submission)
    db.commit()

    # Send grade notification email (runs inline due to task_always_eager=True)
    send_grade_notification.delay(
        student_email=f"student_{submission.student_id}@uni.edu",
        assignment_title=f"Assignment #{submission.assignment_id}",
        score=grade.score,
        feedback=grade.feedback,
    )

    return "Submission graded"


def submissionDelete(submission_id: int, db: Session):
    submission = db.query(Submission).get(submission_id)
    db.delete(submission)
    db.commit()
    return "Submission deleted"
