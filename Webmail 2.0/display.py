# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'display.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(730, 539)
        self.From = QtWidgets.QLabel(Form)
        self.From.setGeometry(QtCore.QRect(-1, 48, 731, 41))
        self.From.setStyleSheet("font-size:16pt;color:white;")
        self.From.setAlignment(QtCore.Qt.AlignCenter)
        self.From.setObjectName("From")
        self.subject = QtWidgets.QLabel(Form)
        self.subject.setGeometry(QtCore.QRect(0, 89, 731, 41))
        self.subject.setStyleSheet("font-size:16pt;color:white;")
        self.subject.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.subject.setObjectName("subject")
        self.read = QtWidgets.QTextBrowser(Form)
        self.read.setGeometry(QtCore.QRect(0, 130, 731, 411))
        self.read.setStyleSheet("QTextBrowser{background-color:rgba(255,255,255,0.6);color:black;}")
        self.read.setObjectName("read")
        self.read.setOpenExternalLinks(True)
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
        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(87, 115, 501, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.From.show()
        self.subject.show()
        self.read.show()
        self.line.show()
        self.line_2.show()
        self.line_3.show()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.From.setText(_translate("Form", "TextLabel"))
        self.subject.setText(_translate("Form", "TextLabel"))

