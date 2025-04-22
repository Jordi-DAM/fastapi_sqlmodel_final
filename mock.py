from sqlmodel import Session
from models import *
from database import engine, create_db_and_tables


def create_samples():
    with Session(engine) as session:
        course_dam = Course(name="Desarrollo de Aplicaciones Multiplataforma")
        course_asir = Course(name="Administración de Sistemas Informáticos en Red")

        session.add(course_dam)
        session.add(course_asir)
        session.commit()

        teacher_pep = Teacher(name="Pep", surname="Bea", age=30)
        teacher_alberto = Teacher(name="Alberto", surname="Montero", age=30)
        teacher_gines = Teacher(name="Gines", surname="Plazas", age=30)

        session.add(teacher_pep)
        session.add(teacher_alberto)
        session.add(teacher_gines)
        session.commit()

        subject_prog = Subject(name="Programación", courses=[course_dam], teachers=[teacher_pep, teacher_alberto])
        subject_digi = Subject(name="Digitalización", courses=[course_dam], teachers=[teacher_alberto])
        subject_bd = Subject(name="Bases de Datos", courses=[course_dam, course_asir], teachers=[teacher_gines])

        session.add(subject_prog)
        session.add(subject_digi)
        session.add(subject_bd)
        session.commit()

        student_jordi = Student(name="Jordi", surname="Divison", age=25, course=course_dam)
        student_joan = Student(name="Joan", surname="Moreno", age=18, course=course_dam)
        student_sara = Student(name="Sara", surname="Díaz", age=22, course=course_asir)

        session.add(student_jordi)
        session.add(student_joan)
        session.add(student_sara)
        session.commit()


def main():
    create_db_and_tables()
    create_samples()


if __name__ == "__main__":
    main()
