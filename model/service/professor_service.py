from controller.exception.exeption import UniversityNotFoundError
from model.da.da import DataAccess
from model.entity.professor import Professor


class ProfessorService:
    @classmethod
    def save(cls, professor):
        professor_da = DataAccess(Professor)
        professor_da.save(professor)
        return professor

    @classmethod
    def edit(cls, professor):
        professor_da = DataAccess(Professor)
        if professor_da.find_by_id(professor.id):
            professor_da.edit(professor)
            return professor
        else:
            raise UniversityNotFoundError()

    @classmethod
    def remove(cls, id):
        professor_da = DataAccess(Professor)
        if professor_da.find_by_id(id):
            return professor_da.remove(id)
        else:
            raise UniversityNotFoundError()

    @classmethod
    def find_all(cls, ):
        professor_da = DataAccess(Professor)
        return professor_da.find_all()

    @classmethod
    def find_by_id(cls, id):
        professor_da = DataAccess(Professor)
        return professor_da.find_by_id(id)

    @classmethod
    def find_by_family(cls, family):
        professor_da = DataAccess(Professor)
        return professor_da.find_by(Professor.family == family)
