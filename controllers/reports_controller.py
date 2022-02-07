from datetime import datetime
from views.reports_view import ReportsView


class ReportsController:
    def __init__(self, controllers_manager):
        self.__controllers_manager = controllers_manager
        self.view = ReportsView()
    
    def open_reports_menu(self):
        bindings = {
            1: self.open_soon_events,
            2: self.open_events_ranking_by_participants,
            3: self.open_past_events
        }

        while True:
            option = self.view.show_reports_menu()

            if (option == 0):
                return

            bindings[option]()
    
    def open_soon_events(self):
        # TODO order by date
        events = self.__controllers_manager.event.get_events()

        soon_events = []
        for event in events:
            current = datetime.now()
            if (event.datetime > current):
                soon_events.append(event)

        self.view.show_report_events(soon_events, '-= Proximos Eventos =-')

    def open_events_ranking_by_participants(self):
        events = self.__controllers_manager.event.get_events()

        events_sorted = self.__sort_events(events)    

        self.view.show_report_events(events_sorted, '-= Ranking por participantes =-', True)

    def open_past_events(self):
        # TODO order by date
        events = self.__controllers_manager.event.get_events()
        
        past_events = []
        for event in events:
            current = datetime.now()
            if (event.datetime <= current):
                past_events.append(event)

        self.view.show_report_events(past_events, '-= Ultimos Eventos =-')

    def __sort_events(self, events):
        def sort_func(event):
            return len(event.participants)

        return sorted(events, key=sort_func, reverse=True)