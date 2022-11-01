# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(251, 199)
        Form.setStyleSheet("background-color: rgb(76, 76, 76);")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(40, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(166, 166, 166);\n""")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 90, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(9)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 140, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(9)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Авторизация"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Username..."))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password..."))
        self.pushButton.setText(_translate("Form", "Sign up"))
        self.pushButton_2.setText(_translate("Form", "Sign in"))
        self.label.setText(_translate("Form", "Авторизация"))
