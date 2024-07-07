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


    def __init__(self,code,course_name,course_type,unit_number,prerequisite,tongue,hold_type,start_date,end_date,professor,deleted=False):
        self._row = None
        self._code = code
        self._course_name = course_name
        self._course_type = course_type
        self._unit_number = unit_number
        self._prerequisite = prerequisite
        self._tongue = tongue
        self._hold_type = hold_type
        self._start_date = start_date
        self._end_date = end_date
        self._professor = professor
        self._deleted = deleted