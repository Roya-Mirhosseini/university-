from sqlalchemy import Column, Integer, Float, String, Boolean, DateTime, ForeignKey
from mft.model.entity.base import Base
from sqlalchemy.orm import relationship


class Student(Base):
    __tablename__ = "student_tbl"
    _student_id = Column("student_id", Integer, primary_key=True, autoincrement=True)
    _student_name = Column("student_name", String(20), nullable=False)
    _student_family = Column("student_family", String(20), nullable=False)
    _father_name = Column("father_name", String(20), nullable=False)
    _national_id = Column("national_id", String(10), nullable=False)
    _degree = Column("degree", String(20), nullable=False)
    _major = Column("major", String(20), nullable=False)
    _grade = Column("grade", Float, nullable=False)
    _phone_number = Column("phone_number", String(14), nullable=False)
    _email_address = Column("email_address", String(40), nullable=False)
    _deleted = Column("deleted", Boolean, default=False)

    def __init__(self, student_name, student_family, father_name, national_id, degree, major, grade, phone_number,
                 email_address, deleted=False):
        self._student_id = None
        self._student_name = student_name
        self._student_family = student_family
        self._father_name = father_name
        self._national_id = national_id
        self._degree = degree
        self._major = major
        self._grade = grade
        self._phone_number = phone_number
        self._email_address = email_address
        self._deleted = deleted

        @property
        def student_id(self):
            return self._student_id

        @student_id.setter
        def student_id(self, student_id):
            self._student_id = student_id

        @property
        def student_name(self):
            return self._student_name

        @student_name.setter
        def student_name(self, student_name):
            self._student_name = student_name

        @property
        def student_family(self):
            return self._student_family

        @student_family.setter
        def student_family(self, student_family):
            self._student_family = student_family

        @property
        def father_name(self):
            return self._father_name

        @father_name.setter
        def father_name(self, father_name):
            self._father_name = father_name

        @property
        def national_id(self):
            return self._national_id

        @national_id.setter
        def national_id(self, national_id):
            self._national_id = national_id

        @property
        def degree(self):
            return self._degree

        @degree.setter
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
        def phone_number(self, phone_number):
            self._phone_number = phone_number

        @property
        def email_address(self):
            return self._email_address

        @email_address.setter
        def email_address(self, email_address):
            self._email_address = email_address

        @property
        def deleted(self):
            return self._deleted

        @deleted.setter
        def deleted(self, deleted):
            self._deleted = deleted
