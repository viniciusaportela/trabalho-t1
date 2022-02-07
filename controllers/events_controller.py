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

    def add_event(self, title, max_participants, local, datetime, organizers):
        already_has_event = self.get_event_by_title(title)

        if (already_has_event):
            return False, 'Esse evento ja existe!'

        event = Event(title, max_participants, [], local, datetime, organizers)

        self.__events.append(event)

        return True, ''

    def open_events_menu(self):
        bindings = {
            1: self.open_register_event,
            2: self.open_edit_event,
            3: self.open_add_participant_to_event,
            4: self.open_delete_event,
            5: self.open_list_events,
            6: self.open_find_event
        }

        while True:
            option = self.view.show_events_menu()

            if (option == 0):
                return

            bindings[option]()

    def open_register_event(self):
        event_data = self.view.show_register_event()
        organizer = self.__controllers_manager.user.view.show_find_user()
        local = self.__controllers_manager
    
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