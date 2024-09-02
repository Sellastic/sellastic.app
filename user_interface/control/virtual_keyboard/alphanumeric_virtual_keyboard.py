from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QSizePolicy, QLineEdit, QWidget

from user_interface.control.virtual_keyboard.key_animation_thread import KeyAnimationThread
from user_interface.control.virtual_keyboard.key_press_handler_thread import KeyPressHandlerThread
from user_interface.control.virtual_keyboard.keyboard_button import KeyboardButton
from user_interface.control.virtual_keyboard.signal import BackSpaceSignal, AnimationSignal


class AlphaNumericVirtualKeyboard(QWidget):
    """ AlphaNumericVirtualKeyboard class
    """

    def __init__(self, source=None, width=970, height=315, location_x=0, location_y=0, parent=None):
        """ AlphaNumericVirtualKeyboard class constructor

        Parameters
        ----------
       source : QLineEdit
            lineedit to which characters will be added
        width : int, optional

        height : int, optional

        location_x : int, optional
            X position of the keypad pop up (the default is 0)
        location_y : int, optional
            Y position of the keypad pop up (the default is 0)
        parent : QWidget
            Parent widget (the default is None)
        """
        super(AlphaNumericVirtualKeyboard, self).__init__(parent)

        self.setSizePolicy(QtWidgets.QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        self.CAPS_LOCK = 1
        self.NUMBER_ONLY = 2
        self.FRACTION_NUMBER = 3
        self.constraint = 0
        self.source = source
        self.parent = parent
        self.keyboard_width = width
        self.keyboard_height = height

        if location_x != 0:
            self.location_x = location_x
        else:
            self.location_x = 0
        if location_y != 0:
            self.location_y = location_y
        else:
            self.location_y = 0

        self.move_up = False
        # self.global_layout = QtWidgets.QVBoxLayout(parent)
        self.keys_layout = QtWidgets.QGridLayout(self)
        self.is_back_key_pressed = False
        self.threadPool = QtCore.QThreadPool()
        self.keyPressHandler = None
        self.backspace_signal = BackSpaceSignal()
        self.animation_signal = AnimationSignal()
        self.animation_signal_for_close = AnimationSignal()
        self.callback_method = None
        self.back_button = None
        self.caps_button = None
        self.symbol_button = None
        self.close_button = None
        self.symbol_state = False
        self.caps_state = False
        self.is_hidden = True
        self.close_ui_scroll = None
        self.key_list_by_lines_lower = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                                        ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                                        ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '.'],
                                        ['z', 'x', 'c', 'v', 'b', 'n', 'm', ',', 'Backspace'],
                                        ['Caps', ' ', 'Sym', 'Close', '  ']]

        self.key_list_by_lines_caps = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                                       ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                                       ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '.'],
                                       ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', 'Backspace'],
                                       ['Caps', ' ', 'Sym', 'Close', '  ']]

        self.key_list_by_lines_symbol = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                                         ['~', '`', '@', '#', '$', '%', '^', '&&', '*', '('],
                                         [')', '_', '-', '+', '=', '|', '[', ']', '{', "'"],
                                         ['}', '"', '<', '>', '?', '/', '\\', '!', 'Backspace'],
                                         ['Caps', ' ', 'Sym', 'Close', '  ']]

        self.array_buttons = [[0 for x in range(10)] for y in range(5)]

    def _convert_to_caps(self):
        """ AlphaNumericVirtualKeyboard class method to convert keys between upper and lower case
        """
        keys = None
        if not self.caps_state:
            self.caps_state = 1
            self.symbol_state = 0
            keys = self.key_list_by_lines_caps
            self.caps_button.setStyleSheet(
                "background-color:rgb(29, 150, 255);font-size: 20px;font-family: Noto Sans CJK JP;" +
                "border: 3px solid #8f8f91;border-radius: 8px; min-height:42px; max-height: 42px; width: 120px;")
        else:
            self.caps_state = 0
            keys = self.key_list_by_lines_lower
            self.caps_button.setStyleSheet(
                "QPushButton {font-size: 20px;font-family: Noto Sans CJK JP;border: 3px solid #8f8f91;" +
                "border-radius: 8px;" +
                "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);" +
                "min-height:42px; max-height: 42px; width: 120px;}\n" +
                "QPushButton:pressed {background-color: rgb(29, 150, 255);}")
        for line_index, line in enumerate(keys):
            for key_index, key in enumerate(line):
                if key != ' ' and key != '  ' and key != 'Backspace' and \
                        key != 'CAPS' and key != 'Close' and key != 'Sym':
                    button = self.array_buttons[line_index][key_index]
                    button.setText(key)
        self.symbol_button.setStyleSheet(
            "QPushButton {font-size: 20px;font-family: Noto Sans CJK JP;" +
            "border: 3px solid #8f8f91;border-radius: 8px;" +
            "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);" +
            "min-height:42px; max-height: 42px; width: 120px;}\n" +
            "QPushButton:pressed {background-color: rgb(29, 150, 255);}")
        self.symbol_state = 0

    def _open_symbol(self):
        keys = None
        if not self.symbol_state:
            self.symbol_state = 1
            keys = self.key_list_by_lines_symbol
            self.symbol_button.setStyleSheet(
                "background-color:rgb(29, 150, 255);font-size: 20px;font-family: Noto Sans CJK JP;" +
                "border: 3px solid #8f8f91;border-radius: 8px; min-height:42px; max-height: 42px; width: 120px;")
        elif self.caps_state:
            self.symbol_state = 0
            keys = self.key_list_by_lines_caps
            self.symbol_button.setStyleSheet(
                "QPushButton {font-size: 20px;font-family: Noto Sans CJK JP;border: 3px solid #8f8f91;" +
                "border-radius: 8px;" +
                "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);" +
                "min-height:42px; max-height: 42px; width: 120px;}\n" +
                "QPushButton:pressed {background-color: rgb(29, 150, 255);}")
        else:
            self.symbol_state = 0
            keys = self.key_list_by_lines_lower
            self.symbol_button.setStyleSheet(
                "QPushButton {font-size: 20px;font-family: Noto Sans CJK JP;border: 3px solid #8f8f91;" +
                "border-radius: 8px;" +
                "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #f6f7fa, stop: 1 #dadbde);" +
                "min-height:42px; max-height: 42px; width: 120px;}\n" +
                "QPushButton:pressed {background-color: rgb(29, 150, 255);}")
        for line_index, line in enumerate(keys):
            for key_index, key in enumerate(line):
                if key != ' ' and key != '  ' and key != 'Backspace' and \
                        key != 'Caps' and key != 'Close' and key != 'Sym':
                    button = self.array_buttons[line_index][key_index]
                    button.setText(key)

    def display(self, source, event=None, ui_scroll=None, close_button_enable=False, call_back=None, constraint=0,
                move_up=False):
        """ AlphaNumericVirtualKeyboard class method to display virtual keypad

        Parameters
        ----------
        source : QLineEdit
            lineedit to which characters will be added
        event : , optional
            
        ui_scroll : , optional
            
        close_button_enable : , optional
        
        call_back: , optional
        
        constraint: , optional
        
        move_up:  , optional
        
        """
        self.source = source
        if self.location_x == 0:
            self.location_x = int((self.parent.width() - self.keyboard_width) / 2)

        if self.location_y == 0 and self.source.pos().y() + self.source.size().height() > self.parent.height() / 2:
            self.location_y = 0
        else:
            self.location_y = self.parent.height() - self.keyboard_height

        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.setWindowState(Qt.WindowState.WindowActive)
        self.move_up = move_up
        if ui_scroll:
            self.close_ui_scroll = ui_scroll
            ui_scroll.show()
        if self.is_hidden:
            for line_index, line in enumerate(self.key_list_by_lines_lower):
                for key_index, key in enumerate(line):
                    if isinstance(self.array_buttons[line_index][key_index], KeyboardButton):
                        continue
                    if key == ' ':
                        button = KeyboardButton(key, self.parent)
                        self.array_buttons[line_index][key_index] = button
                        self.keys_layout.addWidget(button, line_index, key_index, 1, 5)
                        button.key_button_clicked_signal.connect(lambda key: self._add_input_by_key(key))
                    elif key == '  ':
                        button = KeyboardButton(key, self.parent)
                        self.array_buttons[line_index][key_index] = button
                        self.keys_layout.addWidget(button, line_index, 8, 1, 2)
                        button.key_button_clicked_signal.connect(lambda key: self._add_input_by_key(key))
                    elif key == 'Backspace':
                        self.back_button = KeyboardButton("Backspace", self)
                        self.array_buttons[line_index][key_index] = self.back_button
                        self.keys_layout.addWidget(self.back_button, line_index, key_index, 1, 2)
                        self.backspace_signal.signal.connect(self._backspace)
                        self.back_button.mousePressEvent = self._backspace_press_event
                        self.back_button.mouseReleaseEvent = self._backspace_release_event
                        self.back_button.mouseDoubleClickEvent = self._backspace_double_click
                    elif key == 'Caps':
                        self.caps_button = KeyboardButton("Caps", self)
                        self.array_buttons[line_index][key_index] = self.caps_button
                        self.keys_layout.addWidget(self.caps_button, line_index, key_index)
                        self.caps_button.key_button_clicked_signal.connect(self._convert_to_caps)
                        if self.caps_state == 1:
                            self.caps_button.setStyleSheet(
                                "background-color:rgb(29, 150, 255);border: 3px solid #8f8f91;border-radius: 8px;" +
                                "min-height:42px; max-height: 42px; width: 120px;")
                    elif key == 'Close':
                        self.close_button = KeyboardButton("Close", self)
                        self.array_buttons[line_index][key_index] = self.close_button
                        self.keys_layout.addWidget(self.close_button, line_index, 7)
                        self.close_button.key_button_clicked_signal.connect(self._close_handler)
                    elif key == 'Sym':
                        self.symbol_button = KeyboardButton("?!@#", self)
                        self.array_buttons[line_index][key_index] = self.symbol_button
                        self.keys_layout.addWidget(self.symbol_button, line_index, 6)
                        self.symbol_button.key_button_clicked_signal.connect(self._open_symbol)
                        if self.symbol_state == 1:
                            self.symbol_button.setStyleSheet(
                                "background-color:rgb(29, 150, 255);border: 3px solid #8f8f91;border-radius: 8px;" +
                                "min-height:42px; max-height: 42px; width: 20px;")
                    else:
                        button = KeyboardButton(key, self.parent)
                        self.array_buttons[line_index][key_index] = button
                        self.keys_layout.addWidget(button, line_index, key_index)
                        button.key_button_clicked_signal.connect(lambda key: self._add_input_by_key(key))

            # self.global_layout.addLayout(self.keys_layout)
            # self.move(self.x_pos, self.y_pos * 2)
            self.move(self.location_x, self.location_y)
            self.show()
            self.animation_signal.signal.connect(self._show_animate)
            animate = KeyAnimationThread(self.animation_signal.signal, self)
            animate.start()
            self.is_hidden = False
        self._set_source(event, source, call_back)
        self.constraint = constraint

        for line_index, line in enumerate(self.key_list_by_lines_lower):
            for key_index, key in enumerate(line):
                if line_index:
                    button = self.array_buttons[line_index][key_index]
                    button.setDisabled(False)

        if constraint == self.CAPS_LOCK:
            self.caps_button.setDisabled(True)
            self.caps_state = 0
            self._convert_to_caps()
        elif constraint == self.NUMBER_ONLY or constraint == self.FRACTION_NUMBER:
            for line_index, line in enumerate(self.key_list_by_lines_lower):
                for key_index, key in enumerate(line):
                    if line_index:
                        button = self.array_buttons[line_index][key_index]
                        if not (button.text() == "Backspace" or button.text() == "Enter") and \
                                ((constraint == self.FRACTION_NUMBER and not button.text() == ".") or
                                 constraint == self.NUMBER_ONLY):
                            button.setDisabled(True)
        else:
            self.caps_state = 1
            self.caps_button.setDisabled(False)
            self._convert_to_caps()

        self.close_button.key_disabled(close_button_enable)

    def _show_animate(self, val):
        pass
        # self.move(self.x_pos, 2 * self.y_pos - self.y_pos * (val) / 25)

    def _backspace_press_event(self, event):
        QtWidgets.QPushButton.mousePressEvent(self.back_button, event)
        self.keyPressHandler = KeyPressHandlerThread(self.backspace_signal.signal, "Backspace", self)
        self.keyPressHandler.start()

    def _backspace_release_event(self, event):
        QtWidgets.QPushButton.mouseReleaseEvent(self.back_button, event)
        self.keyPressHandler.setisKeyRelease(True)

    def _backspace_double_click(self, event):
        pass

    def _set_source(self, event, source, call_back=None):
        self.callback_method = call_back
        self.source = source
        if source and event:
            if isinstance(self.source, QtWidgets.QLineEdit):
                QtWidgets.QLineEdit.mousePressEvent(source, event)
            elif isinstance(self.source, QtWidgets.QTextEdit):
                QtWidgets.QTextEdit.mousePressEvent(source, event)

    def get_button_by_key(self, key):
        """ AlphaNumericVirtualKeyboard class method to get the handle of button by name

        Parameters
        ----------
        key : str
            key of the button

        Returns
        -------
        QPushbutton
            handle of the button with the assigned key
        """
        return getattr(self, "keyButton" + key.capitalize())

    def _get_key(self, val):
        if not self.symbol_state:
            return (val.lower(), val.capitalize())[self.caps_state]
        else:
            for i, e in enumerate(self.key_list_by_lines_lower):
                try:
                    pos = i, e.index(val)
                    retval = self.key_list_by_lines_symbol[pos[0]][pos[1]]
                    if retval == "&&":
                        retval = "&"
                    return retval
                except ValueError:
                    pass

    def _add_input_by_key(self, key):
        """ AlphaNumericVirtualKeyboard class method to update lineedit when a key is pressed

        Parameters
        ----------
        key : str
            key to be added to the lineedit
        """
        if not self.source:
            return

        key_to_add = self._get_key(key)
        if isinstance(self.source, QtWidgets.QGraphicsTextItem):
            cursor = self.source.textCursor()
            start = cursor.selectionStart()
            end = cursor.selectionEnd()
            if not start == end and start > end:
                temp = start
                start = end
                end = temp

            input_text = self.source.toPlainText()
            if key_to_add == '  ':
                key_to_add = "\n"
            output_string = input_text[:start] + key_to_add + input_text[end:]
            self.source.setPlainText(output_string)
            new_cursor = QtGui.QTextCursor(cursor)
            new_cursor.setPosition(start + 1, 0)
            self.source.setTextCursor(new_cursor)
            if self.callback_method:
                self.callback_method("textChange")
        else:
            if key_to_add == '  ':
                event_press = QtGui.QKeyEvent(QEvent.KeyPress, Qt.Key_Enter, Qt.NoModifier)
                QtCore.QCoreApplication.postEvent(self.source, event_press)
                event_release = QtGui.QKeyEvent(QEvent.KeyRelease, Qt.Key_Enter, Qt.NoModifier)
                QtCore.QCoreApplication.postEvent(self.source, event_release)
                return
            else:
                if self.constraint == self.FRACTION_NUMBER and "." in self.source.text() and key_to_add == ".":
                    return
                event_press = QtGui.QKeyEvent(QEvent.KeyPress, Qt.Key_1, Qt.NoModifier, key_to_add)
                QtCore.QCoreApplication.postEvent(self.source, event_press)
                event_release = QtGui.QKeyEvent(QEvent.KeyRelease, Qt.Key_1, Qt.NoModifier, key_to_add)
                QtCore.QCoreApplication.postEvent(self.source, event_release)
                return

    def _backspace(self):
        """ AlphaNumericVirtualKeyboard class method to do backspace
        """
        if isinstance(self.source, QtWidgets.QGraphicsTextItem):
            cursor = self.source.textCursor()
            # cursor_position = cursor.position()
            start = cursor.selectionStart()
            end = cursor.selectionEnd()
            if not start == end and start > end:
                temp = start
                start = end
                end = temp
            elif start == end:
                start = start - 1
            if start > -1:
                input_text = self.source.toPlainText()
                output_string = input_text[:start] + input_text[end:]
                self.source.setPlainText(output_string)
                new_cursor = QtGui.QTextCursor(cursor)
                new_cursor.setPosition(start, 0)
                self.source.setTextCursor(new_cursor)
                if self.callback_method:
                    self.callback_method("textChange")

        else:
            event = QtGui.QKeyEvent(QEvent.KeyPress, Qt.Key_Backspace, Qt.NoModifier)
            QtCore.QCoreApplication.postEvent(self.source, event)

    def _close_handler(self):
        """ AlphaNumericVirtualKeyboard class method to close the Virtual Keyboard pop up
        """
        if self.callback_method:
            self.callback_method("keyboard hidden")
        self.animation_signal_for_close.signal.connect(self._close_animate)
        animate = KeyAnimationThread(self.animation_signal_for_close.signal, self)
        animate.start()

    def _close_animate(self, val):
        self.move(self.location_x, self.location_y + self.location_y * (val) / 25)
        if val == 25:
            self.hide()
            if self.close_ui_scroll:
                self.close_ui_scroll.hide()

    def paintEvent(self, event):
        """ Overrides resizeEvent method in QtGui.QWidget

        Parameters
        ----------
        event : QResizeEvent
            event handle raised by resize event

        """
        if not self.is_hidden:
            painter = QtGui.QPainter()
            painter.begin(self)
            painter.setRenderHint(QPainter.Antialiasing)
            path = QtGui.QPainterPath()
            path.addRoundedRect(QtCore.QRectF(self.rect()), 10, 10)
            QtGui.QRegion(path.toFillPolygon(QtGui.QTransform()).toPolygon())
            pen = QtGui.QPen(Qt.gray, 1)
            painter.setPen(pen)
            painter.fillPath(path, Qt.gray)
            painter.drawPath(path)
            painter.end()

    def resize_from_parent(self):
        if self.parent.width() < self.keyboard_width:
            self.keyboard_width = self.parent.width()

        if self.parent.height() / 2 < self.keyboard_height:
            self.keyboard_height = int(self.parent.height() / 2)

    def resizeEvent(self, event):
        """ Overrides method in QtGui.QWidget

        Parameters
        ----------
        event : QtCore.QEvent
            Event handle when AddPatientScreen widget resizes

        """
        self.resize(self.keyboard_width, self.keyboard_height)
        event.accept()

    def hide(self, animation=False):
        QtWidgets.QWidget.hide(self)
        self.is_hidden = True
