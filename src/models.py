from sqlalchemy import Table, Column, String, Integer, MetaData, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from typing import Annotated
import enum

from database import Base



intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = 
updated_at = 




class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"


class WorkersOrm(Base):
    __tablename__ = "workers"
    id: Mapped[intpk]
    username: Mapped[str] = mapped_column()


class ResumeOrm(Base):
    __tablename__ = "resumes"
    id: Mapped[int]
    title: Mapped[str]
    compensation: Mapped[int | None]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id",ondelete='CASCADE'))
    created_at:Mapped[datetime] = mapped_column(server_default=text('TIMEZONE("utc",now())'))
    updated_at:Mapped[datetime] = mapped_column(server_default=text('TIMEZONE("utc",now())'),
                                                onupdate=datetime.utcnow)
    












э






metadat_obj = MetaData()


workers_table = Table(
    "workers",
    metadat_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String),
)
