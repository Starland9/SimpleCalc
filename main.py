import sys

from PyQt6.QtWidgets import QApplication

from src.calculator_window import CalculatorWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorWindow()
    window.show()
    sys.exit(app.exec())
