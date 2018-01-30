# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'webmail.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(890, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("mail-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.back = QtWidgets.QLabel(Form)
        self.back.setGeometry(QtCore.QRect(0, 0, 890, 600))
        self.back.setText("")
        self.back.setPixmap(QtGui.QPixmap("back1.jpg"))
        self.back.setScaledContents(True)
        self.back.setObjectName("back")
        self.Icon = QtWidgets.QLabel(Form)
        self.Icon.setGeometry(QtCore.QRect(330, 90, 140, 120))
        self.Icon.setText("")
        self.Icon.setPixmap(QtGui.QPixmap("mail-icon.png"))
        self.Icon.setScaledContents(True)
        self.Icon.setObjectName("Icon")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(302, 210, 201, 71))
        self.label.setStyleSheet("color:white;font-size:40pt;")
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(293, 340, 221, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(293, 320, 20, 20))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("user.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.user = QtWidgets.QLineEdit(Form)
        self.user.setGeometry(QtCore.QRect(326, 320, 181, 21))
        self.user.setStyleSheet("border-radius:1px;background-color:rgba(255,255,255,0);color:white;")
        self.user.setClearButtonEnabled(True)
        self.user.setObjectName("user")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(293, 390, 221, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pas = QtWidgets.QLineEdit(Form)
        self.pas.setGeometry(QtCore.QRect(326, 370, 181, 21))
        self.pas.setStyleSheet("border-radius:1px;background-color:rgba(255,255,255,0);color:white;")
        self.pas.setInputMask("")
        self.pas.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pas.setDragEnabled(False)
        self.pas.setClearButtonEnabled(True)
        self.pas.setObjectName("pas")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(293, 370, 20, 20))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("lock.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.lo = QtWidgets.QPushButton(Form)
        self.lo.setGeometry(QtCore.QRect(293, 440, 221, 41))
        self.lo.setObjectName("lo")

        self.rem = QCheckBox(Form)
        self.rem.setGeometry(350,410,121,20)
        self.rem.setStyleSheet('color:white')
        self.rem.setText("Remember Me")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PyWebmail"))
        self.label.setText(_translate("Form", "PyWebmail"))
        self.user.setPlaceholderText(_translate("Form", "Username"))
        self.pas.setPlaceholderText(_translate("Form", "Password"))
        self.lo.setText(_translate("Form", "Log in"))

