from sqlalchemy import Column, Integer, Boolean, String, ForeignKey, DateTime, Time, Date
from sqlalchemy.orm import relationship
from model.tools.validator import *
from model.entity.base import Base
from model.entity.student import Student
from model.entity.professor import Professor
from model.entity.select_course import SelectCourse
from model.entity.course import Course