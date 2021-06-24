import field
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QPixmap

from game import RandomFieldFilling
from game import game_field
from view.game_field import Ui_Form

class net_game_field(game_field):

    def __init__(self, fields, connect, turn):
        self.transit()
        self.connect = connect
        self.fields = fields
        self.shots = {"username": field.Field(), "enemy": field.Field()}
        self.turns = turn
        print(self.turns)
        self.ui = Ui_Form()
        #self.update_label()
        self.ui.setupUi(self)
        RandomFieldFilling(self.fields['enemy'])
        # print('Поле противника')
        # fields['enemy'].prints()
        #self.update_label()
        self.UI()


    def update_label(self):
        if self.turns[0] is True :
            self.ui.label_201.setText(f"Ваш ход")
        else:
            self.ui.label_201.setText(f"Ждите хода")

    def mousePressEvent(self, event):
        print("Чей ход?")
        print(self.turns)
        QTimer.singleShot(1, self.update_label)

        if event.button() == Qt.LeftButton and self.turns[0] == 1:
            self.__mousePressPos = event.globalPos()
            click = event.pos() - self.ui.field.pos()
            x = click.x()
            y = click.y()
            print(str(x) + "  " + str(y))
            cell = self.findCellByIndex(self.cells, x, y)
            if cell is not None:
                size = self.cells[0].width()
                pos = cell.pos()
                x, y = pos.x() // size, pos.y() // size
                if self.shots['username'].isHitted(y, x) is False:
                    self.shots['username'].IndicateCell(y, x)
                    shot = str(y) + "," + str(x)
                    self.connect[0].sendall(shot.encode())
                    print("Точка " + shot)

                    while True:
                        data = self.connect[0].recv(1024)
                        if data.decode() == "0":
                            print("ПОПАЛ!!!!!!!!!!!!!")
                            hitted = True
                            break;
                        elif data.decode() == "1":
                            print("НЕ ПОПАЛ!!!!!!!!!!!")
                            hitted = False
                            self.ui.label_201.setText(f"Ждите хода")
                            break;

                    if hitted is True:
                        print("Где проблема, если попал?")
                        cell.setPixmap(QPixmap(':/images/shape.png'))
                        # отмечаем ячейки, в которые можно не стрелять
                        livingShips = self.fields['username'].GetAvailableShips(self.shots['username'])
                        print("ВСЕГО ОСТАЛОСЬ КОРАБЛЕЙ! = " + str(livingShips))
                        if livingShips == field.Ships(0, 0, 0, 0):
                            self.connect[0].sendall("win".encode())
                            QMessageBox.about(self, 'The end', "You ПРОИГРАЛ")
                            self.turns[0] = False
                            self.close()
                            self.closed.emit()
                    else:
                        cell.setPixmap(QPixmap(':/images/cross.png'))
                        self.turns[0] = False
                        self.turns[1] = True
                        self.connect[0].sendall("turn".encode())
        if self.turns[0] == 0:
            print("Ушли в приём")
            #self.ui.label_201
            self.enemyTurn("enemy", 'username')
            # Нужно, зачем не помню

        self.transit2(event)


    def enemyTurn(self, username, enemy):
        self.ui.label_201.setText(f"Ждите хода")
        while not self.turns[0]:
            print("Прошли while not self.turns[0]:")
            data = self.connect[0].recv(1024)
            data = data.decode()
            if data is not "":
                print("Первое пришло (ход, победа или выстрел): " + data)
                if data == "turn":
                    self.turns[0] = True
                    self.turns[1] = False

                    return
                    # Ход меяется
                elif data == "win":
                    QMessageBox.about(self, 'The end', "You Выиграл")
                    self.close()
                    self.closed.emit()
                    return
                    # Ты выиграл, соперник проиграл
                else:
                    strs = str(data).split(',')
                    x, y = int(strs[1]), int(strs[0])
                    self.shots[username].IndicateCell(y, x)
                    size = self.cells_2[0].width()
                    x, y = x * size + size // 2, y * size + size // 2
                    cell = self.findCellByIndex(self.cells_2, x, y)
                    if cell is None:
                        print('Боту не удалось найти ячейку для выстрела ' + str(x) + ' ' + str(y))
                        print('Останавка игры...')
                        # self.turn[enemy] = False
                        # self.turn[username] = False
                        return
                    x, y = cell.pos().x() // size, cell.pos().y() // size
                    print(str(x) + " " + str(y))

                    hitted, _ = self.fields[enemy].GetStrickenShips(y, x, self.shots[username])
                    if hitted is True:
                        print("ПОПАЛCЯ!!!!!!!!!!!!!")
                        cell.setPixmap(QPixmap(':/images/shape.png'))
                        # отмечаем ячейки, в которые можно не стрелять
                        self.connect[0].sendall("0".encode())
                        self.turns[0] = False
                        livingShips = self.fields[enemy].GetAvailableShips(self.shots[username])
                        if livingShips == field.Ships(0, 0, 0, 0):
                            print("Победил " + username)
                            QMessageBox.about(self, 'The end', "Победил " + username)
                            self.turns[0] = False
                            self.connect[0].sendall("0".encode())
                            self.close()
                            self.closed.emit()

                    else:
                        cell.setPixmap(QPixmap(':/images/cross.png'))
                        self.connect[0].sendall("1".encode())
                        self.turns[0] = True



