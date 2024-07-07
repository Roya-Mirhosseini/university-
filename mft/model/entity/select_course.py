from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, ForeignKey
from mft.model.entity.base import Base
from sqlalchemy.orm import relationship

class SelectCourse(Base):
    __tablename__ = "select_course_tbl"
    _course = Column("course", String(20), nullable=False)
    _student = Column("student", String(40), nullable=False)
    _date_time = Column("date_time", DateTime, nullable=False)
    _deleted = Column("deleted", Boolean, default=False)


    def __init__(self,course,student,date_time,deleted=False):
        self._course = course
        self._student = student
        self._date_time = date_time
        self._deleted = deleted