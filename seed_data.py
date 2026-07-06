import requests
import datetime

BASE_URL = "http://127.0.0.1:8000"

def post(path, payload, token=None):
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    res = requests.post(f"{BASE_URL}{path}", json=payload, headers=headers)
    if res.status_code != 200:
        print(f"  ❌ POST {path} → {res.status_code}: {res.text}")
    return res

def get(path, params=None, token=None):
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    return requests.get(f"{BASE_URL}{path}", params=params, headers=headers)

def put(path, payload, token=None):
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    res = requests.put(f"{BASE_URL}{path}", json=payload, headers=headers)
    if res.status_code != 200:
        print(f"  ❌ PUT {path} → {res.status_code}: {res.text}")
    return res


def seed():
    print("=" * 55)
    print("  Seeding database with realistic data...")
    print("=" * 55)

    # ─────────────────────────────────────────────
    # 0. AUTH
    # ─────────────────────────────────────────────
    print("\n[0/8] Creating Admin User & Getting Token...")
    post("/auth/register", {"email": "admin@uni.edu", "password": "securepassword", "role": "admin"})
    admin_login = requests.post(f"{BASE_URL}/auth/login", json={"email": "admin@uni.edu", "password": "securepassword"})
    admin_token = admin_login.json().get("access_token")

    # ─────────────────────────────────────────────
    # 1. DEPARTMENTS
    # ─────────────────────────────────────────────
    print("\n[1/8] Creating departments...")
    departments_data = [
        {"name": "Computer Science",       "building": "Engineering Block A"},
        {"name": "Mathematics",            "building": "Science Tower B"},
        {"name": "Physics",                "building": "Science Tower C"},
        {"name": "Electrical Engineering", "building": "Engineering Block B"},
        {"name": "Business Administration","building": "Commerce Hall"},
    ]
    for d in departments_data:
        post("/department/createDepartment", d, admin_token)

    depts = get("/department/allDepartments", token=admin_token).json()
    dept_ids = {d["name"]: d["id"] for d in depts}
    print(f"   ✅ {len(depts)} departments ready: {list(dept_ids.keys())}")

    cs_id   = dept_ids.get("Computer Science", 1)
    math_id = dept_ids.get("Mathematics", 2)
    phy_id  = dept_ids.get("Physics", 3)
    ee_id   = dept_ids.get("Electrical Engineering", 4)
    ba_id   = dept_ids.get("Business Administration", 5)

    # ─────────────────────────────────────────────
    # 2. TEACHERS
    # ─────────────────────────────────────────────
    print("\n[2/8] Creating teachers...")
    teachers_data = [
        # Computer Science
        {"firstName": "Alan", "lastName": "Turing",      "email": "alan.turing@uni.edu",      "salary": 95000, "departmentId": cs_id},
        {"firstName": "Ada", "lastName": "Lovelace",   "email": "ada.lovelace@uni.edu",     "salary": 92000, "departmentId": cs_id},
        {"firstName": "Donald", "lastName": "Knuth",     "email": "donald.knuth@uni.edu",     "salary": 98000, "departmentId": cs_id},
        # Mathematics
        {"firstName": "Euler", "lastName": "Leonard",  "email": "euler.leonard@uni.edu",    "salary": 88000, "departmentId": math_id},
        {"firstName": "Sophie", "lastName": "Germain",   "email": "sophie.germain@uni.edu",   "salary": 85000, "departmentId": math_id},
        # Physics
        {"firstName": "Richard", "lastName": "Feynman",  "email": "r.feynman@uni.edu",        "salary": 97000, "departmentId": phy_id},
        {"firstName": "Marie", "lastName": "Curie",    "email": "marie.curie@uni.edu",      "salary": 94000, "departmentId": phy_id},
        # Electrical Engineering
        {"firstName": "Nikola", "lastName": "Tesla",     "email": "n.tesla@uni.edu",          "salary": 91000, "departmentId": ee_id},
        {"firstName": "Claude", "lastName": "Shannon", "email": "c.shannon@uni.edu",        "salary": 89000, "departmentId": ee_id},
        # Business Administration
        {"firstName": "Peter", "lastName": "Drucker",  "email": "p.drucker@uni.edu",        "salary": 86000, "departmentId": ba_id},
    ]
    for t in teachers_data:
        post("/teacher/create", t, admin_token)

    teachers = get("/teacher/list", token=admin_token).json()
    print(f"   ✅ {len(teachers)} teachers created")
    # Map last_name -> id
    teacher_ids = {t["last_name"]: t["id"] for t in teachers}

    # ─────────────────────────────────────────────
    # 3. STUDENTS
    # ─────────────────────────────────────────────
    print("\n[3/8] Creating students...")
    students_data = [
        # CS students
        {"firstName": "Alice", "lastName": "Johnson",    "email": "alice.j@student.uni.edu",    "age": 20, "departmentId": cs_id},
        {"firstName": "Bob", "lastName": "Williams",     "email": "bob.w@student.uni.edu",      "age": 21, "departmentId": cs_id},
        {"firstName": "Carol", "lastName": "Martinez",   "email": "carol.m@student.uni.edu",    "age": 19, "departmentId": cs_id},
        {"firstName": "David", "lastName": "Chen",       "email": "david.c@student.uni.edu",    "age": 22, "departmentId": cs_id},
        {"firstName": "Emma", "lastName": "Davis",       "email": "emma.d@student.uni.edu",     "age": 20, "departmentId": cs_id},
        # Math students
        {"firstName": "Frank", "lastName": "Miller",     "email": "frank.m@student.uni.edu",    "age": 21, "departmentId": math_id},
        {"firstName": "Grace", "lastName": "Wilson",     "email": "grace.w@student.uni.edu",    "age": 20, "departmentId": math_id},
        {"firstName": "Henry", "lastName": "Moore",      "email": "henry.mo@student.uni.edu",   "age": 22, "departmentId": math_id},
        # Physics students
        {"firstName": "Isla", "lastName": "Taylor",      "email": "isla.t@student.uni.edu",     "age": 19, "departmentId": phy_id},
        {"firstName": "Jack", "lastName": "Anderson",    "email": "jack.a@student.uni.edu",     "age": 21, "departmentId": phy_id},
        {"firstName": "Karen", "lastName": "Thomas",     "email": "karen.t@student.uni.edu",    "age": 20, "departmentId": phy_id},
        # EE students
        {"firstName": "Liam", "lastName": "Jackson",     "email": "liam.j@student.uni.edu",     "age": 22, "departmentId": ee_id},
        {"firstName": "Mia", "lastName": "White",        "email": "mia.w@student.uni.edu",      "age": 21, "departmentId": ee_id},
        {"firstName": "Noah", "lastName": "Harris",      "email": "noah.h@student.uni.edu",     "age": 20, "departmentId": ee_id},
        # BA students
        {"firstName": "Olivia", "lastName": "Clark",     "email": "olivia.c@student.uni.edu",   "age": 23, "departmentId": ba_id},
        {"firstName": "Peter", "lastName": "Lewis",      "email": "peter.l@student.uni.edu",    "age": 21, "departmentId": ba_id},
        {"firstName": "Quinn", "lastName": "Robinson",   "email": "quinn.r@student.uni.edu",    "age": 20, "departmentId": ba_id},
        {"firstName": "Rachel", "lastName": "Walker",    "email": "rachel.w@student.uni.edu",   "age": 22, "departmentId": ba_id},
        {"firstName": "Sam", "lastName": "Hall",         "email": "sam.h@student.uni.edu",      "age": 19, "departmentId": cs_id},
        {"firstName": "Tina", "lastName": "Young",       "email": "tina.y@student.uni.edu",     "age": 21, "departmentId": math_id},
    ]
    for s in students_data:
        post("/api/student/create", s, admin_token)

    # Register Alice as a User so she can log in
    post("/auth/register", {"email": "alice.j@student.uni.edu", "password": "alicepassword", "role": "student"})
    alice_login = requests.post(f"{BASE_URL}/auth/login", json={"email": "alice.j@student.uni.edu", "password": "alicepassword"})
    alice_token = alice_login.json().get("access_token")

    students = get("/api/student/students", token=admin_token).json()
    print(f"   ✅ {len(students)} students created")
    student_ids = {s["last_name"]: s["id"] for s in students}

    # ─────────────────────────────────────────────
    # 4. COURSES
    # ─────────────────────────────────────────────
    print("\n[4/8] Creating courses...")

    def tid(name): return teacher_ids.get(name, 1)

    courses_data = [
        # CS courses
        {"name": "Algorithms & Data Structures", "credits": 4, "teacherId": tid("Turing"),     "departmentId": cs_id},
        {"name": "Operating Systems",            "credits": 3, "teacherId": tid("Lovelace"),  "departmentId": cs_id},
        {"name": "Database Systems",             "credits": 3, "teacherId": tid("Knuth"),    "departmentId": cs_id},
        {"name": "Machine Learning",             "credits": 4, "teacherId": tid("Turing"),     "departmentId": cs_id},
        # Math courses
        {"name": "Linear Algebra",               "credits": 3, "teacherId": tid("Leonard"), "departmentId": math_id},
        {"name": "Calculus II",                  "credits": 4, "teacherId": tid("Germain"),  "departmentId": math_id},
        {"name": "Discrete Mathematics",         "credits": 3, "teacherId": tid("Leonard"), "departmentId": math_id},
        # Physics courses
        {"name": "Quantum Mechanics",            "credits": 4, "teacherId": tid("Feynman"), "departmentId": phy_id},
        {"name": "Thermodynamics",               "credits": 3, "teacherId": tid("Curie"),   "departmentId": phy_id},
        # EE courses
        {"name": "Circuit Theory",               "credits": 3, "teacherId": tid("Tesla"),    "departmentId": ee_id},
        {"name": "Digital Signal Processing",    "credits": 4, "teacherId": tid("Shannon"),"departmentId": ee_id},
        # BA courses
        {"name": "Principles of Management",     "credits": 3, "teacherId": tid("Drucker"), "departmentId": ba_id},
        {"name": "Financial Accounting",         "credits": 3, "teacherId": tid("Drucker"), "departmentId": ba_id},
    ]
    for c in courses_data:
        post("/course/create", c, admin_token)

    courses = get("/course/courses", token=admin_token).json()
    print(f"   ✅ {len(courses)} courses created")
    course_ids = {c["name"]: c["id"] for c in courses}

    # ─────────────────────────────────────────────
    # 5. ENROLLMENTS
    # ─────────────────────────────────────────────
    print("\n[5/8] Creating enrollments...")

    def sid(name): return student_ids.get(name, 1)
    def cid(name): return course_ids.get(name, 1)

    enrollments_data = [
        # Alice → CS courses
        {"studentId": sid("Johnson"),  "courseId": cid("Algorithms & Data Structures"), "semester": 1, "grade": 88},
        {"studentId": sid("Johnson"),  "courseId": cid("Operating Systems"),            "semester": 1, "grade": 91},
        {"studentId": sid("Johnson"),  "courseId": cid("Linear Algebra"),               "semester": 1, "grade": 85},
        # Bob
        {"studentId": sid("Williams"),   "courseId": cid("Algorithms & Data Structures"), "semester": 2, "grade": 76},
        {"studentId": sid("Williams"),   "courseId": cid("Database Systems"),             "semester": 2, "grade": 83},
        {"studentId": sid("Williams"),   "courseId": cid("Machine Learning"),             "semester": 2, "grade": 79},
        # Carol
        {"studentId": sid("Martinez"), "courseId": cid("Operating Systems"),            "semester": 1, "grade": 93},
        {"studentId": sid("Martinez"), "courseId": cid("Discrete Mathematics"),         "semester": 1, "grade": 87},
    ]

    ok = 0
    for e in enrollments_data:
        res = post("/enrollment/create", e, admin_token)
        if res.status_code == 200:
            ok += 1

    print(f"   ✅ {ok}/{len(enrollments_data)} enrollments created")

    # ─────────────────────────────────────────────
    # 6. LESSONS & ASSIGNMENTS
    # ─────────────────────────────────────────────
    print("\n[6/8] Creating lessons & assignments...")
    cs_course_id = cid("Algorithms & Data Structures")
    teacher_id = tid("Turing")

    lessons = [
        {"courseId": cs_course_id, "title": "Intro to Sorting", "description": "Basics of Sorting", "order": 1},
        {"courseId": cs_course_id, "title": "Advanced Graphs", "description": "Graph algorithms", "order": 2},
    ]
    for l in lessons:
        post("/lesson/create", l, admin_token)

    lessons_resp = get("/lesson/list", token=admin_token).json()
    print(f"   ✅ {len(lessons_resp)} lessons created")
    
    if len(lessons_resp) > 0:
        lesson_id = lessons_resp[0]["id"]
        deadline = (datetime.datetime.now(datetime.UTC) + datetime.timedelta(days=7)).isoformat()
        asn_data = {"lessonId": lesson_id, "courseId": cs_course_id, "teacherId": teacher_id, "title": "Sorting HW", "description": "Sort an array", "deadline": deadline, "maxScore": 100}
        post("/assignment/create", asn_data, admin_token)

        asn_resp = get("/assignment/list", token=admin_token).json()
        print(f"   ✅ {len(asn_resp)} assignments created")

    # ─────────────────────────────────────────────
    # 7. SUBMISSIONS
    # ─────────────────────────────────────────────
    print("\n[7/8] Creating submissions...")
    asn_resp = get("/assignment/list", token=admin_token).json()
    if len(asn_resp) > 0:
        asn_id = asn_resp[0]["id"]
        sub_data = {"assignmentId": asn_id, "studentId": sid("Johnson"), "filePath": "/uploads/hw1_alice.pdf"}
        # Alice uses her token to submit!
        post("/submission/create", sub_data, alice_token)
        
        subs = get("/submission/list", token=admin_token).json()
        print(f"   ✅ {len(subs)} submissions created")
        
        if len(subs) > 0:
            sub_id = subs[0]["id"]
            # Admin/Teacher uses their token to grade!
            res = put(f"/submission/grade/{sub_id}", {"score": 95, "feedback": "Excellent"}, admin_token)
            if res.status_code == 200:
                print(f"   ✅ Graded submission {sub_id}")

    # ─────────────────────────────────────────────
    # 8. MONGODB (NOTIFICATIONS & COMMENTS)
    # ─────────────────────────────────────────────
    print("\n[8/8] Creating Notifications & Comments...")
    post("/notification/create", {"userId": 1, "message": "Welcome to the new system!"}, admin_token)
    post("/comment/create", {"lessonId": 1, "userId": 1, "content": "This lesson is great."}, admin_token)
    
    print("\n" + "=" * 55)
    print("  ✅  Seed complete! Summary:")
    print(f"      Departments : {len(depts)}")
    print(f"      Teachers    : {len(teachers)}")
    print(f"      Students    : {len(students)}")
    print(f"      Courses     : {len(courses)}")
    print(f"      Enrollments : {ok}")
    print("=" * 55)


if __name__ == "__main__":
    seed()
