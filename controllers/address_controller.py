from views.address_view import AddressView

class AddressController:
    def __init__(self, controllers_manager):
        self.controllers_manager = controllers_manager
        self.view = AddressView()