from pos.data import EventName
from pos.manager.event import GeneralEvent, ReportEvent, SaleEvent, ConfigurationEvent


class EventHandler(GeneralEvent, ReportEvent, SaleEvent, ConfigurationEvent):
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
            case EventName.SALE.name:
                function_object = self._sale
            case EventName.CONFIG.name:
                function_object = self._configuration
            case EventName.CLOSURE.name:
                function_object = self._closure
            case EventName.BACK.name:
                function_object = self._back
        return function_object



