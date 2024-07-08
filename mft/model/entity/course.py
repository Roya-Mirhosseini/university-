from sqlalchemy import Column, Integer, Float, String, Boolean, Date, ForeignKey
from mft.model.entity.base import Base
from sqlalchemy.orm import relationship
from mft.model.tools.validator import *


class Course(Base):
    __tablename__ = "course_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _code = Column("code", String(20), nullable=False)
    _course_name = Column("course_name", String(20), nullable=False)
    _course_type = Column("course_type", String(20), nullable=False)
    _unit_number = Column("unit_number", Integer, nullable=False)
    _prerequisite = Column("prerequisite", String(20), nullable=False)
    _tongue = Column("tongue", String(20), nullable=False)
    _hold_type = Column("hold_type", String(20), nullable=False)
    _start_date = Column("start_date", Date, nullable=False)
    _end_date = Column("end_date", Date, nullable=False)
    _deleted = Column("deleted", Boolean, default=False)

    _professor_id = Column("professor_id", Integer, ForeignKey("professor_tbl.id"))
    proffesor = relationship("Professor")

    def __init__(self, code, course_name, course_type, unit_number, prerequisite, tongue, hold_type, start_date,
                 end_date,professor, deleted=False):
        self._id = None
        self._code = code
        self._course_name = course_name
        self._course_type = course_type
        self._unit_number = unit_number
        self._prerequisite = prerequisite
        self._tongue = tongue
        self._hold_type = hold_type
        self._start_date = start_date
        self._end_date = end_date
        self._professor_id = professor.id
        self._deleted = deleted

    @property
    def id(self):
        return self._id

    @id.setter
    def row(self, id):
        self._id = id

    @property
    def code(self):
        return self._code

    @code.setter
    @pattern_validator(r"^[\d\-\#]{1,9}$", "invalid code !!!")
    def code(self, code):
        self._code = code

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    @pattern_validator(r"^[a-zA-Z\s\d]{2,20}$", "invalid course name !!!")
    def course_name(self, course_name):
        self._course_name = course_name

    @property
    def course_type(self):
        return self._course_type

    @course_type.setter
    @pattern_validator(r"^(theoretical|practical)$", "invalid course type !!!")
    def course_type(self, course_type):
        self._course_type = course_type

    @property
    def unit_number(self):
        return self._unit_number

    @unit_number.setter
    def unit_number(self, unit_number):
        if isinstance(unit_number, int):
            self._unit_number = unit_number
        else:
            raise ValueError("invalid unit number")

    @property
    def prerequisite(self):
        return self._prerequisite

    @prerequisite.setter
    def prerequisite(self, prerequisite):
        self._prerequisite = prerequisite

    @property
    def tongue(self):
        return self._tongue

    @tongue.setter
    @pattern_validator(r"^(english|french|persion)$", "invalid tongue !!!")
    def tongue(self, tongue):
        self._tongue = tongue

    @property
    def hold_type(self):
        return self._hold_type

    @hold_type.setter
    @pattern_validator(r"^(in person|distance learning)$", "invalid hold type !!!")
    def hold_type(self, hold_type):
        self._hold_type = hold_type

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    @date_time_validator("invalid start date")
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    @date_time_validator("invalid end date")
    def end_date(self, end_date):
        self._end_date = end_date

    @property
    def professor_id(self):
        return self._professor_id

    @professor_id.setter
    def professor_id(self, professor_id):
        self._professor_id = professor_id

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        self._deleted = deleted
