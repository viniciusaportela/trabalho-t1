class ControllersManager:
    def __init__(self):
        self.__user_controller = UserController()
        self.__participant_controller = ParicipantController()

        self.controllers_bindings = {
            'user': self.__user_controller,
            'participant': self.__participant_controller
        }

    def get(self, name):
        return self.controllers_bindings[name]

controllersManager = ControllersManager()