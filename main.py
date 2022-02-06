from datetime import datetime
from controllers.controllers_manager import controllers_manager
from views.main_view import MainView

class App:
    def __init__(self):
        self.view = MainView()

    def __inject_data(self):
        controllers_manager.user.add_user('123', 'Vini', datetime(2001, 7, 4), '123', 'a', 'b', 'test')
        controllers_manager.user.add_user('1234', 'Vini2', datetime(2001, 7, 4), '123', 'a', 'b', 'test', True)

    def run(self):
        self.__inject_data()
        # users_controller = controllers_manager.user
        # users_controller.open_user_menu()

        bindings = {
            1: controllers_manager.user.open_user_menu,
            2: controllers_manager.user.open_user_menu, ## TODO
            3: controllers_manager.report.open_reports_menu,
        }

        while True:
            option = self.view.view_menu()

            if (option == 0):
                return

            bindings[option]()

App().run()
