import os
import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QFont, Qt, QIcon


class ToolBar(QToolBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFont(QFont("Verdana", 20))
        self.setMovable(False)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.setIconSize(QSize(32, 32))
        self.setLayoutDirection(Qt.LayoutDirection.RightToLeft)

    def add_event(self, **kwargs):
        if "back_function" in kwargs and "back_function_caption" in kwargs and "back_function_image" in kwargs:
            if kwargs["back_function_image"] == "":
                self.addAction(kwargs["back_function_caption"], kwargs["back_function"])
            else:
                project_path = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))
                image_path = os.path.join(project_path, 'design_files', 'images', kwargs["back_function_image"])
                self.addAction(QIcon(image_path), kwargs["back_function_caption"], kwargs["back_function"])

