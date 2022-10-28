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
        self.pushButton_exit.setGeometry(QtCore.QRect(260, 240, 81, 41))
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
        self.label_shifr = QtWidgets.QLabel(personal_win)
        self.label_shifr.setGeometry(QtCore.QRect(100, 99, 220, 21))
        self.label_shifr.setObjectName("label_shifr")
        self.label_rasshifr = QtWidgets.QLabel(personal_win)
        self.label_rasshifr.setGeometry(QtCore.QRect(100, 160, 220, 21))
        self.label_rasshifr.setObjectName("label_rasshifr")

        self.retranslateUi(personal_win)
        QtCore.QMetaObject.connectSlotsByName(personal_win)

    def retranslateUi(self, personal_win):
        _translate = QtCore.QCoreApplication.translate
        personal_win.setWindowTitle(_translate("personal_win", "Личный кабинет"))
        self.pushButton_exit.setText(_translate("personal_win", "Exit"))
        self.label.setText(_translate("personal_win", "Личный кабинет"))
        self.label_shifr.setText(_translate("personal_win", " "))
        self.label_rasshifr.setText(_translate("personal_win", " "))
