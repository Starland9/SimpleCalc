from PyQt6.QtWidgets import QMainWindow, QPushButton

from ui.main_window import Ui_MainWindow


class CalculatorWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit.textChanged.connect(self.set_correction)

        self.btn_1.clicked.connect(lambda: self.btn_clicked(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.btn_clicked(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.btn_clicked(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.btn_clicked(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.btn_clicked(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.btn_clicked(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.btn_clicked(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.btn_clicked(self.btn_8.text()))
        self.btn_0.clicked.connect(lambda: self.btn_clicked(self.btn_0.text()))

        self.btn_plus.clicked.connect(lambda: self.btn_clicked(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.btn_clicked(self.btn_minus.text()))
        self.btn_cross.clicked.connect(lambda: self.btn_clicked(self.btn_cross.text()))
        self.btn_div.clicked.connect(lambda: self.btn_clicked(self.btn_div.text()))

        self.btn_equal.clicked.connect(lambda: self.set_correction())

        self.btn_exit.clicked.connect(lambda: self.close())

        #
        # for child in self.centralwidget.children():
        #     if child.__class__.__name__ == 'QPushButton':
        #         child.clicked.connect(lambda: self.btn_clicked(child.objectName()))

    def btn_clicked(self, value):
        self.lineEdit.setText(self.lineEdit.text() + value)

    def set_correction(self):
        expression = self.lineEdit.text()
        if expression == '':
            self.lineEdit.setText('0')
            return
        try:
            self.lineEdit_2.setText(str(eval(self.lineEdit.text())))
        except Exception as e:
            print(e)
            self.lineEdit_2.setText(f'Error')
