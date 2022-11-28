from user_interface.window import BaseWindow


class Interface:
    def __init__(self):
        self.window = BaseWindow()

    def draw(self):
        self.window.show()
