import sys
from PySide6.QtWidgets import QApplication
from user_interface.manager import Interface


class Application:
    def __init__(self):
        self.app = QApplication([])
        self.interface = Interface()

    def run(self):
        self.interface.draw()
        sys.exit(self.app.exec())
