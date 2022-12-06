import time

from PySide6 import QtCore


class KeyAnimationThread (QtCore.QThread):

    def __init__(self, signal, parent):
        super(KeyAnimationThread, self).__init__(parent)
        self.signal = signal

    def run(self):
        for i in range(25):
            self.signal.emit(i + 1)
            time.sleep(0.01)
