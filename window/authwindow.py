from database.db import dao
from py_ui.auth import Ui_Form
from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication

from window.adminmainwindow import AdminMainWindow
from window.mainwindow import MainWindow


class AuthWindow(QWidget,Ui_Form):
    def __init__(self, account=None):
        super().__init__()
        self.window = None
        self.account = account
        self.setupUi(self)
        self.pushButton_user.clicked.connect(self.login_user)
        self.pushButton_guest.clicked.connect(self.guest_login)





    def login_user(self):
        login = self.lineEdit_login.text()
        password = self.lineEdit_pass.text()
        account = dao.login_user(login,password)

        if not account:
            QMessageBox.information(self,"Ошибка","Такого аккаунта не существует")
            return

        type_account: int = account["role_id"]
        if type_account == 1:
            self.window = MainWindow(account)
            self.window.show()
            self.close()
        elif type_account == 3:
            self.window = AdminMainWindow(account)
            self.window.show()
            self.close()
        elif type_account == 2:
            self.window = AdminMainWindow(account)
            self.window.show()
            self.close()

    def guest_login(self):
        self.window = MainWindow()
        self.window.show()
        self.close()


app = QApplication([])
window = AuthWindow()
window.show()
app.exec()
