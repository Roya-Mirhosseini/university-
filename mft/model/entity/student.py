from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, ForeignKey
from mft.model.entity.base import Base
from mft.model.tools.validator import *
from sqlalchemy.orm import relationship
from mft.model.tools.validator import pattern_validator


class Student(Base):
    __tablename__ = "student_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)
    _name = Column("name", String(20), nullable=False)
    _family = Column("family", String(20), nullable=False)
    _father_name = Column("father_name", String(20), nullable=False)
    _national_id = Column("national_id", String(10), nullable=False)
    _degree = Column("degree", String(20), nullable=False)
    _major = Column("major", String(20), nullable=False)
    _grade = Column("grade", Float, nullable=False)
    _phone_number = Column("phone_number", String(20), nullable=False)
    _email_address = Column("email_address", String(50), nullable=False)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, name, family, father_name, national_id, degree, major, grade, phone_number,
                 email_address, deleted=False):
        self.id = None
        self.name = name
        self.family = family
        self.father_name = father_name
        self.national_id = national_id
        self.degree = degree
        self.major = major
        self.grade = grade
        self.phone_number = phone_number
        self.email_address = email_address
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
    @pattern_validator(r"^[a-zA-Z\s]{2,20}$", "invalid student name !!!")
    def name(self, name):
        self._name = name

    @property
    def family(self):
        return self._family

    @family.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,20}$", "invalid student family !!!")
    def family(self, family):
        self._family = family

    @property
    def father_name(self):
        return self._father_name

    @father_name.setter
    @pattern_validator(r"^[a-zA-Z\s]{2,20}$", "invalid father's name !!!")
    def father_name(self, father_name):
        self._father_name = father_name

    @property
    def national_id(self):
        return self._national_id

    @national_id.setter
    @pattern_validator(r"(\d{10}|\d{3}-\d{6}-\d)", "invalid national id !!!")
    def national_id(self, national_id):
        self._national_id = national_id

    @property
    def degree(self):
        return self._degree

    @degree.setter
    @pattern_validator(r"^(bachelor|master|doctrate)$", "invalid degree !!!")
    def degree(self, degree):
        self._degree = degree

    @property
    def major(self):
        return self._major

    @major.setter
    def major(self, major):
        self._major = major

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    @pattern_validator(r"^(09|\+989)\d{9}$", "invalid phone number !!!")
    def phone_number(self, phone_number):
        self._phone_number = phone_number

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    @pattern_validator(r"^[\w.]{2,30}@(gmail|yahoo)\.com$", "invalid email address!!!")
    def email_address(self, email_address):
        self._email_address = email_address

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        self._deleted = deleted
