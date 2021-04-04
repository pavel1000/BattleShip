# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 20:49:22 2021

@author: Solust
"""

from jnius import autoclass
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QVBoxLayout

BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
Intent = autoclass('android.content.Intent')
UUID = autoclass('java.util.UUID')

def get_socket_stream(name):
    paired_devices = BluetoothAdapter.getDefaultAdapter().startDiscovery()
    socket = None
    for device in paired_devices:
        if device.getName() == name:
            socket = device.createRfcommSocketToServiceRecord(
                UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
            recv_stream = socket.getInputStream()
            send_stream = socket.getOutputStream()
            break
    socket.connect()
    return recv_stream, send_stream

#Тут продолжить
#def OnReceive

if __name__ == '__main__':
    app = QApplication(sys.argv)
    recv_stream, send_stream = get_socket_stream('linvor')

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    
    vbox = QVBoxLayout()
    plainText = QPlainTextEdit()
    plainText.setPlaceholderText(send_stream)
    
    #plainText.setReadOnly(True)
    
    text = "Please subscribe the channel and like the videos"
    plainText.appendPlainText(text)
    plainText.setUndoRedoEnabled(False)
    
    vbox.addWidget(plainText)
    
    w.setLayout(vbox)
    w.show()
    

    sys.exit(app.exec_())