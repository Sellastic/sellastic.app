import sys

from PySide6.QtWidgets import QMainWindow, QStatusBar, QToolBar
from PySide6.QtCore import Qt


class BaseWindow(QMainWindow):
    def __init__(self, display_type="main_display"):
        super().__init__(parent=None)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def draw_window(self, settings: dict, design: list):
        p = self.palette()
        p.setColor(self.backgroundRole(), settings['background_color'])
        p.setColor(self.foregroundRole(), settings['foreground_color'])
        self.setPalette(p)

        self.setStyleSheet(f"background-color: {settings['background_color']:02X};")
        self.setWindowTitle(settings["name"])
        self.setGeometry(0, 0, settings["width"], settings["height"])
        self.setFixedSize(settings["width"], settings["height"])

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


