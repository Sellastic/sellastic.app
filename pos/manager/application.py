import sys
from PySide6.QtWidgets import QApplication
from user_interface.manager import Interface
from data_layer import *


class Application:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        self.app = QApplication([])
        self.interface = Interface()

    def run(self):
        self.interface.draw()
        sys.exit(self.app.exec())
