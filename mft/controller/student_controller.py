from mft.model.entity.student import Student
from mft.model.service.student_service import StudentService
from mft.model.tools.decorators import exception_handling


class StudentController:
    @classmethod
    @exception_handling
    def save(cls, name, family, father_name, national_id, degree, major, grade, phone_number, email_address):
        student = Student(name, family, father_name, national_id, degree, major, grade, phone_number, email_address)
        return True, StudentService.save(student)

    @classmethod
    @exception_handling
    def edit(cls, id, name, family,father_name, national_id, degree, major, grade, phone_number, email_address):
        student = Student(name, family,father_name, national_id, degree, major, grade, phone_number, email_address)
        student.id = id
        return True, StudentService.edit(student)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, StudentService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls, ):
        return True, StudentService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, StudentService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_family(cls, family):
        return True, StudentService.find_by_family(family)
