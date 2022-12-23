from PySide6.QtWidgets import QWidget


class NumPad(QWidget):
    def __init__(self, source=None, width=970, height=315, x_pos=0, y_pos=0, parent=None):
        super(NumPad, self).__init__(parent)

    def set_event(self, function):
        pass
