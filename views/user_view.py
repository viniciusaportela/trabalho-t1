from datetime import datetime


class UserView:
    def open_users_menu(self):
        valid_option = False
        while not valid_option:
            print('-= Menu Pessoas =-')
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

    def show_register_user(self, edit_mode = False):
        print('-= Editar Pessoa =-' if edit_mode else '-= Cadastrar Pessoa =-')
        name = input('Nome: ')
        cpf = None
        if (not edit_mode):
            cpf = input('CPF: ')
        birthday_raw = input('Data Nascimento (dia/mes/ano): ')
        birthday_raw_split = birthday_raw.split("/")
        birthday = datetime(
            int(birthday_raw_split[2]),
            int(birthday_raw_split[1]),
            int(birthday_raw_split[0])
        )
        return { "name": name, "cpf": cpf, "birthday": birthday }

    def show_edit_user(self):
        pass

    def show_edit_user_menu(self):
        pass

    def show_delete_user(self, user):
        pass

    def show_find_user(self):
        print('-= Procurar Pessoa =-')
        user_cpf = input('Digite o CPF ou 0 para sair: ')

        if (user_cpf == '0'):
            return None

        return user_cpf
    
    def show_user_list(self, users):
        pass

    def show_user_details(self, user):
        pass

    def show_select_user_menu(self, users):
        pass

    def show_participant_register(self, skip_first_ask = False):
        has_covid_proof = True
        if (not skip_first_ask):
            has_covid_proof = input("Tem alguma comprovacao contra covid (s/n)? ").lower() == 's'

        if not has_covid_proof:
            return { "has_two_vaccines": None, "has_covid": None, "pcr_exam_date": None }

        has_two_vaccines = input('Tomou duas doses (s/n)? ') == 's'

        if (has_two_vaccines):
            return { "has_two_vaccines": has_two_vaccines, "has_covid": None, "pcr_exam_date": None }
        
        has_pcr_test = input('Fez um teste PCR (s/n)? ') == 's'

        if (not has_pcr_test):
            return { "has_two_vaccines": None, "has_covid": None, "pcr_exam_date": None }

        has_covid = input('Qual resultado do exame? (positivo/negativo)') == 'positivo'
        pcr_exam_date_raw = input('Qual foi a data do exame (dia/mes/ano)? ')
        pcr_exam_date_raw_splitted = pcr_exam_date_raw.split("/")
        pcr_exam_date = datetime(
            int(pcr_exam_date_raw_splitted[2]),
            int(pcr_exam_date_raw_splitted[1]),
            int(pcr_exam_date_raw_splitted[0])
        )

        return { "has_two_vaccines": False, "has_covid": has_covid, "pcr_exam_date": pcr_exam_date }
        
        
