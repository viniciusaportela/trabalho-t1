from controllers.controllers_manager import controllers_manager

def init():
    users_controller = controllers_manager.get('user')
    users_controller.open_user_menu()

init()
