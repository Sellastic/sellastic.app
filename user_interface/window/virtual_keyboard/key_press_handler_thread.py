import threading
import time

from PySide6 import QtCore


class KeyPressHandlerThread (QtCore.QThread):

    def __init__(self, signal, key, parent):
        super(KeyPressHandlerThread, self).__init__(parent)
        self.signal = signal
        self.key = key
        self.isKeyRelease = False
        self.threadIsStarted = False
        self.lock = threading.Lock()

    def setisKeyRelease(self, flag):
        self.lock.acquire()
        self.isKeyRelease = flag
        self.lock.release()

    def checkKeyRelease(self):
        self.lock.acquire()
        val = self.isKeyRelease
        self.lock.release()
        return val

    def run(self):
        if self.key == "Backspace":
            self.setisKeyRelease(False)
            self.signal.emit()
            time.sleep(1)
            while True:
                if not self.checkKeyRelease():
                    self.signal.emit()
                    time.sleep(0.05)
                else:
                    break
        # self.threadIsStarted = False