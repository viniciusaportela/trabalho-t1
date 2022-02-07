class EventsView:
    def show_events_menu(self):
        while True:
            print('-----------= Eventos =-----------')
            print('1 - Cadastrar evento')
            print('2 - Editar evento')
            print('3 - Deletar evento')
            print('4 - Listar eventos')
            print('5 - Procurar evento / Manipular evento')
            print('0 - Voltar')

            option = int(input('Selecione uma das opcoes: '))

            if (option >= 0 and option <= 5):
                return option
            else:
                print('Escolha uma opcao valida!')
    
    def show_register_event(self):
        print('-----------= Registrar Evento =-----------')
        name = input('Nome: ')
        max_participants = int(input('Max Participantes: '))
        datetime_raw = input('Data e Hora (dia/mes/ano hora:minuto): ')

        return { "name": name, "max_participants": max_participants, "event_date": datetime_raw }
    
    def show_events_list(self, events):
        print('-----------= Eventos =-----------')

        for index, event in enumerate(events):
            print(str(index +  1) + ' - ' + event.title + ' (' + event.local.name + ' - ' + event.datetime.strftime('%d/%m/%Y %H:%M') + ')')
        
        input('Aperte enter para sair... ')

    def show_event_menu(self, event):
        while True:
            print('-----------= Evento =-----------')
            print('Nome: ' + event.title)
            print('Participantes: ' + str(len(event.participants)) + '/' + str(event.max_participants))
            print('Data: ' + event.datetime.strftime('%d/%m/%Y %H:%M'))
            print('Local: ' + event.local.name)
            print('Organizador: ' + event.organizers[0].name)
            print('')
            print('1 - Cadastrar Participante')
            print('2 - Listar Participantes')
            print('3 - Listar Participantes com comprovacao Covid')
            print('4 - Listar Participantes sem comprovacao Covid')
            print('5 - Registrar entrada')
            print('6 - Registrar saida')
            print('0 - Sair')

            option = int(input('Selecione uma das opcoes: '))

            if (option >= 0 and option <= 6):
                return option
            else:
                print('Escolha uma opcao valida!')
    
    def show_find_event(self, headless = False):
        if (not headless):
            print('-----------= Procurar Evento =-----------')
        local_name = input('Digite o nome do evento ou 0 para sair: ')

        if (local_name == '0'):
            return None

        return local_name
    
    def show_participants_list(self, participants, custom_header = None):
        if (custom_header):
            print(custom_header)
        else:
            print('-----------= Participantes =-----------')

        for index, participant in enumerate(participants):
            print(str(index + 1) + ' - ' + participant.name + ' (' + participant.cpf + ')')
        
        input('Aperte enter para sair... ')

    def get_hour(self):
        date_raw = input('Horario de Entrada (H:m): ')
        date_raw_split = date_raw.split(':')

        hour = int(date_raw_split[0])
        minute = int(date_raw_split[1])

        return hour, minute

