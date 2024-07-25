from model.entity.select_course import SelectCourse
from model.service.select_course_service import SelectCourseService
from model.tools.decorators import exception_handling


class SelectCourseController:
    @classmethod
    @exception_handling
    def save(cls, course, student, date_time):
        select_course = SelectCourse(course, student, date_time)
        return True, SelectCourseService.save(select_course)

    @classmethod
    @exception_handling
    def edit(cls, id, course, student, date_time):
        select_course = SelectCourse(course, student, date_time)
        select_course.id = id
        return True, SelectCourseService.edit(select_course)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, SelectCourseService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls, ):
        return True, SelectCourseService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, SelectCourseService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_course(cls, course):
        return True, SelectCourseService.find_by_course(course)
