from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFont


class Label(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFont(QFont("Verdana", 20))

    def set_color(self, background_color, foreground_color):
        self.setStyleSheet(f"QLabel {{background-color: #{background_color:06X};" +
                           f"color: #{foreground_color:06X};border-radius: 4px;}}")

    def set_event(self, function):
        self.click()

