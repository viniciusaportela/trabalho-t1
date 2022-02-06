class EventsView:
    def view_events_menu():
        print('-= Eventos =-')
        print('1 - Cadastrar evento')
        print('2 - Editar evento')
        print('3 - Cadastrar participante em evento')
        print('4 - Deletar evento')
        print('5 - Listar eventos')
        print('6 - Procurar evento')
        print('0 - Voltar')

        while True:
            option = int(input('Selecione uma das opcoes: '))

            if (option >= 0 and option <= 6):
                return option
            else:
                print('Escolha uma opcao valida!')