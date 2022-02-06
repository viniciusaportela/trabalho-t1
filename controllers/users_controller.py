from views.user_view import UserView
from models.participant_model import Participant
from models.person_model import Person

class UsersController:
    def __init__(self, controllers_manager):
        self.users = []
        self.view = UserView()
        self.controllers_manager = controllers_manager

    def get_users(self):
        return self.users

    def get_user_by_cpf(self, cpf):
        for user in self.users:
            if user['cpf'] == cpf:
                return user
        return None

    def add_user(self, cpf, name, birthday, cep, street, number, complement, has_two_vaccines, has_covid, pcr_exam_date):
        user = None
        is_participant = has_two_vaccines != None and has_covid != None and pcr_exam_date != None
        if (is_participant):
            user = Participant(cpf, name, birthday, cep, street, number, complement, has_two_vaccines, has_covid, pcr_exam_date)
        else:
            user = Person(cpf, name, birthday, cep, street, number, complement)
        
        self.users.append(user)
    
    def edit_user(self, cpf, name, birthday, cep, street, number, complement):
        updated_user = self.get_person_by_cpf(cpf)

        updated_user.name = name
        updated_user.birthday = birthday
        updated_user.cep = cep
        updated_user.address.street = street
        updated_user.address.number = number
        updated_user.address.complement = complement

        for index, user in enumerate(self.users):
            if (user['cpf'] == cpf):
                self.users[index] = updated_user
    
    def remove_user(self, cpf):
        for index, person in enumerate(self.users):
            if (person['cpf'] == cpf):
                self.users.pop(index)

    def can_participate_event(cpf):
        pass

    def set_covid_status():
        pass

    def open_user_menu(self):
        bindings = {
            1: self.open_register_user,
            2: self.view.show_attach_covid_status,
            3: self.view.show_edit_user,
            4: self.view.show_delete_user,
            5: self.view.show_user_list,
            6: self.view.show_find_user
        }

        option = None
        while option != 0:
            option = self.view.open_users_menu()
            bindings[option]()

    def open_register_user(self):
        user_data = self.view.show_register_user()
        address_data = self.controllers_manager.get('address').view.view_register_address()
        participant_data = self.view.show_participant_register()

        has_two_vaccines = participant_data["has_two_vaccines"]

        self.add_user(
            user_data["cpf"],
            user_data["name"],
            user_data["birthday"],
            address_data["cep"],
            address_data["street"],
            address_data["number"],
            address_data["complement"],
            has_two_vaccines,
            participant_data["has_covid"],
            participant_data["pcr_exam_date"],
        )

        print('Usuario adicionado!')

    def open_set_covid_status():
        pass
