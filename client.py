import requests

courses_url = "http://127.0.0.1:8000/courses"
subjects_url = "http://127.0.0.1:8000/subjects"
teachers_url = "http://127.0.0.1:8000/teachers"
students_url = "http://127.0.0.1:8000/students"


def read_courses():
    data = requests.get(courses_url)
    print(data.status_code)
    if data.status_code == 200:
        for course in data.json():
            print(course)
    else:
        print(f"Error: {data.text}")


def read_course(course_id: int):
    data = requests.get(f"{courses_url}/{course_id}")
    print(data.status_code)
    if data.status_code == 200:
        print(data.json())
    else:
        print(f"Error: {data.text}")


def create_course(name: str):
    course = {'name': name}
    data = requests.post(f"{courses_url}/", json=course)
    print(data.status_code)
    if data.status_code in [200, 201]:
        print(data.json())
    else:
        print(f"Error: {data.text}")


def delete_course(course_id: int):
    data = requests.delete(f"{courses_url}/{course_id}")
    print(data.status_code)
    if data.status_code == 200:
        print(data.json())
    else:
        print(f"Error: {data.text}")


def update_course(course_id: int, new_name: str):
    data = requests.patch(f"{courses_url}/{course_id}", json={'name': new_name})
    print(data.status_code)
    if data.status_code == 200:
        print(data.json())
    else:
        print(f"Error: {data.text}")


def read_subjects():
    data = requests.get(subjects_url)
    print(data.status_code)
    if data.status_code == 200:
        for subject in data.json():
            print(subject)
    else:
        print(f"Error: {data.text}")


def create_subject(name: str):
    subject = {'name': name}
    data = requests.post(subjects_url, json=subject)
    print(data.status_code)
    if data.status_code in [200, 201]:
        print(data.json())
    else:
        print(f"Error: {data.text}")


def delete_subject(subject_id: int):
    data = requests.delete(f"{subjects_url}/{subject_id}")
    print(data.status_code)
    if data.status_code == 200:
        print(data.json())
    else:
        print(f"Error: {data.text}")


def update_subject(subject_id: int, new_name: str):
    data = requests.patch(f"{subjects_url}/{subject_id}", json={'name': new_name})
    print(data.status_code)
    if data.status_code == 200:
        print(data.json())
    else:
        print(f"Error: {data.text}")


def read_teachers():
    data = requests.get(teachers_url)
    print(data.status_code)
    if data.status_code == 200:
        for teacher in data.json():
            print(teacher)
    else:
        print(f"Error: {data.text}")


def create_teacher(name: str, surname: str, age: int):
    teacher = {'name': name, 'surname': surname, 'age': age}
    data = requests.post(teachers_url, json=teacher)
    print(data.status_code)
    if data.status_code in [200, 201]:
        print(data.json())
    else:
        print(f"Error: {data.text}")


def delete_teacher(teacher_id: int):
    data = requests.delete(f"{teachers_url}/{teacher_id}")
    print(data.status_code)
    if data.status_code == 200:
        print(data.json())
    else:
        print(f"Error: {data.text}")


def update_teacher(teacher_id: int, new_data: dict):
    data = requests.patch(f"{teachers_url}/{teacher_id}", json=new_data)
    print(data.status_code)
    if data.status_code == 200:
        print(data.json())
    else:
        print(f"Error: {data.text}")


def read_students():
    data = requests.get(students_url)
    print(data.status_code)
    if data.status_code == 200:
        for student in data.json():
            print(student)
    else:
        print(f"Error: {data.text}")


def create_student(name: str, surname: str, age: int, course_id: int):
    student = {'name': name, 'surname': surname, 'age': age, 'course_id': course_id}
    data = requests.post(students_url, json=student)
    print(data.status_code)
    if data.status_code in [200, 201]:
        print(data.json())
    else:
        print(f"Error: {data.text}")


def delete_student(student_id: int):
    data = requests.delete(f"{students_url}/{student_id}")
    print(data.status_code)
    if data.status_code == 200:
        print(data.json())
    else:
        print(f"Error: {data.text}")


def update_student(student_id: int, new_data: dict):
    data = requests.patch(f"{students_url}/{student_id}", json=new_data)
    print(data.status_code)
    if data.status_code == 200:
        print(data.json())
    else:
        print(f"Error: {data.text}")

def get_students_in_course(course_id: int):
    data = requests.get(f"{courses_url}/{course_id}/students")
    print(data.status_code)
    if data.status_code == 200:
        for student in data.json():
            print(student)
    else:
        print(f"Error: {data.text}")


def get_teachers_in_subject(subject_id: int):
    data = requests.get(f"{subjects_url}/{subject_id}/teachers")
    print(data.status_code)
    if data.status_code == 200:
        for teacher in data.json():
            print(teacher)
    else:
        print(f"Error: {data.text}")


def get_courses_for_subject(subject_id: int):
    data = requests.get(f"{subjects_url}/{subject_id}/courses")
    print(data.status_code)
    if data.status_code == 200:
        for course in data.json():
            print(course)
    else:
        print(f"Error: {data.text}")


def get_student_count_in_course(course_id: int):
    data = requests.get(f"{courses_url}/{course_id}/student_count")
    print(data.status_code)
    if data.status_code == 200:
        print(data.json())
    else:
        print(f"Error: {data.text}")


def get_courses_for_teacher(teacher_id: int):
    data = requests.get(f"{teachers_url}/{teacher_id}/courses")
    print(data.status_code)
    if data.status_code == 200:
        for course in data.json():
            print(course)
    else:
        print(f"Error: {data.text}")

if __name__ == "__main__":
    print("\nCourses Operations")
    read_courses()
    create_course("New Course")
    read_course(3)
    update_course(3, "Updated Course Name")
    delete_course(3)

    print("\nSubjects Operations")
    read_subjects()
    create_subject("New Subject")
    update_subject(4, "Updated Subject Name")
    delete_subject(4)

    print("\nTeachers Operations")
    read_teachers()
    create_teacher("Juan", "Matesanz", 30)
    update_teacher(4, {"surname": "Perez"})
    delete_teacher(4)

    print("\nStudents Operations")
    read_students()
    create_student("Hector", "Rodriguez", 22, 1)
    update_student(4, {"name":"Hector", "surname":"Rodriguez","age": 18,"course_id":1})
    delete_student(4)

    print("\nAdditional Endpoints Operations")
    get_students_in_course(2)
    get_teachers_in_subject(3)
    get_courses_for_subject(3)
    get_student_count_in_course(2)
    get_courses_for_teacher(2)