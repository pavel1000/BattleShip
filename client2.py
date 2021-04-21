# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 13:16:18 2021

@author: Solust
"""
import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('192.168.0.170', 9090)
print('Старт сервера на {} порт {}'.format(*server_address))
sock.bind(server_address)

# Слушаем входящие подключения
sock.listen(1)
while True:
    # ждем соединения
    print('Ожидание соединения...')
    connection, client_address = sock.accept()
    print(client_address[0])
    try:
        print('Подключено к:', client_address)
        # Принимаем данные порциями и ретранслируем их
        while True:
            data = connection.recv(1024)
            print(f'Получено: {data.decode()}')
            if data:
                print('Обработка данных...')
                text = str(input())
                print('Отправка обратно клиенту.')
                connection.sendall(text.encode())
            else:
                print('Нет данных от:', client_address)
                break

    finally:
        # Очищаем соединение
        connection.close()
