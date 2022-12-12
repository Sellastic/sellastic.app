from PySide6 import QtCore


class BackSpaceSignal (QtCore.QObject):
    signal = QtCore.Signal()


class AnimationSignal (QtCore.QObject):
    signal = QtCore.Signal(int)
