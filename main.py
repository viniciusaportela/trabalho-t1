from datetime import datetime
from controllers.controllers_manager import controllers_manager
from views.main_view import MainView

class App:
    def __init__(self):
        self.view = MainView()

    def __inject_data(self):
        controllers_manager.user.add_user('12312312312', 'Vinicius', datetime(2001, 7, 4), '8800000', 'rua Porto', 220, 'Apt 100')
        controllers_manager.user.add_user('12312312313', 'Jose', datetime(2000, 2, 5), '8800000', 'rua Almeida', 10, '', True)

    def run(self):
        self.__inject_data()

        bindings = {
            1: controllers_manager.user.open_user_menu,
            2: controllers_manager.event.open_events_menu,
            3: controllers_manager.report.open_reports_menu,
        }

        while True:
            option = self.view.view_menu()

            if (option == 0):
                return

            bindings[option]()

App().run()
