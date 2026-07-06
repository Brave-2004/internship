from fastapi import FastAPI

from database import engine, Base
from routers import (
    student_router,
    department_router,
    teacher_router,
    course_router,
    enrollment_router,
    lesson_router,
    assignment_router,
    submission_router,
    notification_router,
    comment_router,
    auth_router,
)

app = FastAPI(title="University Management API")

Base.metadata.create_all(bind=engine)

# ─── Auth ─────────────────────────────────────────────────────────
app.include_router(auth_router.router)

# ─── Core Academic (PostgreSQL) ───────────────────────────────────
app.include_router(student_router.router)
app.include_router(department_router.router)
app.include_router(teacher_router.router)
app.include_router(course_router.router)
app.include_router(enrollment_router.router)

# ─── Content (PostgreSQL) ─────────────────────────────────────────
app.include_router(lesson_router.router)
app.include_router(assignment_router.router)
app.include_router(submission_router.router)

# ─── NoSQL (MongoDB) ──────────────────────────────────────────────
app.include_router(notification_router.router)
app.include_router(comment_router.router)
