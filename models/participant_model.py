from models.person_model import Person

class Participant(Person):
    def __init__(self, person, has_two_vacines, pcr_exam_date):
        self.__pcr_exam = PCRExam(has_covid, pcr_exam_date)
        self.__has_two_vaccines = has_two_vacines