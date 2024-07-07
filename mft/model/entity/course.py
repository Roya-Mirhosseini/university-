from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, ForeignKey
from mft.model.entity.base import Base
from sqlalchemy.orm import relationship


class Course(Base):
    __tablename__ = "course_tbl"
    _row = Column("row", Integer, primary_key=True, autoincrement=True)
    # todo: is code considered as int or char?
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

    def __init__(self, code, course_name, course_type, unit_number, prerequisite, tongue, hold_type, start_date,
                 end_date, professor, deleted=False):
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

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, row):
        self._row = row

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, course_name):
        self._course_name = course_name

    @property
    def course_type(self):
        return self._course_type

    @course_type.setter
    def course_type(self, course_type):
        self._course_type = course_type

    @property
    def unit_number(self):
        return self._unit_number

    @unit_number.setter
    def unit_number(self, unit_number):
        self._unit_number = unit_number

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
    def tongue(self, tongue):
        self._tongue = tongue

    @property
    def hold_type(self):
        return self._hold_type

    @hold_type.setter
    def hold_type(self, hold_type):
        self._hold_type = hold_type

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        self._end_date = end_date

    @property
    def professor(self):
        return self._professor

    @professor.setter
    def professor(self, professor):
        self._professor = professor

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        self._deleted = deleted
