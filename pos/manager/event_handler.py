from pos.data import EventName
from pos.manager.event import GeneralEvent, ReportEvent, SaleEvent, SettingEvent


class EventHandler(GeneralEvent, ReportEvent, SaleEvent, SettingEvent):
    def event_distributor(self, event_name):
        function_object = None
        match event_name:
            case EventName.NONE.name:
                pass
            case EventName.EXIT_APPLICATION.name:
                function_object = self._exit_application
            case EventName.LOGIN.name:
                function_object = self._login
            case EventName.LOGOUT.name:
                function_object = self._logout
        return function_object



