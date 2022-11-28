import sys

from PySide6.QtWidgets import QMainWindow, QStatusBar, QToolBar
from PySide6.QtCore import Qt
import settings


class BaseWindow(QMainWindow):
    def __init__(self, display_type="main_display"):
        super().__init__(parent=None)
        self.setWindowTitle("Sellastic")
        if display_type == "main_display":
            self.setGeometry(0, 0, settings.data.md_width, settings.data.md_height)
        elif display_type == "customer_display":
            self.setGeometry(0, 0, settings.data.cd_width, settings.data.cd_height)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self._create_toolbar()
        self._create_status_bar()

    def _create_toolbar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)

    def _create_status_bar(self):
        status = QStatusBar()
        status.showMessage("Status Bar")
        self.setStatusBar(status)


