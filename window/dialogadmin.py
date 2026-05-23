from PyQt6.QtWidgets import QDialog, QFileDialog

from py_ui.dialogadmin import Ui_Dialog


class AdminDialog(QDialog,Ui_Dialog):
    def __init__(self,product: dict | None = None):
        super().__init__()
        self.product = product
        self.setupUi(self)
        self.load_product()
        self.pushButton_load.clicked.connect(self.image_path)
        self.pushButton_save.clicked.connect(self.accept)

    def load_product(self):
        if self.product is None:
            return
        self.descroptionLineEdit.setText(self.product["description"])
        self.priceLineEdit.setText(str(self.product["price"]))
        self.quantityLineEdit.setText(str(self.product["quantity"]))
        self.imageLineEdit.setText(self.product["image"])

    def get_order(self):
        description = self.descroptionLineEdit.text()
        price = self.priceLineEdit.text()
        quantity = self.quantityLineEdit.text()
        image = self.imageLineEdit.text()
        return description, price,quantity,image

    def image_path(self):
        path, _ = QFileDialog.getOpenFileName(self,"Выберите фото","image/","All Files(*)")
        if path:
            self.imageLineEdit.setText(path.split("/")[-1])






