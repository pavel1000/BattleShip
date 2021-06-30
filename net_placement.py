import random
import socket
import field

from placement import ship_placement
from view.ship_placement7 import Ui_Form


class net_ship_placement(ship_placement):

    def __init__(self, typeGame, ip):
        self.transit()
        self.type = typeGame
        self.ip = ip
        self.connect = [""]
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.fields = {"username": field.Field(), "enemy": field.Field()}
        self.turn = [False for _ in range(2)]
        self.UI()

    def initTurn(self, turn):
        if turn == 1:
            self.turn[0] = True
            self.turn[1] = False
        else:
            self.turn[0] = False
            self.turn[1] = True
        self.show()

    def net(self):
        ran = str(random.randint(0, 100))
        print("А что тут?")
        print(self.ip)
        print("А что тут?")
        if self.ip[0] == "":
            # Сервер
            print("NE AD")
            h_name = socket.gethostname()
            # работает нормально ели отключить внутриний Ethernet
            IP_addres = socket.gethostbyname(h_name)

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = (IP_addres, 9090)
            print('Старт сервера на {} порт {}'.format(*server_address))
            sock.bind(server_address)
            sock.listen(1)
            connection, client_address = sock.accept()
            while True:
                print("11")
                connection.sendall("CONNECTION".encode())
                data = connection.recv(1024)
                if data.decode() == "CONNECTION":
                    while True:
                        print("22")
                        connection.sendall(ran.encode())
                        data = connection.recv(1024)

                        if self.is_number(data.decode()):
                            if data.decode() > ran:
                                self.connect[0] = connection
                                self.turn[0] = False
                                return connection, 0
                            elif data.decode() == ran:
                                print("Ваш ход")
                                self.connect[0] = connection
                                self.turn[0] = True
                                return connection, 1
                            else:
                                print("Ваш ход")
                                self.connect[0] = connection
                                self.turn[0] = True

                                return connection, 1

        else:
            print("AD")
            # Клиент
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # print(self.ip[0])
            server_address = (self.ip[0], 9090)
            print('Подключено к {} порт {}'.format(*server_address))
            sock.connect(server_address)
            while True:
                print("11")
                sock.sendall("CONNECTION".encode())
                data = sock.recv(1024)
                if data.decode() == "CONNECTION":
                    while True:
                        print("22")
                        sock.sendall(ran.encode())
                        data = sock.recv(1024)
                        if self.is_number(data.decode()):
                            if data.decode() > ran:
                                self.connect[0] = sock
                                self.turn[0] = False

                                return sock, 0
                            elif data.decode() == ran:
                                self.connect[0] = sock
                                self.turn[0] = False

                                return sock, 0
                            else:
                                print("Ваш ход")
                                self.connect[0] = sock
                                self.turn[0] = True

                                return sock, 1

    def is_number(self, str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    def loadGame(self):
        self.initField()
        if self.fields['username'].CheckPositionOfShips() is True:
            print('Корабли расставлены верно')
            self.net()
            self.nextWin.emit()
            self.close()
        else:
            print('Корабли расставлены НЕ верно')
            self.ui.start_button.setDisabled(True)
