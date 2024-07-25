from model.entity.course import Course
from model.service.course_service import CourseService
from model.tools.decorators import exception_handling


class CourseController:
    @classmethod
    @exception_handling
    def save(cls, code, course_name, course_type, unit_number, prerequisite, tongue, hold_type, start_date,
             end_date, professor):
        course = Course(code, course_name, course_type, unit_number, prerequisite, tongue, hold_type, start_date,
                        end_date, professor)
        return True, CourseService.save(course)

    @classmethod
    @exception_handling
    def edit(cls, id, code, course_name, course_type, unit_number, prerequisite, tongue, hold_type, start_date,
             end_date, professor):
        course = Course(code, course_name, course_type, unit_number, prerequisite, tongue, hold_type, start_date,
                        end_date, professor)
        #todo: course.id cannot be set why ???
        course.id = id
        return True, CourseService.edit(course)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, CourseService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls, ):
        return True, CourseService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, CourseService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_course_name(cls, course_name):
        return True, CourseService.find_by_course_name(course_name)
