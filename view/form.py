# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(960, 540)
        Form.setMinimumSize(QtCore.QSize(900, 500))
        self.newSoloGame = QtWidgets.QPushButton(Form)
        self.newSoloGame.setGeometry(QtCore.QRect(170, 130, 211, 211))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.newSoloGame.setFont(font)
        self.newSoloGame.setStyleSheet("background-color: #4CAF50;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    margin: 4px 2px;\n"
"border-radius: 100%;")
        self.newSoloGame.setObjectName("newSoloGame")
        self.newNetGame = QtWidgets.QPushButton(Form)
        self.newNetGame.setGeometry(QtCore.QRect(570, 130, 211, 211))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.newNetGame.setFont(font)
        self.newNetGame.setStyleSheet("background-color: #4CAF50;\n"
"    border: none;\n"
"    color: white;\n"
"    padding: 20px;\n"
"    text-align: center;\n"
"    text-decoration: none;\n"
"    display: inline-block;\n"
"    margin: 4px 2px;\n"
"border-radius: 100%;")
        self.newNetGame.setObjectName("newNetGame")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.newSoloGame.setText(_translate("Form", "Начать игру"))
        self.newNetGame.setText(_translate("Form", "Сетевая"))

