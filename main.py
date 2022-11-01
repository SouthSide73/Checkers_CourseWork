import sys
from PyQt5 import QtCore, QtWidgets
from des import Ui_Form
from personal import Ui_personal_win
from exit import Ui_Exit_Form
from cypher_wake import *
from textwrap import wrap


# Функция закрытия приложения
def exit_prog():
    global exit_prog
    exit_prog = QtWidgets.QDialog()
    ui = Ui_Exit_Form()
    ui.setupUi(exit_prog)
    personal_win.hide()
    exit_prog.show()

    def button_exit():
        exit_prog.close()

    def button_rest():
        exit_prog.hide()
        personal_win.show()

    ui.pushButton_exitprog.clicked.connect(button_exit)

    ui.pushButton_auth.clicked.connect(button_rest)


# Функция открытия личного кабинета
def openPersonalWin():
    global personal_win
    personal_win = QtWidgets.QDialog()
    ui = Ui_personal_win()
    ui.setupUi(personal_win)
    auth.hide()
    personal_win.show()

    # Функция вывода зашифрованного текста в файл
    def record():
        text = ui.lineEdit_3.text()
        text = text.replace(" ", "_")
        text = wrap(text, 10)
        for i in range(len(text)):
            text[i] = str_xor(text[i], key)
        text = "".join(text)
        with open('users_data.txt', 'r+', -1, 'utf-8') as file:
            file.write(text)
            ui.label_doshifr.setText("")
        file.close()

    # Функция вывода расшифрованного текста в форму
    def derivation():
        with open('users_data.txt', 'r+', -1, 'utf-8') as file:
            text = file.readlines()[0]
            text = wrap(text, 10)
            for i in range(len(text)):
                text[i] = str_xor(text[i], key)
            text = "".join(text)
            text = text.replace("_", " ")
            ui.label_doshifr.setText(text)
            file.truncate()
        file.close()

    ui.pushButton_exit.clicked.connect(exit_prog)

    ui.pushButton_obrabot.clicked.connect(record)

    ui.pushButton_obrabot2.clicked.connect(derivation)


# Функция входа
def login(username, password, signal):
    global user_data
    with open('users.txt', 'r+') as file:
        flag = False
        for line in file:
            line = line.split('<-[Username]---[Password]->')
            line[1] = line[1][:len(line[1])-1]
            if line[0] == str_xor(username, key) and line[1] == str_xor(password, key):
                flag = True
                user_data = r"data_D.txt"
                user_data = user_data.replace('D', username)
                openPersonalWin()
        if not flag:
            signal.emit('Проверьте правильность ввода данных!')
    file.close()


# Функция регистрации
def register(username, password, signal):
    flag2 = False
    with open('users.txt', 'r+') as file:
        for line in file:
            line = line.split('<-[Username]---[Password]->')
            line[1] = line[1][:len(line[1]) - 1]
            if line[0] == str_xor(username, key):
                flag2 = True
                signal.emit('Такой ник уже используется!')
        if username == '' or password == '':
            flag2 = True
            signal.emit('Не оставляйте поля пустыми!')
        elif len(username) > 10 or len(password) > 10 and len(username) < 2 or len(password) < 2:
            flag2 = True
            signal.emit('Username и password не могут быть больше 10 и меньше 2 символов!')
        if not flag2:
            file.write(str_xor(username, key))
            file.write('<-[Username]---[Password]->')
            file.write(str_xor(password, key))
            file.write('\n')
            signal.emit('Вы успешно зарегистрированы!')
    file.close()


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
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        self.check_db.thr_login(username, password)

    def reg(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        self.check_db.thr_register(username, password)


# Открытие окна авторизации
app = QtWidgets.QApplication(sys.argv)
auth = Interface()
auth.show()
app.exec()
