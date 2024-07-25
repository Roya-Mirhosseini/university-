from model.entity.professor import Professor
from model.service.professor_service import ProfessorService
from model.tools.decorators import exception_handling


class ProfessorController:
    @classmethod
    @exception_handling
    def save(cls, name, family, faculty, academic_department, employment_status,
             academic_email):
        professor = Professor(name, family, faculty, academic_department, employment_status,
                              academic_email)
        return True, ProfessorService.save(professor)

    @classmethod
    @exception_handling
    def edit(cls, id, name, family, faculty, academic_department, employment_status,
             academic_email):
        professor = Professor(name, family, faculty, academic_department, employment_status,
                              academic_email)
        professor.id = id
        return True, ProfessorService.edit(professor)

    @classmethod
    @exception_handling
    def remove(cls, id):
        return True, ProfessorService.remove(id)

    @classmethod
    @exception_handling
    def find_all(cls, ):
        return True, ProfessorService.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, id):
        return True, ProfessorService.find_by_id(id)

    @classmethod
    @exception_handling
    def find_by_family(cls, family):
        return True, ProfessorService.find_by_family(family)
