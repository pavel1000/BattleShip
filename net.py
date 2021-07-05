from view.net import Ui_Form

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSignal, QRect


class net_window(QWidget):
    nextNetWin = pyqtSignal()
    nextNetServerWin = pyqtSignal()
    back = pyqtSignal()
    resizeSygnal = pyqtSignal(QRect)

    def __init__(self):
        super(net_window, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ip = [""]
        self.ui.pushButton.clicked.connect(self.nextNetWindow)
        self.ui.pushButton_2.clicked.connect(self.nextNetServerWindow)
        self.ui.pushButton_3.clicked.connect(self.closeWin)

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

    def closeWin(self):
        self.back.emit()
        self.close()

    def positioning(self):
        widthBtn = self.ui.pushButton_2.width()//2
        x = self.width()//4
        y = self.height()*3//5 - self.ui.pushButton_2.height()//2
        self.ui.pushButton_3.setGeometry(x-widthBtn, y, self.ui.pushButton_2.width(), self.ui.pushButton_2.height())
        self.ui.pushButton.setGeometry(2*x-widthBtn, y, self.ui.pushButton_2.width(), self.ui.pushButton_2.height())
        self.ui.pushButton_2.setGeometry(3*x-widthBtn , y, self.ui.pushButton_2.width(), self.ui.pushButton_2.height())

    def resizeEvent(self, event):
        '''Подгоняет размер элементов под размер экрана.'''
        self.positioning()
        return super().resizeEvent(event)

    def paintEvent(self, event):
        self.resizeSygnal.emit(self.geometry())
        return super().paintEvent(event)
