from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtGui import QPainter, Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QSizePolicy, QVBoxLayout


class NumPad(QWidget):
    def __init__(self, width=320, height=315, location_x=0, location_y=0, parent=None, *args, **kwargs):
        super(NumPad, self).__init__(*args, **kwargs)

        self.setSizePolicy(QtWidgets.QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.keys_layout = QVBoxLayout()
        self.numpad_width = width
        self.numpad_height = height
        self.location_x = location_x
        self.location_y = location_y
        print(self.numpad_width, self.numpad_height, self.location_x, self.location_y)
        parent.setLayout(self.keys_layout)

    def display(self, parent):
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setWindowState(Qt.WindowState.WindowActive)

        self.setGeometry(self.location_x, self.location_y, self.numpad_width, self.numpad_height)
        # self.show()

    def set_event(self, function):
        pass

    def resizeEvent(self, event):
        """ Overrides method in QtGui.QWidget

        Parameters
        ----------
        event : QtCore.QEvent
            Event handle when AddPatientScreen widget resizes

        """
        self.resize(self.numpad_width, self.numpad_height)
        event.accept()

    def paintEvent(self, event):
        """ Overrides resizeEvent method in QtGui.QWidget

        Parameters
        ----------
        event : QResizeEvent
            event handle raised by resize event

        """
        painter = QtGui.QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), 10, 10)
        QtGui.QRegion(path.toFillPolygon(QtGui.QTransform()).toPolygon())
        pen = QtGui.QPen(Qt.gray, 1)
        painter.setPen(pen)
        painter.fillPath(path, Qt.gray)
        painter.drawPath(path)
        painter.end()
