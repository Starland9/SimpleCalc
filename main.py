import sys

from PyQt6.QtWidgets import QApplication

from src.age_calculator import AgeCalculator

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AgeCalculator()
    window.show()
    sys.exit(app.exec())
