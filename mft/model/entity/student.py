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