import requests

BASE_URL = "http://127.0.0.1:8000"

def test_endpoints():
    print("Testing endpoints...")

    # 1. Department
    print("\\n--- Department ---")
    dept_payload = {"name": "Computer Science", "building": "Building A"}
    res = requests.post(f"{BASE_URL}/department/createDepartment", json=dept_payload)
    print("POST /department/createDepartment:", res.status_code, res.text)
    
    # We might need the department ID for next requests, but for simplicity, let's assume it's 1 if DB was empty, or get it from list
    res = requests.get(f"{BASE_URL}/department/allDepartments")
    print("GET /department/allDepartments:", res.status_code)
    dept_id = res.json()[-1]["id"] if res.json() else 1

    res = requests.get(f"{BASE_URL}/department/departments/get/{dept_id}")
    print("GET /department/departments/get/{id}:", res.status_code)

    res = requests.put(f"{BASE_URL}/department/departments/update/{dept_id}", json={"name": "CS Updated", "building": "Building B"})
    print("PUT /department/departments/update/{id}:", res.status_code)

    # 2. Teacher
    print("\\n--- Teacher ---")
    teacher_payload = {"name": "John Doe", "email": "john@example.com", "salary": 50000, "departmentId": dept_id}
    res = requests.post(f"{BASE_URL}/teacher/create", json=teacher_payload)
    print("POST /teacher/create:", res.status_code, res.text)

    res = requests.get(f"{BASE_URL}/teacher/teacherList")
    print("GET /teacher/teacherList:", res.status_code)
    teacher_id = res.json()[-1]["id"] if res.json() else 1

    res = requests.get(f"{BASE_URL}/teacher/teacherBY_ID", params={"teacher_id": teacher_id})
    print("GET /teacher/teacherBY_ID:", res.status_code)

    # 3. Student
    print("\\n--- Student ---")
    student_payload = {"name": "Alice", "email": "alice@example.com", "age": 20, "departmentId": dept_id}
    res = requests.post(f"{BASE_URL}/api/student/create", json=student_payload)
    print("POST /api/student/create:", res.status_code, res.text)

    res = requests.get(f"{BASE_URL}/api/student/students")
    print("GET /api/student/students:", res.status_code)
    student_id = res.json()[-1]["id"] if res.json() else 1

    res = requests.get(f"{BASE_URL}/api/student/students/{student_id}")
    print("GET /api/student/students/{id}:", res.status_code)

    # 4. Course
    print("\\n--- Course ---")
    course_payload = {"name": "Math 101", "credits": 4, "teacherId": teacher_id, "departmentId": dept_id}
    res = requests.post(f"{BASE_URL}/course/create", json=course_payload)
    print("POST /course/create:", res.status_code, res.text)

    res = requests.get(f"{BASE_URL}/course/courses")
    print("GET /course/courses:", res.status_code)
    course_id = res.json()[-1]["id"] if res.json() else 1
    
    res = requests.get(f"{BASE_URL}/course/courseById", params={"course_id": course_id})
    print("GET /course/courseById:", res.status_code)

    # 5. Enrollment
    print("\\n--- Enrollment ---")
    # EnrollmentCreate has an id field, we'll try to omit it or pass a dummy one
    enrollment_payload = {"id": 1, "studentId": student_id, "teacherId": course_id, "semester": 1, "grade": 95}
    res = requests.post(f"{BASE_URL}/enrollment/create", json=enrollment_payload)
    print("POST /enrollment/create:", res.status_code, res.text)

    res = requests.get(f"{BASE_URL}/enrollment/enrollmentList")
    print("GET /enrollment/enrollmentList:", res.status_code)
    enroll_list = res.json()
    enrollment_id = enroll_list[-1]["id"] if enroll_list else 1

    res = requests.get(f"{BASE_URL}/enrollment/enrollmentGet/{enrollment_id}")
    print("GET /enrollment/enrollmentGet/{id}:", res.status_code)

    print("\\n--- Deletions ---")
    res = requests.delete(f"{BASE_URL}/enrollment/enrollmentDelete/{enrollment_id}")
    print("DELETE /enrollment/enrollmentDelete/{id}:", res.status_code)

    res = requests.delete(f"{BASE_URL}/course/courseDelete", params={"course_id": course_id})
    print("DELETE /course/courseDelete:", res.status_code)

    res = requests.delete(f"{BASE_URL}/api/student/students/{student_id}")
    print("DELETE /api/student/students/{id}:", res.status_code)

    res = requests.delete(f"{BASE_URL}/teacher/delete", params={"teacher_id": teacher_id})
    print("DELETE /teacher/delete:", res.status_code)

    res = requests.delete(f"{BASE_URL}/department/departments/{dept_id}")
    print("DELETE /department/departments/{id}:", res.status_code)

if __name__ == '__main__':
    test_endpoints()
