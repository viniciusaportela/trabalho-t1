class MainView:
    def show_menu(self):
        while True:
            print('-----------= Menu =-----------')
            print('1 - Pessoas')
            print('2 - Eventos')
            print('3 - Locais')
            print('4 - Relatorios')
            print('0 - Sair')
        
            option = int(input('Selecione uma das opcoes: ') or '-1')

            if (option >= 0 and option <= 4):
                return option
            else:
                print('Escolha uma opcao valida!')