# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'com.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(680, 539)
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(87, 115, 501, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(87, 45, 501, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(87, 80, 501, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.msgTo = QtWidgets.QLineEdit(Form)
        self.msgTo.setGeometry(QtCore.QRect(0, 48, 681, 41))
        self.msgTo.setStyleSheet("background-color:rgba(255,255,255,0);color:white;font-size:16pt;border-radius:1px")
        self.msgTo.setAlignment(QtCore.Qt.AlignCenter)
        self.msgTo.setObjectName("msgTo")
        self.su = QtWidgets.QLineEdit(Form)
        self.su.setGeometry(QtCore.QRect(0, 89, 681, 41))
        self.su.setStyleSheet("background-color:rgba(255,255,255,0);color:white;font-size:16pt;border-radius:1px")
        self.su.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.su.setObjectName("su")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(0, 130, 681, 411))
        self.textEdit.setStyleSheet("background-color:rgba(255,255,255,0.6);color:black;font-size:14pt")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.line.show()
        self.line_2.show()
        self.line_3.show()
        self.msgTo.show()
        self.textEdit.show()
        self.su.show()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.msgTo.setPlaceholderText(_translate("Form", "To: Id separated by commas"))
        self.su.setPlaceholderText(_translate("Form", "Subject"))
        self.textEdit.setPlaceholderText(_translate("Form", "Message - You can type in Rich Text also using HTML"))

