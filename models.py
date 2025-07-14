from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import Integer, String, DateTime
import datetime

class Base(AsyncAttrs, DeclarativeBase):
    pass

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[str] = mapped_column(String(255))
    deadline: Mapped[datetime] = mapped_column(DateTime)
    roles: Mapped[str] = mapped_column(String(255))
