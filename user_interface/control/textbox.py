from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QFont


class TextBox(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFont(QFont("Verdana", 20))

        self.filed_name = ""

    def set_font_size(self, font_size):
        if font_size:
            self.setFont(QFont("Verdana", font_size))

    def set_password_type(self):
        self.setEchoMode(QLineEdit.Password)
