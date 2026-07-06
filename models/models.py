from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, Text, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Department(Base):
    __tablename__ = "department"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    building: Mapped[str] = mapped_column(String(100))

    students = relationship("Student", back_populates="department")
    teachers = relationship("Teacher", back_populates="department")
    courses = relationship("Course", back_populates="department")


class Teacher(Base):
    __tablename__ = "teacher"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100))
    salary: Mapped[float]
    department_id: Mapped[int] = mapped_column(ForeignKey("department.id"))

    department = relationship("Department", back_populates="teachers")
    courses = relationship("Course", back_populates="teacher")
    assignments = relationship("Assignment", back_populates="teacher")


class Student(Base):
    __tablename__ = "student"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    age: Mapped[int]
    email: Mapped[str] = mapped_column(String(100))
    department_id: Mapped[int] = mapped_column(ForeignKey("department.id"))

    department = relationship("Department", back_populates="students")
    enrollments = relationship("Enrollment", back_populates="student")
    submissions = relationship("Submission", back_populates="student")


class Course(Base):
    __tablename__ = "course"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    credits: Mapped[int]
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teacher.id"))
    department_id: Mapped[int] = mapped_column(ForeignKey("department.id"))

    teacher = relationship("Teacher", back_populates="courses")
    department = relationship("Department", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")
    lessons = relationship("Lesson", back_populates="course")
    assignments = relationship("Assignment", back_populates="course")


class Enrollment(Base):
    __tablename__ = "enrollment"

    id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("student.id"))
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id"))
    semester: Mapped[int]
    grade: Mapped[float]

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")


class Lesson(Base):
    __tablename__ = "lesson"

    id: Mapped[int] = mapped_column(primary_key=True)
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id"))
    title: Mapped[str] = mapped_column(String(150))
    description: Mapped[str] = mapped_column(Text)
    order: Mapped[int]

    course = relationship("Course", back_populates="lessons")
    assignments = relationship("Assignment", back_populates="lesson")


class Assignment(Base):
    __tablename__ = "assignment"

    id: Mapped[int] = mapped_column(primary_key=True)
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lesson.id"))
    course_id: Mapped[int] = mapped_column(ForeignKey("course.id"))
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teacher.id"))
    title: Mapped[str] = mapped_column(String(150))
    description: Mapped[str] = mapped_column(Text)
    deadline: Mapped[datetime]
    max_score: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)

    lesson = relationship("Lesson", back_populates="assignments")
    course = relationship("Course", back_populates="assignments")
    teacher = relationship("Teacher", back_populates="assignments")
    submissions = relationship("Submission", back_populates="assignment")


class Submission(Base):
    __tablename__ = "submission"

    id: Mapped[int] = mapped_column(primary_key=True)
    assignment_id: Mapped[int] = mapped_column(ForeignKey("assignment.id"))
    student_id: Mapped[int] = mapped_column(ForeignKey("student.id"))
    file_path: Mapped[str] = mapped_column(String(255))
    submitted_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    score: Mapped[Optional[float]] = mapped_column(nullable=True)
    feedback: Mapped[Optional[str]] = mapped_column(Text, nullable=True)

    assignment = relationship("Assignment", back_populates="submissions")
    student = relationship("Student", back_populates="submissions")


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    hashed_password: Mapped[str]
    role: Mapped[str] = mapped_column(String(20))  # admin, teacher, student
