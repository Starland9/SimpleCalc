from PyQt6.QtWidgets import QDialog, QWidget, QCalendarWidget, QGridLayout


# noinspection PyUnresolvedReferences
class DateChooser(QDialog, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.calendar = QCalendarWidget()
        self.calendar.clicked.connect(self.get_date)

        layout = QGridLayout()
        layout.addWidget(self.calendar)

        self.setLayout(layout)

    def get_date(self):
        date = self.calendar.selectedDate()
        self.close()
        return date
