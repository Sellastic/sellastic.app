from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QFont


class ToolBar(QToolBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFont(QFont("Verdana", 20))

    def add_event(self, **kwargs):
        print(kwargs)
        if "back_function" in kwargs and "back_function_caption" in kwargs:
            self.addAction(kwargs["back_function_caption"], kwargs["back_function"])
