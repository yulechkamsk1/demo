from PyQt6.QtWidgets import QWidget, QMessageBox, QDialog

from database.db import dao
from py_ui.mainclient import Ui_Form
from window.cardwindow import CardWindow
from window.dialogwindow import DialogWindow


class MainWindow(QWidget,Ui_Form):
    def __init__(self, account=None):
        super().__init__()
        self.account = account
        self.selected = None
        self.total = 0
        self.setupUi(self)
        self.widget_product()
        self.pushButton.clicked.connect(self.get_order)
        if self.account is None:
            self.tabWidget.setTabVisible(1,False)

    def widget_product(self):
        while self.verticalLayout_4.count():
            widget = self.verticalLayout_4.takeAt(0).widget()
            if widget is not None:
                widget.deleteLater()
        items = dao.all_product()
        for item in items:
            widget = CardWindow(item)
            widget.clicked.connect(self.click_product)
            self.verticalLayout_4.addWidget(widget)

    def click_product(self,product):
        self.selected = product
        widget = CardWindow(product)
        self.verticalLayout_8.addWidget(widget)
        QMessageBox.information(self,"Успех","Ваш товар добавлен в корзину")
        self.total += product["price"]

    def get_order(self):
        if self.selected is None:
            return
        dialog = DialogWindow()
        result = dialog.exec()

        if result == QDialog.DialogCode.Accepted:
            name, address, quantity = dialog.get_order()
            total = quantity * self.total
            QMessageBox.information(self,"Успех",f"Ваш заказ оформлен на сумму {total}")
