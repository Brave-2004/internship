from celery_app import celery


@celery.task
def send_submission_confirmation(student_email: str, assignment_title: str):
    """Notify student that their submission was received."""
    print(f"[EMAIL] To: {student_email}")
    print(f"[EMAIL] Subject: Submission Received — {assignment_title}")
    print(f"[EMAIL] Body: Your submission for '{assignment_title}' has been received successfully.")


@celery.task
def send_deadline_reminder(student_email: str, assignment_title: str, deadline: str):
    """Remind student about an upcoming assignment deadline."""
    print(f"[EMAIL] To: {student_email}")
    print(f"[EMAIL] Subject: Reminder — '{assignment_title}' due {deadline}")
    print(f"[EMAIL] Body: Don't forget! '{assignment_title}' is due on {deadline}.")


@celery.task
def send_grade_notification(student_email: str, assignment_title: str, score: float, feedback: str):
    """Notify student that their submission has been graded."""
    print(f"[EMAIL] To: {student_email}")
    print(f"[EMAIL] Subject: Grade Posted — {assignment_title}")
    print(f"[EMAIL] Body: Score: {score} | Feedback: {feedback}")
