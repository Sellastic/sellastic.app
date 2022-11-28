import sys

from PySide6.QtWidgets import QMainWindow, QStatusBar, QToolBar
from PySide6.QtCore import Qt


class BaseWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Sellastic")
        self.setGeometry(0, 0, 1280, 640)
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


