from user_interface.window import BaseWindow
from settings import data


class Interface:
    def __init__(self):
        self.window = BaseWindow()

    def draw(self):
        # with open("design_files//"+data.design_files, "rb") as file_object:
        #     pass
        self.window.show()
