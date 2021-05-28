from placement import ship_placement
from game import game_field
from view.net import Ui_Dialog
import socket
import random

import sys
import field
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSignal


class net_window(QWidget):
    nextNetWin = pyqtSignal()
    nextNetServerWin = pyqtSignal()

    def __init__(self):
        super(net_window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ip = ""
        self.ui.pushButton.clicked.connect(self.nextNetWindow)
        self.ui.pushButton_2.clicked.connect(self.nextNetServerWindow)
    
    def net(self):
        ran = random.randint(0,100)
        if self.ip == "":
            while True:
                #Сервер
                print("NE AD")
                h_name = socket.gethostname()
                IP_addres = socket.gethostbyname(h_name)
                
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_address = (IP_addres, 9090)
                print('Старт сервера на {} порт {}'.format(*server_address))
                sock.bind(server_address)
                sock.listen(1)
                connection, client_address = sock.accept()
                while True:
                    connection.sendall("CONNECTION".encode())
                    data = connection.recv(1024)
                    if data.decode() == "CONNECTION":
                        while True:
                            connection.sendall(ran.encode())
                            data = connection.recv(1024)
                            if data.decode() > ran:
                                return connection, 0
                            elif data.decode() == ran:
                                return connection, 1
                            else:
                                return connection, 1

        else:
            while True:
                print("AD")
                #Клиент
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                server_address = (self.ip, 9090)
                print('Подключено к {} порт {}'.format(*server_address))
                sock.connect(server_address)
                while True:
                    sock.sendall("CONNECTION".encode())
                    data = sock.recv(1024)
                    if data.decode() == "CONNECTION":
                        while True:
                            sock.sendall(ran.encode())
                            data = sock.recv(1024)
                            if data.decode() > ran:
                                return sock, 0
                            elif data.decode() == ran:
                                return sock, 0
                            else:
                                return sock, 1
                        

    def nextNetWindow(self):
        print("Ожидайте подключения")
        self.connect , self.turn = self.net()
        self.close()
        self.nextNetWin.emit()
    
    def nextNetServerWindow(self):
        self.ip = self.ui.lineEdit.text()
        print("Ожидайте подключения")
        self.connect , self.turn = self.net()
        self.close()
        self.nextNetServerWin.emit()

    def positioning(self):
       """ x = self.width()//2 - self.ui.newSoloGame.width()//2
        y = self.height()//2 - self.ui.newSoloGame.height()//2
        self.ui.newSoloGame.setGeometry(x, y, self.ui.newSoloGame.width(), self.ui.newSoloGame.height())
        self.ui.newNetGame.setGeometry(x+100, y, self.ui.newNetGame.width(), self.ui.newNetGame.height())"""

    def resizeEvent(self, event):
        '''Подгоняет размер элементов под размер экрана.'''
        self.positioning()
        #return super(startWindow, self).resizeEvent(event)
