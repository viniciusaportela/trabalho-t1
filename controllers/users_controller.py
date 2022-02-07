from views.user_view import UserView
from models.participant_model import Participant
from models.person_model import Person


class UsersController:
    def __init__(self, controllers_manager):
        self.__users = []
        self.__controllers_manager = controllers_manager
        self.view = UserView()

    def get_users(self):
        return self.__users

    def get_user_by_cpf(self, cpf):
        for index, user in enumerate(self.__users):
            if user.cpf == cpf:
                return user, index
        return None, -1

    def add_user(self, cpf, name, birthday, cep, street, number, complement, has_two_vaccines = None, has_covid = None, pcr_exam_date = None):
        already_has_user, _ = self.get_user_by_cpf(cpf)

        if (already_has_user):
            return False, 'Esse usuario ja existe!'

        user = None
        is_participant = has_two_vaccines != None or (has_covid != None and pcr_exam_date != None)
        if (is_participant):
            user = Participant(cpf, name, birthday, cep, street, number, complement, has_two_vaccines, has_covid, pcr_exam_date)
        else:
            user = Person(cpf, name, birthday, cep, street, number, complement)
        
        self.__users.append(user)

        return True, ''

    def edit_user(self, cpf, name, birthday, cep, street, number, complement):
        user, index = self.get_user_by_cpf(cpf)

        user.name = name
        user.birthday = birthday
        user.cep = cep
        user.address.street = street
        user.address.number = number
        user.address.complement = complement

        self.__users[index] = user

    def remove_user(self, cpf):
        for index, user in enumerate(self.__users):
            if (user.cpf == cpf):
                self.__users.pop(index)

    def set_covid_status(self, cpf, has_two_vaccines, has_covid, pcr_exam_date):
        user, index = self.get_user_by_cpf(cpf)

        participant = Participant(
            user.cpf,
            user.name,
            user.birthday,
            user.address.cep,
            user.address.street,
            user.address.number,
            user.address.complement,
            has_two_vaccines,
            has_covid,
            pcr_exam_date
        )

        self.__users[index] = participant
        self.__controllers_manager.event.update_user_reference(participant)

    def open_user_menu(self):
        bindings = {
            1: self.open_register_user,
            2: self.open_register_participant,
            3: self.open_edit_user,
            4: self.open_remove_user,
            5: self.open_user_list,
            6: self.open_find_user
        }

        option = None
        while option != 0:
            option = self.view.open_users_menu()

            if (option == 0):
                return

            bindings[option]()

    def open_register_user(self):
        user_data = self.view.show_register_user()
        address_data = self.__controllers_manager.address.view.show_register_address()
        participant_data = self.view.show_participant_register()

        has_two_vaccines = "has_two_vaccines" in participant_data and participant_data["has_two_vaccines"]
        has_covid = "has_covid" in participant_data and participant_data['has_covid']
        pcr_exam_date = "pcr_exam_date" in participant_data and participant_data["pcr_exam_date"]

        self.add_user(
            user_data["cpf"],
            user_data["name"],
            user_data["birthday"],
            address_data["cep"],
            address_data["street"],
            address_data["number"],
            address_data["complement"],
            has_two_vaccines,
            has_covid,
            pcr_exam_date,
        )

        print('Usuario adicionado!')

    def open_register_participant(self):
        user = self.open_select_user()
        if (user == None):
            return

        participant_data = self.view.show_participant_register(True)
        self.set_covid_status(
            user.cpf,
            participant_data['has_two_vaccines'],
            participant_data['has_covid'],
            participant_data['pcr_exam_date']
        )

        print('Comprovacao Covid anexada!')

    def open_edit_user(self):
        user = self.open_select_user()
        if (user == None):
            return

        user_data = self.view.show_register_user(True)
        address_data = self.__controllers_manager.address.view.show_register_address()
        self.edit_user(
            user.cpf,
            user_data["name"],
            user_data["birthday"],
            address_data["cep"],
            address_data["street"],
            address_data["number"],
            address_data["complement"],
        )

        print('Usuario Editado!')

    def open_remove_user(self):
        user = self.open_select_user()
        if (user == None):
            return

        self.remove_user(user.cpf)

        print('Usuario deletado!')

    def open_user_list(self):
        users = self.get_users()
        self.view.show_user_list(users)

    def open_find_user(self):
        user = self.open_select_user()
        if (user == None):
            return
        
        self.view.show_user_details(user)

    def open_select_user(self):
        user = None
        while True:
            user_cpf = self.view.show_find_user()

            if user_cpf == None:
                return

            user, _ = self.get_user_by_cpf(user_cpf)

            if (user):
                return user
            else:
                'Usuario nao encontrado'