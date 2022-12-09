from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QFont


class TextBox(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setFont(QFont("Verdana", 20))
        self.setStyleSheet("QLineEdit {border-radius: 4px;}")

        self.filed_name = ""
        self.__keyboard = None

    def set_font_size(self, font_size):
        if font_size:
            self.setFont(QFont("Verdana", font_size))

    def set_password_type(self):
        self.setEchoMode(QLineEdit.EchoMode.Password)

    def focusInEvent(self, event):
        if self.__keyboard and self.__keyboard.is_hidden:
            self.__keyboard.display(source=self)
            self.repaint()
            event.accept()

    def focusOutEvent(self, event):
        if self.keyboard:
            self.keyboard.hide()
            self.repaint()
            event.accept()

    @property
    def keyboard(self):
        return self.__keyboard

    @keyboard.setter
    def keyboard(self, value):
        self.__keyboard = value
