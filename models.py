from typing import Optional, List
from pydantic import ConfigDict
from sqlmodel import SQLModel, Field, Relationship

class CourseSubjectLink(SQLModel, table=True):
    course_id: Optional[int] = Field(default=None, foreign_key="course.id", primary_key=True)
    subject_id: Optional[int] = Field(default=None, foreign_key="subject.id", primary_key=True)


class SubjectTeacherLink(SQLModel, table=True):
    subject_id: Optional[int] = Field(default=None, foreign_key="subject.id", primary_key=True)
    teacher_id: Optional[int] = Field(default=None, foreign_key="teacher.id", primary_key=True)


class CourseBase(SQLModel):
    name: str


class Course(CourseBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    students: List["Student"] = Relationship(back_populates="course")
    subjects: List["Subject"] = Relationship(back_populates="courses", link_model=CourseSubjectLink)


class SubjectBase(SQLModel):
    name: str


class Subject(SubjectBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    teachers: List["Teacher"] = Relationship(back_populates="subjects", link_model=SubjectTeacherLink)
    courses: List["Course"] = Relationship(back_populates="subjects", link_model=CourseSubjectLink)


class TeacherBase(SQLModel):
    name: str
    surname: str
    age: int


class Teacher(TeacherBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    subjects: List["Subject"] = Relationship(back_populates="teachers", link_model=SubjectTeacherLink)


class StudentBase(SQLModel):
    name: str
    surname: str
    age: int
    course_id: Optional[int] = Field(default=None, foreign_key="course.id")


class Student(StudentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    course: Optional["Course"] = Relationship(back_populates="students")



class CourseCreate(CourseBase):
    pass


class SubjectCreate(SubjectBase):
    pass


class TeacherCreate(TeacherBase):
    pass


class StudentCreate(StudentBase):
    pass


class SubjectRead(SubjectBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class StudentRead(StudentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class CourseRead(CourseBase):
    id: int
    students: List[StudentRead] = None
    subjects: List[SubjectRead] = None

    model_config = ConfigDict(from_attributes=True)


class TeacherRead(TeacherBase):
    id: int
    subjects: List[SubjectRead] = None

    model_config = ConfigDict(from_attributes=True)


