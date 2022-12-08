from user_interface.window import BaseWindow
from pos.data import DisplayType
from user_interface.design_file import Interpreter


class Interface:
    def __init__(self, app):
        self.app = app
        self.window = BaseWindow(app=self.app)

    def draw(self, display_type: DisplayType):
        interpreter = Interpreter(display_type)
        print(interpreter.settings)
        print(interpreter.design)
        self.window.draw_window(interpreter.settings, interpreter.design)
        self.window.show()
        self.window.focus_text_box()

    def redraw(self, display_type: DisplayType):
        self.window.clear()
        self.draw(display_type)
