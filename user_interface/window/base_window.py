import sys

from PySide6.QtWidgets import QMainWindow, QStatusBar, QToolBar
from PySide6.QtCore import Qt


class BaseWindow(QMainWindow):
    def __init__(self, display_type="main_display"):
        super().__init__(parent=None)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def draw_window(self, settings: dict, design: list):
        self.setWindowTitle(settings["name"])
        self.setGeometry(0, 0, settings["width"], settings["height"])
        if settings["toolbar"]:
            self._create_toolbar()
        if settings["statusbar"]:
            self._create_status_bar()

    def _create_toolbar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)

    def _create_status_bar(self):
        status = QStatusBar()
        status.showMessage("Status Bar")
        self.setStatusBar(status)


