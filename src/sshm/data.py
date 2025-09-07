from sqlalchemy.ext.mutable import MutableList
from sqlalchemy import JSON, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import List

class Base(DeclarativeBase):
    pass

class Connection(Base):
    __tablename__ = "connections"
    id: Mapped[int] = mapped_column(primary_key=True)
    host: Mapped[str] = mapped_column(unique=True)
    args: Mapped[List[str]] = mapped_column(
        MutableList.as_mutable(JSON),  # works in SQLite (json1)
        default=list,                  # default to []
        nullable=False,
    )

engine = create_engine("sqlite:///data.sqlite3", echo=False)
Base.metadata.create_all(engine)