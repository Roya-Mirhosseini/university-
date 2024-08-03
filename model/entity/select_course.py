from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
from model.entity.base import Base
from sqlalchemy.orm import relationship


class SelectCourse(Base):
    __tablename__ = "select_course_tbl"
    _id = Column("id", Integer, primary_key=True, autoincrement=True)

    _course_id = Column("course_id",Integer, ForeignKey("course_tbl.id"))
    course = relationship("Course")

    _student_id = Column("student_id", Integer, ForeignKey("student_tbl.id"))
    student = relationship("Student")

    _date_time = Column("date_time", DateTime, nullable=False)
    _deleted = Column("deleted", Boolean, default=False)


    def __init__(self,course,student,date_time,deleted=False):
        self._id = None
        self._course_id = course
        self._student_id = student
        self._date_time = date_time
        self._deleted = deleted




    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id


    @property
    def course_id(self):
        return self._course_id

    @course_id.setter
    def course_id(self, course_id):
        self._course_id = course_id

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, student_id):
        self._student_id = student_id

    @property
    def date_time(self):
        return self._date_time

    @date_time.setter
    def date_time(self, date_time):
        self._date_time = date_time

    @property
    def deleted(self):
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        self._deleted = deleted
