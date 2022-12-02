from pos.data import EventName


class EventHandler:
    app = None  # just for ignore warning

    def event_distributor(self, event_name):
        function_object = None
        match event_name:
            case EventName.NONE.name:
                pass
            case EventName.EXIT_APPLICATION.name:
                function_object = self._exit_application
            case EventName.LOGIN:
                function_object = self._login
        return function_object

    def _exit_application(self):
        self.app.quit()

    def _login(self):
        pass
