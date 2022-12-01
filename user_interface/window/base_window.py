import sys

from PySide6.QtWidgets import QMainWindow, QStatusBar, QToolBar
from PySide6.QtCore import Qt

from user_interface.control import TextBox, Button


class BaseWindow(QMainWindow):
    def __init__(self, display_type="main_display"):
        super().__init__(parent=None)
        self.setWindowFlags(Qt.FramelessWindowHint)

    def draw_window(self, settings: dict, design: list):
        p = self.palette()
        p.setColor(self.backgroundRole(), settings['background_color'])
        p.setColor(self.foregroundRole(), settings['foreground_color'])
        self.setPalette(p)

        self.setWindowTitle(settings["name"])
        self.move(0, 0)
        self.setFixedSize(settings["width"], settings["height"])

        if settings["toolbar"]:
            self._create_toolbar()
        if settings["statusbar"]:
            self._create_status_bar()

        for control_design_data in design:
            if control_design_data["type"] == "textbox":
                self._create_textbox(control_design_data)
            if control_design_data["type"] == "button":
                self._create_button(control_design_data)

    def _create_button(self, design_data):
        print(design_data)
        button = Button(design_data["caption"], self)

        button.setGeometry(design_data["location_x"], design_data["location_y"],
                           design_data["width"], design_data["height"])

        button.set_color(design_data['background_color'], design_data['foreground_color'])

    def _create_textbox(self, design_data):
        print(design_data)
        textbox = TextBox(self)
        if design_data.get('alignment') == "left":
            textbox.setAlignment(Qt.AlignLeft)
        elif design_data.get('alignment') == "right":
            textbox.setAlignment(Qt.AlignRight)
        elif design_data.get('alignment') == "center":
            textbox.setAlignment(Qt.AlignCenter)
        if design_data.get('input_type') == "password":
            textbox.set_password_type()
        textbox.setGeometry(design_data["location_x"], design_data["location_y"],
                            design_data["width"], design_data["height"])
        textbox.set_font_size(design_data.get('font_size'))
        p = textbox.palette()
        p.setColor(textbox.backgroundRole(), design_data['background_color'])
        p.setColor(textbox.foregroundRole(), design_data['foreground_color'])
        textbox.setPalette(p)

    def _create_toolbar(self):
        tools = QToolBar()
        tools.addAction("Exit", self.close)
        self.addToolBar(tools)

    def _create_status_bar(self):
        status = QStatusBar()
        status.showMessage("Status Bar")
        self.setStatusBar(status)


