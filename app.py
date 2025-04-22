from fastapi import FastAPI, Depends, Query, HTTPException
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select
from database import engine, lifespan, get_session
from models import *

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Welcome. This API was built thinking of a simulation of a school"}


# COURSE
@app.post("/courses")
def create_course(
        course_data: CourseCreate,
        session: Session = Depends(get_session)
) -> Course:
    course = Course(name=course_data.name)
    session.add(course)
    session.commit()
    session.refresh(course)
    return course


@app.get("/courses", response_model=List[CourseRead])
def read_courses(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as session:
        statement = select(Course).options(
            selectinload(Course.students),
            selectinload(Course.subjects)
        ).offset(offset).limit(limit)
        courses = session.exec(statement).all()
        return courses


@app.get("/courses/{course_id}", response_model=CourseRead)
def read_course(course_id: int):
    with Session(engine) as session:
        statement = select(Course).where(Course.id == course_id).options(
            selectinload(Course.students),
            selectinload(Course.subjects)
        )
        course = session.exec(statement).first()
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        return course


@app.patch("/courses/{course_id}", response_model=CourseRead)
def update_course(course_id: int, course: CourseBase):
    with Session(engine) as session:
        statement = select(Course).where(Course.id == course_id).options(
            selectinload(Course.students),
            selectinload(Course.subjects)
        )
        existing_course = session.exec(statement).first()
        if not existing_course:
            raise HTTPException(status_code=404, detail="Course not found")

        existing_course.name = course.name
        session.add(existing_course)
        session.commit()
        session.refresh(existing_course)
        return existing_course


@app.delete("/courses/{course_id}")
def delete_course(course_id: int):
    with Session(engine) as session:
        course = session.get(Course, course_id)
        if not course:
            raise HTTPException(status_code=404, detail="Course not found")
        session.delete(course)
        session.commit()
        return {"message": "Course deleted successfully"}


# SUBJECT
@app.post("/subjects")
def create_subject(
        subject_data: SubjectCreate,
        session: Session = Depends(get_session)
) -> Subject:
    subject = Subject(name=subject_data.name)
    session.add(subject)
    session.commit()
    session.refresh(subject)
    return subject


@app.get("/subjects", response_model=List[SubjectRead])
def read_subjects(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as session:
        statement = select(Subject).options(
            selectinload(Subject.teachers),
            selectinload(Subject.courses)
        ).offset(offset).limit(limit)
        subjects = session.exec(statement).all()
        return subjects


@app.get("/subjects/{subject_id}", response_model=SubjectRead)
def read_subject(subject_id: int):
    with Session(engine) as session:
        statement = select(Subject).where(Subject.id == subject_id).options(
            selectinload(Subject.teachers),
            selectinload(Subject.courses)
        )
        subject = session.exec(statement).first()
        if not subject:
            raise HTTPException(status_code=404, detail="Subject not found")
        return subject


@app.patch("/subjects/{subject_id}", response_model=SubjectRead)
def update_subject(subject_id: int, subject: SubjectBase):
    with Session(engine) as session:
        existing_subject = session.get(Subject, subject_id)
        if not existing_subject:
            raise HTTPException(status_code=404, detail="Subject not found")
        existing_subject.name = subject.name
        session.add(existing_subject)
        session.commit()
        session.refresh(existing_subject)
        return existing_subject


@app.delete("/subjects/{subject_id}")
def delete_subject(subject_id: int):
    with Session(engine) as session:
        subject = session.get(Subject, subject_id)
        if not subject:
            raise HTTPException(status_code=404, detail="Subject not found")
        session.delete(subject)
        session.commit()
        return {"message": "Subject deleted successfully"}


# TEACHER
@app.post("/teachers")
def create_teacher(
        teacher_data: TeacherCreate,
        session: Session = Depends(get_session)
) -> Teacher:
    teacher = Teacher(name=teacher_data.name, surname=teacher_data.surname, age=teacher_data.age)
    session.add(teacher)
    session.commit()
    session.refresh(teacher)
    return teacher


@app.get("/teachers", response_model=List[TeacherRead])
def read_teachers(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as session:
        statement = select(Teacher).options(selectinload(Teacher.subjects)).offset(offset).limit(limit)
        teachers = session.exec(statement).all()
        return teachers


@app.get("/teachers/{teacher_id}", response_model=TeacherRead)
def read_teacher(teacher_id: int):
    with Session(engine) as session:
        teacher = session.exec(select(Teacher).where(Teacher.id == teacher_id)).first()
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        return teacher


@app.patch("/teachers/{teacher_id}", response_model=TeacherRead)
def update_teacher(teacher_id: int, teacher: TeacherBase):
    with Session(engine) as session:
        existing_teacher = session.get(Teacher, teacher_id)
        if not existing_teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        existing_teacher.name = teacher.name
        existing_teacher.surname = teacher.surname
        existing_teacher.age = teacher.age
        session.add(existing_teacher)
        session.commit()
        session.refresh(existing_teacher)
        return existing_teacher


@app.delete("/teachers/{teacher_id}")
def delete_teacher(teacher_id: int):
    with Session(engine) as session:
        teacher = session.get(Teacher, teacher_id)
        if not teacher:
            raise HTTPException(status_code=404, detail="Teacher not found")
        session.delete(teacher)
        session.commit()
        return {"message": "Teacher deleted successfully"}


# STUDENT
@app.post("/students")
def create_student(
        student_data: StudentCreate,
        session: Session = Depends(get_session)
) -> Student:
    student = Student(name=student_data.name, surname=student_data.surname, age=student_data.age,
                      course_id=student_data.course_id)
    session.add(student)
    session.commit()
    session.refresh(student)
    return student


@app.get("/students", response_model=List[StudentRead])
def read_students(offset: int = 0, limit: int = Query(default=100, le=100)):
    with Session(engine) as session:
        statement = select(Student).offset(offset).limit(limit)
        students = session.exec(statement).all()
        return students


@app.get("/students/{student_id}", response_model=StudentRead)
def read_student(student_id: int):
    with Session(engine) as session:
        student = session.exec(select(Student).where(Student.id == student_id)).first()
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        return student


@app.patch("/students/{student_id}", response_model=StudentRead)
def update_student(student_id: int, student: StudentBase):
    with Session(engine) as session:
        existing_student = session.get(Student, student_id)
        if not existing_student:
            raise HTTPException(status_code=404, detail="Student not found")
        existing_student.name = student.name
        existing_student.surname = student.surname
        existing_student.age = student.age
        if student.course_id:
            existing_student.course_id = student.course_id
        session.add(existing_student)
        session.commit()
        session.refresh(existing_student)
        return existing_student


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    with Session(engine) as session:
        student = session.get(Student, student_id)
        if not student:
            raise HTTPException(status_code=404, detail="Student not found")
        session.delete(student)
        session.commit()
        return {"message": "Student deleted successfully"}


@app.get("/courses/{course_id}/students", response_model=List[StudentRead])
def get_students_in_course(course_id: int, session: Session = Depends(get_session)):
    course = session.get(Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course.students

@app.get("/subjects/{subject_id}/teachers", response_model=List[TeacherRead])
def get_teachers_in_subject(subject_id: int, session: Session = Depends(get_session)):
    subject = session.get(Subject, subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return subject.teachers


@app.get("/subjects/{subject_id}/courses", response_model=List[CourseRead])
def get_courses_for_subject(subject_id: int, session: Session = Depends(get_session)):
    subject = session.get(Subject, subject_id)
    if not subject:
        raise HTTPException(status_code=404, detail="Subject not found")
    return subject.courses


@app.get("/courses/{course_id}/student_count")
def get_student_count_in_course(course_id: int, session: Session = Depends(get_session)):
    course = session.get(Course, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    student_count = len(course.students)
    return {"course_id": course_id, "student_count": student_count}


@app.get("/teachers/{teacher_id}/courses", response_model=List[CourseRead])
def get_courses_for_teacher(teacher_id: int, session: Session = Depends(get_session)):
    teacher = session.get(Teacher, teacher_id)
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    courses = []
    for subject in teacher.subjects:
        courses.extend(subject.courses)
    return courses
