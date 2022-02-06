import controllers.users_controller

class ControllersManager:
    def __init__(self):
        self.__users_controller = controllers.users_controller.UsersController(self)

        self.controllers_bindings = {
            'user': self.__users_controller,
        }

    def get(self, name):
        return self.controllers_bindings[name]

controllers_manager = ControllersManager()