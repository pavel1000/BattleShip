# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 20:49:22 2021

@author: Solust
"""
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QVBoxLayout
import sys
import socket
import threading


class SocketStream(threading.Thread):
    def socket_stream(self, plainText):
        while True:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = ('192.168.0.170', 9090)
            print('Подключено к {} порт {}'.format(*server_address))
            sock.connect(server_address)
            text = str(input())
            message = text.encode()
            sock.sendall(message)
            '''amount_received = 0
            amount_expected = len(message)
            while amount_received < amount_expected:'''

            data = sock.recv(1024)
            #amount_received += len(data)
            mess = data.decode()
            print(f'Получено: {data.decode()}')
            plainText.setPlaceholderText(mess)
            plainText.setReadOnly(True)
            text = "Please subscribe the channel and like the videos"
            plainText.appendPlainText(mess)

# Тут продолжить
# def OnReceive


if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')

    vbox = QVBoxLayout()
    plainText = QPlainTextEdit()
    Stream = SocketStream()
    Stream.socket_stream(plainText)
    plainText.setUndoRedoEnabled(False)

    vbox.addWidget(plainText)

    w.setLayout(vbox)
    w.show()

    sys.exit(app.exec_())
