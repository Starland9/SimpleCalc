from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMainWindow

from ui import convertor
from utils import convertor_utils as utils


# noinspection PyUnresolvedReferences
class Convertor(QMainWindow, convertor.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.toItem = None
        self.fromItem = None
        self.setupUi(self)
        self.currentCategory = None
        self.categories = utils.categories
        self.menuActions = []

        for c in self.categories:
            action = QAction(c.name)
            action.triggered.connect(lambda: self.set_category(c))
            self.menuActions.append(action)

        self.menuCategory.addActions(self.menuActions)

        self.comboBoxFrom.currentIndexChanged.connect(self.from_changed)
        self.comboBoxTo.currentIndexChanged.connect(self.to_changed)
        self.lineEditFrom.textEdited.connect(self.convert)

        self.set_category(self.categories[0])

    def set_category(self, category: utils.ConvertorCategory):
        self.currentCategory = category
        self.fill_combos()

    def fill_combos(self):
        self.comboBoxTo.clear()
        self.comboBoxFrom.clear()
        self.comboBoxFrom.addItems([i.name for i in self.currentCategory.items])
        self.comboBoxTo.addItems([i.name for i in self.currentCategory.items])

    def from_changed(self, i):
        self.currentCategory.selectedFrom = self.currentCategory.items[i]
        self.convert()

    def to_changed(self, i):
        self.currentCategory.selectedTo = self.currentCategory.items[i]
        self.convert()

    def convert(self):
        try:
            conversion = self.currentCategory.get_conversion(float(self.lineEditFrom.text()))
            self.lineEditTo.setText(str(conversion))
        except ValueError:
            self.lineEditFrom.setText('')
            self.lineEditTo.setText(str(0))
