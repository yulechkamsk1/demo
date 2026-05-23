from PyQt6.QtWidgets import QDialog

from py_ui.dialog import Ui_Dialog


class DialogWindow(QDialog,Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.accept)


    def get_order(self):
        name = self.nameLineEdit.text()
        address = self.adressLineEdit.text()
        quantity = self.quantitySpinBox.value()
        return name, address,quantity





