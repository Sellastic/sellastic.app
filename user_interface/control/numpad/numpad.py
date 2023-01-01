from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtGui import QPainter, Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QSizePolicy, QVBoxLayout, QAbstractButton


class NumPad(QAbstractButton):
    def __init__(self, width=320, height=315, location_x=0, location_y=0, parent=None, *args, **kwargs):
        QAbstractButton.__init__(self, parent=parent, *args, **kwargs)

        self.parent = parent
        self.numpad_width = width
        self.numpad_height = height
        self.location_x = location_x
        self.location_y = location_y
        print(self.numpad_width, self.numpad_height, self.location_x, self.location_y)

    staticMetaObject = QtCore.QMetaObject()

    def display(self, parent):
        self.layout.move(self.location_x, self.location_y)
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
        pass
