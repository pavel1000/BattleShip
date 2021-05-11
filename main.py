from placement import ship_placement
from view.form import Ui_Form

import sys
import field
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSignal
from game import game_field

'''
def playerTurn(username, enemy):
    print(username)
    print("Выберите точку удара: ")
    shots[username].prints()
    msg = input().split(" ")
    shots[username].IndicateCell(int(msg[0]), int(msg[1]))
    strickenShips = fields[enemy].GetStrickenShips(msg, shots[username])
    # print("Ваше поле")
    # fields[username].prints()
    print("Поле соперника")
    shots[username].prints()
    if strickenShips.Hitted != "":
        availableShips = fields[enemy].GetAvailableShips(shots[username])
        print(availableShips)
        turn[enemy] = False
        turn[username] = True
        if availableShips == field.Ships(0, 0, 0, 0):
            print("Победил "+username)
            return False
    else:
        turn[enemy] = True
        turn[username] = False
        print("Промазал")
    print()
    return True


def Game():
    username = "username"
    RandomFieldFilling(username)
    enemy = "enemy"
    RandomFieldFilling(enemy)
    stillPlaying = True
    print("Поле игрока")
    fields[username].prints()
    print("Поле соперника")
    fields[enemy].prints()

    # Записали попадание в shots, после получили структуру
    # сбитых и прилежащих к сбитым ячеек, отправили ее для рендера
    # у себя, изменили ее для последующего рендера у 2-ого игрока
    # и записали эти изменения на его имя
    while stillPlaying is True:
        if turn[enemy] is True:
            stillPlaying = playerTurn(enemy, username)
        else:
            stillPlaying = playerTurn(username, enemy)
'''


class MainApp(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        self.start = startWindow()
        self.start.show()

        self.placement = ship_placement()
        self.game = game_field(self.placement.fields)

        self.placement.closed.connect(self.start.show)
        self.game.closed.connect(self.start.show)
        self.game.closed.connect(self.newGameChanges)
        self.start.nextWin.connect(self.placement.show)
        self.placement.nextWin.connect(self.game.show)

    def newGameChanges(self):
        self.placement.returnShips()
        self.game.resetFields()


class startWindow(QWidget):
    nextWin = pyqtSignal()

    def __init__(self):
        super(startWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.nextWindow)

    def nextWindow(self):
        self.close()
        self.nextWin.emit()

    def positioning(self):
        x = self.width()//2 - self.ui.pushButton.width()//2
        y = self.height()//2 - self.ui.pushButton.height()//2
        self.ui.pushButton.setGeometry(x, y, self.ui.pushButton.width(), self.ui.pushButton.height())

    def resizeEvent(self, event):
        '''Подгоняет размер элементов под размер экрана.'''
        self.positioning()
        return super(startWindow, self).resizeEvent(event)


if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())
