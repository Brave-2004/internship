from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field



class DepartmentCreate(BaseModel):
    name: str
    building: str

class DepartmentResponse(BaseModel):
    id: int
    name: str
    building: str

    class Config:
        from_attributes = True



class TeacherCreate(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str
    salary: float
    department_id: int = Field(alias="departmentId")

    class Config:
        populate_by_name = True

class TeacherResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    salary: float
    department: DepartmentResponse

    class Config:
        from_attributes = True



class StudentCreate(BaseModel):
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: str
    age: int
    department_id: int = Field(alias="departmentId")

    class Config:
        populate_by_name = True

class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    email: str

    class Config:
        from_attributes = True



class CourseCreate(BaseModel):
    name: str
    credits: int
    teacher_id: int = Field(alias="teacherId")
    department_id: int = Field(alias="departmentId")

    class Config:
        populate_by_name = True

class CourseResponse(BaseModel):
    id: int
    name: str
    credits: int

    class Config:
        from_attributes = True


class EnrollmentCreate(BaseModel):
    student_id: int = Field(alias="studentId")
    course_id: int = Field(alias="courseId")
    semester: int
    grade: float

    class Config:
        populate_by_name = True

class EnrollmentResponse(BaseModel):
    id: int
    student: StudentResponse
    course: CourseResponse
    semester: int
    grade: float

    class Config:
        from_attributes = True


class LessonCreate(BaseModel):
    course_id: int = Field(alias="courseId")
    title: str
    description: str
    order: int

    class Config:
        populate_by_name = True

class LessonResponse(BaseModel):
    id: int
    course_id: int
    title: str
    description: str
    order: int

    class Config:
        from_attributes = True



class AssignmentCreate(BaseModel):
    lesson_id: int = Field(alias="lessonId")
    course_id: int = Field(alias="courseId")
    teacher_id: int = Field(alias="teacherId")
    title: str
    description: str
    deadline: datetime
    max_score: int = Field(alias="maxScore")

    class Config:
        populate_by_name = True

class AssignmentResponse(BaseModel):
    id: int
    lesson_id: int
    course_id: int
    teacher_id: int
    title: str
    description: str
    deadline: datetime
    max_score: int
    created_at: datetime

    class Config:
        from_attributes = True



class SubmissionCreate(BaseModel):
    assignment_id: int = Field(alias="assignmentId")
    student_id: int = Field(alias="studentId")
    file_path: str = Field(alias="filePath")

    class Config:
        populate_by_name = True

class SubmissionGrade(BaseModel):
    score: float
    feedback: str

class SubmissionResponse(BaseModel):
    id: int
    assignment_id: int
    student_id: int
    file_path: str
    submitted_at: datetime
    status: str
    score: Optional[float] = None
    feedback: Optional[str] = None

    class Config:
        from_attributes = True



class UserRegister(BaseModel):
    email: str
    password: str
    role: str  # admin, teacher, student

class UserLogin(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"



class NotificationCreate(BaseModel):
    user_id: int = Field(alias="userId")
    message: str

    class Config:
        populate_by_name = True

class NotificationResponse(BaseModel):
    id: str
    user_id: int
    message: str
    is_read: bool
    created_at: datetime



class CommentCreate(BaseModel):
    lesson_id: int = Field(alias="lessonId")
    user_id: int = Field(alias="userId")
    content: str

    class Config:
        populate_by_name = True

class CommentResponse(BaseModel):
    id: str
    lesson_id: int
    user_id: int
    content: str
    created_at: datetime