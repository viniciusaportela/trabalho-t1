class UserView:
    def open_users_menu(self):
        valid_option = False
        while not valid_option:
            print('-= Menu Pessoa =-')
            print('1 - Cadastrar Pessoa')
            print('2 - Anexar comprovacao covid')
            print('3 - Editar pessoa')
            print('4 - Deletar pessoa')
            print('5 - Listar Pessoas')
            print('6 - Procurar Pessoa')
            print('0 - Voltar')
            option = int(input('Por favor insira uma opcao: '))
            if (option >= 0 and option <= 6):
                return option

    def show_attach_covid_status(self):
        pass

    def show_register_user(self):
        pass

    def show_edit_user(self):
        pass

    def show_edit_user_menu(self):
        pass

    def show_delete_user(self, user):
        pass

    def show_find_user(self):
        pass
    
    def show_user_list(self, users):
        pass

    def show_user_details(self, user):
        pass

    def show_select_user_menu(self, users):
        pass