from controller.exception.exeption import UniversityNotFoundError
from model.da.da import DataAccess
from model.entity.student import Student


class StudentService:
    @classmethod
    def save(cls, student):
        student_da = DataAccess(Student)
        student_da.save(student)
        return student

    @classmethod
    def edit(cls, student):
        student_da = DataAccess(Student)
        if student_da.find_by_id(student.id):
            student_da.edit(student)
            return student
        else:
            raise UniversityNotFoundError()

    @classmethod
    def remove(cls, id):
        student_da = DataAccess(Student)
        if student_da.find_by_id(id):
            return student_da.remove(id)
        else:
            raise UniversityNotFoundError()

    @classmethod
    def find_all(cls, ):
        student_da = DataAccess(Student)
        return student_da.find_all()

    @classmethod
    def find_by_id(cls, id):
        student_da = DataAccess(Student)
        return student_da.find_by_id(id)

    @classmethod
    def find_by_family(cls, family):
        student_da = DataAccess(Student)
        return student_da.find_by(Student.family == family)
