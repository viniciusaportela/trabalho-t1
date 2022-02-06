import controllers.users_controller
import controllers.address_controller
import controllers.reports_controller

class ControllersManager:
    def __init__(self):
        self.user = controllers.users_controller.UsersController(self)
        self.address = controllers.address_controller.AddressController(self)
        self.report = controllers.reports_controller.ReportsController(self)

controllers_manager = ControllersManager()