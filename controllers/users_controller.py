from views.user_view import UserView

class UsersController:
    def __init__(self):
        self.persons = []
        self.participants = []
        self.user_view = UserView()