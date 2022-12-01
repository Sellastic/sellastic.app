from user_interface.window import BaseWindow
from settings import env_data
from pos.data import DisplayType
from user_interface.design_file import Interpreter


class Interface:
    def __init__(self):
        self.window = BaseWindow()

    def draw(self, display_type: DisplayType):
        interpreter = Interpreter(display_type)
        print(interpreter.settings)
        print(interpreter.design)
        self.window.draw_window(interpreter.settings, interpreter.design)
        self.window.show()
