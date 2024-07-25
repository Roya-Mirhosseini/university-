from controller.exception.exeption import UniversityNotFoundError
from model.da.da import DataAccess
from model.entity.course import Course


class CourseService:
    @classmethod
    def save(cls, course):
        course_da = DataAccess(Course)
        course_da.save(course)
        return course

    @classmethod
    def edit(cls, course):
        course_da = DataAccess(Course)
        if course_da.find_by_id(course.id):
            course_da.edit(course)
            return course
        else:
            raise UniversityNotFoundError()

    @classmethod
    def remove(cls, id):
        course_da = DataAccess(Course)
        if course_da.find_by_id(id):
            return course_da.remove(id)
        else:
            raise UniversityNotFoundError()

    @classmethod
    def find_all(cls, ):
        course_da = DataAccess(Course)
        return course_da.find_all()

    @classmethod
    def find_by_id(cls, id):
        course_da = DataAccess(Course)
        return course_da.find_by_id(id)

    @classmethod
    def find_by_course_name(cls, course_name):
        course_da = DataAccess(Course)
        return course_da.find_by(Course.course_name == course_name)
