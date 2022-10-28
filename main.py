import sys
from PyQt5 import QtCore, QtWidgets
from des import Ui_Form
from personal import Ui_personal_win
from exit import Ui_Exit_Form
import sqlite3
from cypher_wake import *


# Функция рестарта приложения
def restart():
    QtCore.QCoreApplication.quit()
    status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
    return status


# Функция закрытия приложения
def exit_prog():
    global exit_prog
    exit_prog = QtWidgets.QDialog()
    ui = Ui_Exit_Form()
    ui.setupUi(exit_prog)
    personal_win.close()
    exit_prog.show()

    def button_exit():
        exit_prog.close()

    ui.pushButton_exitprog.clicked.connect(button_exit)

    def button_auth():
        restart()

    ui.pushButton_auth.clicked.connect(button_auth)


# Функция открытия личного кабинета
def openPersonalWin(dec, enc):
    global personal_win
    personal_win = QtWidgets.QDialog()
    ui = Ui_personal_win()
    ui.setupUi(personal_win)
    ui.label_rasshifr.setText("Расшифрованный username:" + dec)
    ui.label_shifr.setText("Зашифрованный username:" + enc)
    auth.close()
    personal_win.show()
    ui.pushButton_exit.clicked.connect(exit_prog)


# Функция входа
def login(username, password, signal):
    con = sqlite3.connect('users')
    cur = con.cursor()
    cur.execute(f'SELECT * FROM users WHERE name="{str_xor(username, key)}";')
    value = cur.fetchall()
    if value != [] and value[0][2] == str_xor(password, key):
        openPersonalWin(dec=str_xor(str_xor(username, key), key), enc=str_xor(username, key))
    else:
        signal.emit('Проверьте правильность ввода данных!')
    cur.close()
    con.close()


# Функция регистрации
def register(username, password, signal):
    con = sqlite3.connect('users')
    cur = con.cursor()
    cur.execute(f'SELECT * FROM users WHERE name="{str_xor(username, key)}";')
    value = cur.fetchall()
    if value != []:
        signal.emit('Такой ник уже используется!')
    elif len(username) == 0 or len(password) == 0:
        signal.emit('Не оставляйте поля пустыми!')
    elif len(username) > 9 or len(password) > 9:
        signal.emit('Username и password не могут быть больше 9 символов!')
    elif value == []:
        cur.execute(f"INSERT INTO users (name, password) VALUES ('{str_xor(username, key)}', '{str_xor(password, key)}')")
        signal.emit('Вы успешно зарегистрированы!')
        con.commit()
    cur.close()
    con.close()


# Класс проверки
class CheckThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def thr_login(self, username, password):
        login(username, password, self.signal)

    def thr_register(self, username, password):
        register(username, password, self.signal)


# Класс окна авторизации
class Interface(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.reg)
        self.ui.pushButton_2.clicked.connect(self.auth)
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]
        self.check_db = CheckThread()
        self.check_db.signal.connect(self.warning)

    def warning(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def auth(self):
        name = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        self.check_db.thr_login(name, password)

    def reg(self):
        name = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        self.check_db.thr_register(name, password)


# Открытие окна
app = QtWidgets.QApplication(sys.argv)
auth = Interface()
auth.show()
app.exec()
