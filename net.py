from view.net import Ui_Form

import random

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSignal


class net_window(QWidget):
    
    nextNetWin = pyqtSignal()
    nextNetServerWin = pyqtSignal()
    
    def __init__(self):
        super(net_window, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ip = [""]
        self.ui.pushButton.clicked.connect(self.nextNetWindow)
        self.ui.pushButton_2.clicked.connect(self.nextNetServerWindow)

    def nextNetWindow(self):
        print("Ожидайте подключения")
        self.nextNetWin.emit()
        print("Ожидайте подключения")
        self.close()
    
    def nextNetServerWindow(self):
        self.ip[0] = self.ui.lineEdit.text()
        print("Ожидайте подключения")
        print(self.ip)
        self.nextNetServerWin.emit()
        self.close()

    def positioning(self):
       """ x = self.width()//2 - self.ui.newSoloGame.width()//2
        y = self.height()//2 - self.ui.newSoloGame.height()//2
        self.ui.newSoloGame.setGeometry(x, y, self.ui.newSoloGame.width(), self.ui.newSoloGame.height())
        self.ui.newNetGame.setGeometry(x+100, y, self.ui.newNetGame.width(), self.ui.newNetGame.height())"""

    def resizeEvent(self, event):
        '''Подгоняет размер элементов под размер экрана.'''
        self.positioning()
        #return super(startWindow, self).resizeEvent(event)
