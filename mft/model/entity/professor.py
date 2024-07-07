from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, ForeignKey
from mft.model.entity.base import Base
from sqlalchemy.orm import relationship


class Professor(Base):
    __tablename__ = "professor_tbl"
    _professor_id = Column("professor_id", Integer, primary_key=True, autoincrement=True)
    _professor_name = Column("professor_name", String(20), nullable=False)
    _professor_family = Column("professor_family", String(20), nullable=False)
    _faculty = Column("faculty", String(20), nullable=False)
    _academic_department = Column("academic_department", String(20), nullable=False)
    _employment_status = Column("employment_status", String(20), nullable=False)
    _academic_email = Column("academic_email", String(40), nullable=False)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, professor_name, professor_family, faculty, academic_department, employment_status,
                 academic_email, deleted=False):
        self._professor_id = None
        self._professor_name = professor_name
        self._professor_family = professor_family
        self._faculty = faculty
        self._academic_department = academic_department
        self._employment_status = employment_status
        self._academic_email = academic_email
        self._deleted = deleted

    @property
    def professor_id(self):
        return self._professor_id

    @professor_id.setter
    def professor_id(self, professor_id):
        self._professor_id = professor_id

    @property
    def professor_name(self):
        return self._professor_name

    @professor_name.setter
    def professor_name(self, professor_name):
        self._professor_name = professor_name

    @property
    def professor_family(self):
        return self._professor_family

    @professor_family.setter
    def professor_family(self, professor_family):
        self._professor_family = professor_family

    @property
    def faculty(self):
        return self._faculty

    @faculty.setter
    def faculty(self, faculty):
        self._faculty = faculty

    @property
    def academic_department(self):
        return self._academic_department

    @academic_department.setter
    def academic_department(self, academic_department):
        self._academic_department = academic_department

    @property
    def employment_status(self):
        return self._employment_status

    @employment_status.setter
    def employment_status(self, employment_status):
        self._employment_status = employment_status

    @property
    def academic_email(self):
        return self._academic_email

    @academic_email.setter
    def academic_email(self, academic_email):
        self._academic_email = academic_email

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        self._deleted = deleted
