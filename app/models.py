from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    title: Mapped[str] = mapped_column(String)

    completed: Mapped[bool] = mapped_column(Boolean, default=False)

    description: Mapped[str] = mapped_column(String, default="")

    user_id = Column(String, nullable=False)