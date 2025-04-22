from fastapi import FastAPI
from sqlmodel import SQLModel, Session
from sqlalchemy import create_engine
from contextlib import asynccontextmanager

sqlite_file_name = "school.db"
sqlite_url = f"sqlite:///db/{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield
