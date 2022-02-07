from datetime import datetime
from models.participant_model import Participant


class UserView:
    def open_users_menu(self):
        while True:
            print('-----------= Menu Pessoas =-----------')
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
            else:
                print('Escolha uma opcao valida!')

    def show_register_user(self, edit_mode = False):
        print('-----------= Editar Pessoa =-----------' if edit_mode else '-----------= Cadastrar Pessoa =-----------')
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

    def show_find_user(self, headless = False):
        if (not headless):
            print('-----------= Procurar Pessoa =-----------')
        user_cpf = input('Digite o CPF ou 0 para sair: ')

        if (user_cpf == '0'):
            return None

        return user_cpf

    def show_user_list(self, users):
        print('-----------= Lista de Usuarios =-----------')
        for index, user in enumerate(users):
            print(str(index + 1) + ' - ' + user.name + ' (' + user.cpf + ')')
        input('Aperte enter para sair... ')

    def show_user_details(self, user):
        print('-----------= Usuario =-----------')
        print('Nome: ' + user.name)
        print('CPF: ' + user.cpf)
        print('Aniversario: ' + user.birthday.strftime("%d/%m/%Y"))
        print('Endereco: ' + user.address.cep + ', ' + user.address.street + ', n. ' + user.address.number + ', ' + user.address.complement)

        if (isinstance(user, Participant)):
            print('Tomou duas doses: ' + ('sim' if user.has_two_vaccines else 'nao'))
            print('Exame PCR: ' + ('positivo' if user.pcr_exam.has_covid else 'negativo'))
        
        input('Aperte enter para sair... ')

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

        has_covid = input('Qual resultado do exame(positivo/negativo)? ') == 'positivo'
        pcr_exam_date_raw = input('Qual foi a data do exame (dia/mes/ano)? ')
        pcr_exam_date_raw_splitted = pcr_exam_date_raw.split("/")
        pcr_exam_date = datetime(
            int(pcr_exam_date_raw_splitted[2]),
            int(pcr_exam_date_raw_splitted[1]),
            int(pcr_exam_date_raw_splitted[0])
        )

        return { "has_two_vaccines": False, "has_covid": has_covid, "pcr_exam_date": pcr_exam_date }