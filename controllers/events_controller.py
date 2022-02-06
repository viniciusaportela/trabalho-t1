from models.event_model import Event
from views.events_view import EventsView


class EventsController:
    def __init__(self, controllers_manager):
        self.__controllers_manager = controllers_manager
        self.__events = []
        self.view = EventsView()

    def get_events(self):
        return self.__events

    def get_event_by_title(self, title):
        for index, event in enumerate(self.__events):
            if event.title == title:
                return event, index
        return None, -1

    def add_event(self, title, ):
        already_has_event = self.get_event_by_title(title)

        if (already_has_event):
            return False, 'Esse evento ja existe!'

        event = Event(title, )
        
        self.__users.append(user)

        return True, ''

    def open_events_menu(self):
        bindings = {
            1: self.open_soon_events,
        }

        while True:
            option = self.view.view_events_menu()

            if (option == 0):
                return

            bindings[option]()
    
    def open_register_event(self):
        pass
    
    def open_event_menu(self, event):
        pass

    def open_edit_event(self):
        pass

    def open_add_participant_to_event(self):
        pass

    def open_delete_event(self):
        pass

    def open_list_events(self):
        pass

    def open_find_event(self):
        pass