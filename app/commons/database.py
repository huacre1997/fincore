from datetime import datetime
from typing import Any, Sequence
from typing import TypeVar

# Define un tipo genérico usando TypeVar
from pydantic import BaseModel
from sqlalchemy import create_engine, func
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    declared_attr,
    mapped_column,
    sessionmaker,
)

from config import settings

engine = create_engine(settings.BD_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

T = TypeVar("T")


class Base(DeclarativeBase):
    @declared_attr.directive
    @classmethod
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)


class TimestampMixin:
    created_at: Mapped[datetime] = mapped_column(insert_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(insert_default=func.now())


class AuditableMixin:
    created_by: Mapped[str]
    updated_by: Mapped[str]


def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    finally:
        session.close()


def end_create(db: Session, db_model: T) -> T:
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model


def end_update(
    db: Session, db_model: T, values: Sequence[tuple[str, Any]] | BaseModel
) -> T:
    for key, value in values:
        if hasattr(db_model, key):
            setattr(db_model, key, value)
    db.commit()
    db.refresh(db_model)
    return db_model
