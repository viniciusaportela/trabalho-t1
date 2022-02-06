from models.person_model import Person
from models.pcr_exam_model import PCRExam

class Participant(Person):
    def __init__(self, person, has_two_vacines, has_covid, pcr_exam_date):
        super().__init__(person.cpf, person.name, person.birthday, person.cep, person.street, person.number, person.complement)
        self.__pcr_exam = PCRExam(has_covid, pcr_exam_date)
        self.__has_two_vaccines = has_two_vacines

    @property
    def pcr_exam(self):
        return self.__pcr_exam

    @pcr_exam.setter
    def pcr_exam(self, pcr_exam: str):
        self.__pcr_exam = pcr_exam

    @property
    def has_two_vaccines(self):
        return self.__has_two_vaccines

    @has_two_vaccines.setter
    def has_two_vaccines(self, has_two_vaccines: str):
        self.__has_two_vaccines = has_two_vaccines