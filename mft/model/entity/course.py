from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, ForeignKey
from mft.model.entity.base import Base
from sqlalchemy.orm import relationship

class Course(Base):
    __tablename__ = "course_tbl"
    _row = Column("row", Integer, primary_key=True, autoincrement=True)
    #todo: is code considered as int or char?
    _code = Column("code", String(20), nullable=False)
    _course_name = Column("course_name", String(20), nullable=False)
    _course_type = Column("course_type", String(20), nullable=False)
    _unit_number = Column("unit_number", Integer, nullable=False)
    _prerequisite = Column("prerequisite", String(20), nullable=False)
    _tongue = Column("tongue", String(20), nullable=False)
    _hold_type = Column("hold_type", String(20), nullable=False)
    _start_date = Column("start_date", DateTime, nullable=False)
    _end_date = Column("end_date", DateTime, nullable=False)
    _professor = Column("professor", String(20), nullable=False)
    _deleted = Column("deleted", Boolean, default=False)