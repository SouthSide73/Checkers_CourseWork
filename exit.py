# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exit.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Exit_Form(object):
    def setupUi(self, Exit_Form):
        Exit_Form.setObjectName("Exit_Form")
        Exit_Form.resize(400, 176)
        Exit_Form.setStyleSheet("background-color: rgb(141, 141, 141);")
        self.label = QtWidgets.QLabel(Exit_Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_exitprog = QtWidgets.QPushButton(Exit_Form)
        self.pushButton_exitprog.setGeometry(QtCore.QRect(230, 110, 101, 31))
        self.pushButton_exitprog.setStyleSheet("background-color: rgb(177, 177, 177);")
        self.pushButton_exitprog.setObjectName("pushButton_exitprog")
        self.pushButton_auth = QtWidgets.QPushButton(Exit_Form)
        self.pushButton_auth.setGeometry(QtCore.QRect(60, 110, 101, 31))
        self.pushButton_auth.setStyleSheet("background-color: rgb(177, 177, 177);")
        self.pushButton_auth.setObjectName("pushButton_auth")

        self.retranslateUi(Exit_Form)
        QtCore.QMetaObject.connectSlotsByName(Exit_Form)

    def retranslateUi(self, Exit_Form):
        _translate = QtCore.QCoreApplication.translate
        Exit_Form.setWindowTitle(_translate("Exit_Form", "Выход"))
        self.label.setText(_translate("Exit_Form", "Вы точно желаете выйти из приложения?"))
        self.pushButton_exitprog.setText(_translate("Exit_Form", "Выйти"))
        self.pushButton_auth.setText(_translate("Exit_Form", "Вход"))
