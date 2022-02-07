class MainView:
    def show_menu(self):
        print('-= Menu =-')
        print('1 - Pessoas')
        print('2 - Eventos')
        print('3 - Locais')
        print('4 - Relatorios')
        print('0 - Sair')
        
        while True:
            option = int(input('Selecione uma das opcoes: '))

            if (option >= 0 and option <= 3):
                return option
            else:
                print('Escolha uma opcao valida!')