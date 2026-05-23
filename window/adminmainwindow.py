from PyQt6.QtWidgets import QWidget, QDialog, QMessageBox

from database.db import dao
from py_ui.mainadmin import Ui_Form
from window.cardwindow import CardWindow
from window.dialogadmin import AdminDialog


class AdminMainWindow(QWidget,Ui_Form):
    def __init__(self,account = None):
        super().__init__()
        self.account = account
        self.dialog = AdminDialog()
        self.selected = None
        self.setupUi(self)
        self.widget_product()
        self.pushButton_add.clicked.connect(self.add_product)
        self.pushButton_del.clicked.connect(self.del_product)
        self.pushButton_edit.clicked.connect(self.edit_product)

        if self.account["role_id"] == 2:
            self.pushButton_del.setVisible(False)


    def widget_product(self):
        while self.verticalLayout_3.count():
            widget = self.verticalLayout_3.takeAt(0).widget()
            if widget is not None:
                widget.deleteLater()
        items = dao.all_product()
        for item in items:
            widget = CardWindow(item)
            widget.clicked.connect(self.set_selected)
            self.verticalLayout_3.addWidget(widget)

    def set_selected(self, product):
        self.selected = product

    def add_product(self):
        if self.dialog.exec() == QDialog.DialogCode.Accepted:
            description,price,quantity,image = self.dialog.get_order()
            dao.add_product_bd(description,price,quantity,image)
            self.widget_product()

    def del_product(self):
        if self.selected is None:
            QMessageBox.critical(self,"Ошибка","Выберите товар")
        else:
            dao.delete_product(self.selected["id"])
            self.widget_product()
            QMessageBox.information(self,"Отлично","Вы успешно удалили товар")

    def edit_product(self):
        if self.selected is None:
            QMessageBox.critical(self,"Ошибка","Выберите товар")
            return
        dialog = AdminDialog(self.selected)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            description,price,quantity,image = dialog.get_order()
            dao.update_product(self.selected["id"],description,price,quantity,image)
            self.widget_product()

