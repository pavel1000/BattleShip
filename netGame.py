import field
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

from game import game_field


class net_game_field(game_field):

    def __init__(self, fields, connect, turn):
        super().__init__(fields)
        self.connect = connect
        self.turns = turn
        self.ui.labelTurn.setAlignment(Qt.AlignCenter)
        # print('Поле противника')
        # fields['enemy'].prints()
        self.fields['enemy'].clear()

    def update_label(self):
        if self.turns[0] is True:
            self.ui.labelTurn.setText(f"Ваш ход")
        else:
            self.ui.labelTurn.setText(f"Ждите хода")

    def positioning(self):
        super().positioning()
        x = self.width() // 2 - self.ui.labelTurn.width() // 2
        y = self.height() // 11 - self.ui.labelTurn.height() // 2
        self.ui.labelTurn.setGeometry(x, y, self.ui.labelTurn.width(), self.ui.labelTurn.height())

    def paintEvent(self, event):
        # Заменил showEvent на paintEvent, может будет меньше багов с отображением хода?
        # Нужно будет проверить работает ли resizeSygnal
        self.flagTurn = False
        self.timerLabel = QTimer()
        self.timerLabel.timeout.connect(lambda: self.update_label())
        self.timerLabel.start(10)
        self.timerTurn = QTimer()
        self.timerTurn.timeout.connect(
            lambda: self.enemyTurn("enemy", 'username'))
        self.timerTurn.start(1000)
        return super().paintEvent(event)

    def mousePressEvent(self, event):
        # print("Чей ход?")
        print(self.turns)

        if event.button() == Qt.LeftButton and self.turns[0] is True:
            self.__mousePressPos = event.globalPos()
            click = event.pos() - self.ui.field.pos()
            x = click.x()
            y = click.y()
            print(str(x) + "  " + str(y))
            cell = self.findCellByIndex(self.cells, x, y)
            if cell is None:
                return
            size = self.cells[0].width()
            pos = cell.pos()
            x, y = pos.x() // size, pos.y() // size
            if self.shots['username'].isHitted(y, x) is True:
                return
            self.shots['username'].IndicateCell(y, x)
            shot = str(y) + "," + str(x)
            self.connect[0].sendall(shot.encode())
            print("Точка " + shot)

            while True:
                data = self.connect[0].recv(1024)
                if data.decode() == "0":
                    print("ПОПАЛ!!!!!!!!!!!!!")
                    hitted = True
                    break
                elif data.decode() == "1":
                    print("НЕ ПОПАЛ!!!!!!!!!!!")
                    hitted = False
                    break

            if hitted is True:
                # print("Где проблема, если попал?")
                cell.setPixmap(QPixmap(':/images/square_purple.png'))
                #_, shooted = self.fields['enemy'].GetStrickenShips(y, x, self.shots['username'])
                #for s in shooted:
                #    self.cells[s[0]*10+s[1]].setPixmap(QPixmap(':/images/cross_gradient.png'))
                # отмечаем ячейки, в которые можно не стрелять
                livingShips = self.fields['username'].GetAvailableShips(
                    self.shots['username'])
                print("ВСЕГО ОСТАЛОСЬ " + str(livingShips) + " КОРАБЛЕЙ!")
                if livingShips == field.Ships(0, 0, 0, 0):
                    self.connect[0].sendall("win".encode())
                    QMessageBox.about(self, 'The end', "You ПРОИГРАЛ")
                    self.turns[0] = False
                    self.close()
                    self.closed.emit()
            else:
                # print("Где проблема, если НЕ попал?")
                cell.setPixmap(QPixmap(':/images/cross_gradient.png'))
                # отмечаем ячейку
                self.turns[0] = False
                self.connect[0].sendall("turn".encode())
        elif self.turns[0] is False:
            self.timerTurn.stop()
            self.enemyTurn("enemy", 'username')
        super().mousePressEvent(event)

    def enemyTurn(self, username, enemy):
        self.timerTurn.stop()
        while not self.turns[0]:
            self.update_label()
            print("Прошли while not self.turns[0]:")
            data = self.connect[0].recv(1024)
            data = data.decode()
            if data != "":
                print("Первое пришло (ход, победа или выстрел): " + data)
                if data == "turn":
                    # Ход меяется
                    self.turns[0] = True
                    self.timerTurn.start()
                    return
                elif data == "win":
                    # Ты выиграл, соперник проиграл
                    QMessageBox.about(self, 'The end', "Ты победил!")
                    self.closed.emit()
                    self.close()
                    return
                else:
                    shot_coords = str(data).split(',')
                    x, y = int(shot_coords[1]), int(shot_coords[0])
                    self.shots[username].IndicateCell(y, x)
                    size = self.cells_2[0].width()
                    x, y = x * size + size // 2, y * size + size // 2
                    cell = self.findCellByIndex(self.cells_2, x, y)
                    if cell is None:
                        print(
                            'Боту не удалось найти ячейку для выстрела ' + str(x) + ' ' + str(y))
                        print('Останавка игры...')
                        # self.turn[enemy] = False
                        # self.turn[username] = False
                        return
                    x, y = cell.pos().x() // size, cell.pos().y() // size
                    print(str(x) + " " + str(y))

                    hitted, shooted = self.fields[enemy].GetStrickenShips(
                        y, x, self.shots[username])
                    if hitted is True:
                        print("ПОПАЛCЯ!!!!!!!!!!!!!")
                        cell.setPixmap(QPixmap(':/images/square_purple.png'))
                        # отмечаем ячейки, в которые можно не стрелять
                        for s in shooted:
                            self.cells_2[s[0]*10+s[1]].setPixmap(QPixmap(':/images/cross_gradient.png'))
                        self.connect[0].sendall("0".encode())
                        self.turns[0] = False
                        livingShips = self.fields[enemy].GetAvailableShips(
                            self.shots[username])
                        if livingShips == field.Ships(0, 0, 0, 0):
                            print("Победил " + username)
                            QMessageBox.about(
                                self, 'The end', "Победил " + username)
                            self.turns[0] = False
                            self.connect[0].sendall("0".encode())
                            self.closed.emit()
                            self.close()
                        self.timerTurn.start()
                        return
                    else:
                        cell.setPixmap(QPixmap(':/images/cross_gradient.png'))
                        self.connect[0].sendall("1".encode())
                        self.turns[0] = True
        self.timerTurn.start()
