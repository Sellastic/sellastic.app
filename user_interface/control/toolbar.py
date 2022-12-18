import os
import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QFont, Qt, QIcon

from settings import env_data


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
                image_path = os.path.join(env_data.image_absolute_folder, kwargs["back_function_image"])
                self.addAction(QIcon(image_path), kwargs["back_function_caption"], kwargs["back_function"])

