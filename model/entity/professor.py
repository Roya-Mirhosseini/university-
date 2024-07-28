from sqlalchemy import Column, Integer, String, Boolean
from model.entity.base import Base
from model.tools.validator import *


class Professor(Base):
    __tablename__ = "professor_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _family = Column("family", String(20), nullable=False)
    _faculty = Column("faculty", String(40), nullable=False)
    _academic_department = Column("academic_department", String(20), nullable=False)
    _employment_status = Column("employment_status", String(40), nullable=False)
    _academic_email = Column("academic_email", String(40), nullable=False)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, name, family, faculty, academic_department, employment_status,
                 academic_email, deleted=False):
        self.id = None
        self.name = name
        self.family = family
        self.faculty = faculty
        self.academic_department = academic_department
        self.employment_status = employment_status
        self.academic_email = academic_email
        self.deleted = deleted

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,20}$", "invalid professor name !!!")
    def name(self, name):
        self._name = name

    @property
    def family(self):
        return self._family

    @family.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,20}$", "invalid professor family !!!")
    def family(self, family):
        self._family = family

    @property
    def faculty(self):
        return self._faculty

    @faculty.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,50}$", "invalid faculty !!!")
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
    @pattern_validator(r"^(contractual|official)[\s]employment$", "invalid employment status !!!")
    def employment_status(self, employment_status):
        self._employment_status = employment_status

    @property
    def academic_email(self):
        return self._academic_email

    @academic_email.setter
    @pattern_validator(r"^[\w.]{2,30}@iau.ac\.ir$", "invalid academic email !!!")
    def academic_email(self, academic_email):
        self._academic_email = academic_email

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        self._deleted = deleted

