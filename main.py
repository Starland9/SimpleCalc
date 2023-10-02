import sys

from PyQt6.QtWidgets import QApplication

from src.age_calculator import AgeCalculator
from src.calculator_window import CalculatorWindow
from src.convertor import Convertor

if __name__ == '__main__':
    app = QApplication(sys.argv)
    c = Convertor()
    cc = CalculatorWindow()
    a = AgeCalculator()
    c.show()
    cc.show()
    a.show()
    sys.exit(app.exec())
