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