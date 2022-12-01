from PySide6.QtWidgets import QPushButton
from PySide6.QtGui import QFont


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFont(QFont("Verdana", 20))

    def set_color(self, background_color, foreground_color):
        self.setStyleSheet(f"QPushButton {{background-color: #{background_color:06X}; color: #{foreground_color:06X};}}")
