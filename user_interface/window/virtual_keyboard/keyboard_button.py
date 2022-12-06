from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Qt


class KeyboardButton(QtWidgets.QPushButton):
    """ KeyButton class to be used by AlphaNeumericVirtualKeyboard class
    """
    key_button_clicked_signal = QtCore.Signal(str)

    def __init__(self, key, parent=None):
        """ KeyButton class constructor

        Parameters
        ----------
        key : str
            key of the button
        parent : QWidget, optional
            Parent widget (the default is None)
        """
        super(KeyboardButton, self).__init__(parent)
        self._key = key
        self.set_key(key)
        self.clicked.connect(self.emit_key)
        if key == "Backspace":
            self.setStyleSheet("QPushButton {min-width: 100px;font-size: 20px; font-family: Noto Sans CJK JP;" +
                               "max-width: 200px; min-height:40px; max-height: 40px;" +
                               "border: 3px solid #8f8f91;border-radius: 8px;" +
                               "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);}\n" +
                               "QPushButton:pressed {background-color: rgb(29, 150, 255);}")
        elif key == "  ":
            self.setStyleSheet("QPushButton {min-width: 100px;font-size: 20px;font-family: Noto Sans CJK JP;" +
                               "max-width: 200px; min-height:40px; max-height: 40px; border: 3px solid #8f8f91;" +
                               "border-radius: 8px;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);}\n" +
                               "QPushButton:pressed {background-color: rgb(29, 150, 255);}")
        elif key == " ":
            self.setStyleSheet("QPushButton {min-width: 450px;font-size: 20px;font-family: Noto Sans CJK JP; max-width: 550px;" +
                               "min-height:40px; max-height: 40px; border: 3px solid #8f8f91;border-radius: 8px;" +
                               "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);}\n" +
                               "QPushButton:pressed {background-color: rgb(29, 150, 255);}")
        else:
            self.setStyleSheet("QPushButton {min-width: 80px;font-size: 20px;font-family: Noto Sans CJK JP;" +
                               "max-width: 80px; min-height:40px; max-height: 40px; border: 3px solid #8f8f91;" +
                               "border-radius: 8px;" +
                               "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);}\n" +
                               "QPushButton:pressed {background-color: rgb(29, 150, 255);}")
        self.setFocusPolicy(Qt.NoFocus)

    def set_key(self, key):
        """ KeyButton class method to set the key and text of button

        Parameters
        ----------
        key : str
            key of the button
        """
        self._key = key
        if key == ' ':
            self.setText('Space')
            # self.resize(300, 60)
        elif key == '  ':
            self.setText('Enter')
        else:
            self.setText(key)

    def emit_key(self):
        """ KeyButton class method to return key as a qt signal
        """
        self.key_button_clicked_signal.emit(str(self._key))

    def sizeHint(self):
        """ KeyButton class method to return size

        Returns
        -------
        QSize
            Size of the created button
        """
        return QtCore.QSize(80, 80)

    def key_disabled(self, flag):
        self.setDisabled(flag)
