from PyQt6.QtCore import QDate
from PyQt6.QtWidgets import QMainWindow

from src.widgets.date_chooser import DateChooser
from ui import age_calculator


class AgeCalculator(QMainWindow, age_calculator.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dateChooser = None
        self.dateDialog = None
        self.setupUi(self)

        self.toolButton.clicked.connect(self.get_age)
        self.pushButtonGetAge.clicked.connect(self.calc_age)

    def get_age(self):
        self.dateChooser = DateChooser()
        self.dateChooser.exec()
        self.dateEdit.setDate(self.dateChooser.get_date())

    def calc_age(self):
        age = QDate.currentDate().toPyDate() - self.dateEdit.date().toPyDate()
        self.lineEditResult.setText(str(age.days // 365))
