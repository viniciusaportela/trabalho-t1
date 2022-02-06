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
            option = self.view.view_reports_menu()

            if (option == 0):
                return

            bindings[option]()
    
    def open_soon_events(self):
        pass

    def open_events_ranking_by_participants(self):
        pass

    def open_past_events(self):
        pass