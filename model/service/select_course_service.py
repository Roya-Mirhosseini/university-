from controller.exception.exeption import UniversityNotFoundError
from model.da.da import DataAccess
from model.entity.select_course import SelectCourse


class SelectCourseService:
    @classmethod
    def save(cls, select_course):
        select_course_da = DataAccess(SelectCourse)
        select_course_da.save(select_course)
        return select_course

    @classmethod
    def edit(cls, select_course):
        select_course_da = DataAccess(SelectCourse)
        if select_course_da.find_by_id(select_course.id):
            select_course_da.edit(select_course)
            return select_course
        else:
            raise UniversityNotFoundError()

    @classmethod
    def remove(cls, id):
        select_course_da = DataAccess(SelectCourse)
        if select_course_da.find_by_id(id):
            return select_course_da.remove(id)
        else:
            raise UniversityNotFoundError()

    @classmethod
    def find_all(cls, ):
        select_course_da = DataAccess(SelectCourse)
        return select_course_da.find_all()

    @classmethod
    def find_by_id(cls, id):
        select_course_da = DataAccess(SelectCourse)
        return select_course_da.find_by_id(id)

    @classmethod
    def find_by_course(cls, course):
        select_course_da = DataAccess(SelectCourse)
        return select_course_da.find_by(SelectCourse.course == course)
