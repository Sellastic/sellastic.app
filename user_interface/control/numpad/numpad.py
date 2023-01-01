from PySide6 import QtGui, QtCore, QtWidgets
from PySide6.QtGui import QPainter, Qt
from PySide6.QtWidgets import QWidget, QGridLayout, QSizePolicy


class NumPad(QWidget):
    def __init__(self, width=320, height=315, x_pos=0, y_pos=0, parent=None):
        super(NumPad, self).__init__(parent)

        self.setSizePolicy(QtWidgets.QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.keys_layout = QGridLayout(self)
        self.numpad_width = width
        self.numpad_height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.display(parent=parent)

    def display(self, parent):
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)
        self.setWindowState(Qt.WindowState.WindowActive)

        self.move(self.x_pos, self.y_pos)
        self.show()

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
        if not self.is_hidden:
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
