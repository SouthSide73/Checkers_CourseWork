# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personal_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_personal_win(object):
    def setupUi(self, personal_win):
        personal_win.setObjectName("personal_win")
        personal_win.resize(411, 324)
        personal_win.setStyleSheet("background-color: rgb(118, 118, 118);")
        self.pushButton_exit = QtWidgets.QPushButton(personal_win)
        self.pushButton_exit.setGeometry(QtCore.QRect(300, 260, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(14)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setStyleSheet("background-color: rgb(202, 202, 202);")
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.label = QtWidgets.QLabel(personal_win)
        self.label.setGeometry(QtCore.QRect(130, 20, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_doshifr = QtWidgets.QLabel(personal_win)
        self.label_doshifr.setGeometry(QtCore.QRect(60, 160, 171, 21))
        self.label_doshifr.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.label_doshifr.setObjectName("label_doshifr")
        self.lineEdit_3 = QtWidgets.QLineEdit(personal_win)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 100, 171, 21))
        self.lineEdit_3.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.lineEdit_3.setObjectName("lineEdit")
        self.pushButton_obrabot = QtWidgets.QPushButton(personal_win)
        self.pushButton_obrabot.setGeometry(QtCore.QRect(240, 100, 75, 23))
        self.pushButton_obrabot.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.pushButton_obrabot.setObjectName("pushButton_obrabot")
        self.pushButton_obrabot2 = QtWidgets.QPushButton(personal_win)
        self.pushButton_obrabot2.setGeometry(QtCore.QRect(240, 160, 75, 23))
        self.pushButton_obrabot2.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.pushButton_obrabot2.setObjectName("pushButton_obrabot2")

        self.retranslateUi(personal_win)
        QtCore.QMetaObject.connectSlotsByName(personal_win)

    def retranslateUi(self, personal_win):
        _translate = QtCore.QCoreApplication.translate
        personal_win.setWindowTitle(_translate("personal_win", "Личный кабинет"))
        self.pushButton_exit.setText(_translate("personal_win", "Exit"))
        self.label.setText(_translate("personal_win", "Личный кабинет"))
        self.label_doshifr.setText(_translate("personal_win", ""))
        self.lineEdit_3.setPlaceholderText(_translate("personal_win", "Введите текст..."))
        self.pushButton_obrabot.setText(_translate("personal_win", "Отправить"))
        self.pushButton_obrabot2.setText(_translate("personal_win", "Вывести"))
