import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from user_interface.manager import Interface
from data_layer import *
from pos.data import DisplayType


class Application:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.login_success = False
        self.display_type = DisplayType.LOGIN

        init_db()
        self.app = QApplication([])
        self.app.setApplicationName("Sellastic")
        self.app.setWindowIcon(QIcon('logo.png'))
        self.interface = Interface()

    def run(self):
        self.interface.draw()
        sys.exit(self.app.exec())
