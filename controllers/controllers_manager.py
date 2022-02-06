import controllers.users_controller
import controllers.address_controller

class ControllersManager:
    def __init__(self):
        self.__users_controller = controllers.users_controller.UsersController(self)
        self.__address_controller = controllers.address_controller.AddressController(self)

        self.controllers_bindings = {
            'user': self.__users_controller,
            'address': self.__address_controller
        }

    def get(self, name):
        return self.controllers_bindings[name]

controllers_manager = ControllersManager()