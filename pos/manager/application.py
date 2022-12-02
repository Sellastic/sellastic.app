import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from pos.manager.status import Status
from pos.manager.event_handler import EventHandler
from user_interface.manager import Interface
from data_layer import *


class Application(Status, EventHandler):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        Status.__init__(self)
        EventHandler.__init__(self)

        init_db()
        self.app = QApplication([])
        self.app.setApplicationName("Sellastic")
        self.app.setWindowIcon(QIcon('logo.png'))
        self.interface = Interface(self)

    def run(self):
        self.interface.draw(self.current_display_type)
        sys.exit(self.app.exec())
