from PySide6.QtCore import QTimer, Slot, QDateTime
from PySide6.QtWidgets import QStatusBar, QLabel


class StatusBar(QStatusBar):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet(
            """QStatusBar {
                padding-left:8px;
                padding-right:8px;
                background:gray;
                color:black;
                font-family:'Times New Roman';
                font-size:16pt;
            }
            """)
        date_time_timer = QTimer(self, interval=1000, timeout=self.show_date_time)
        date_time_timer.start()
        self.date_time_label = QLabel("")
        self.addPermanentWidget(self.date_time_label)
        self.show_date_time()

    @Slot()
    def show_date_time(self):
        date_time = QDateTime.currentDateTime()
        self.date_time_label.setText(
            date_time.toString('yyyy MM dd hh mm' if date_time.time().second() % 2 == 0 else 'yyyy-MM-dd hh:mm'))

