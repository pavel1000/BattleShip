from placement import ship_placement
from game import game_field
from view.form import Ui_Form
from net import net_window
from netGame import net_game_field
from net_placement import net_ship_placement

import sys
import field
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSignal

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
        self.net = net_window()
        self.net_game = net_game_field(self.placement.fields,self.net.connect, self.net.turn)

        self.placement.closed.connect(self.start.show)
        self.game.closed.connect(self.start.show)
        self.game.closed.connect(self.newGameChanges)
        
        self.start.nextNetWin.connect(self.net.show)
        self.net.nextNetWin.connect(self.placement.show)
        self.net.nextNetServerWin.connect(self.placement.show)
        self.placement.nextNetWin.connect(self.net_game.show)
        
        self.start.nextWin.connect(self.placement.show)
        self.placement.nextWin.connect(self.game.show)

    def newGameChanges(self):
        self.placement.returnShips()
        self.game.resetFields()


class startWindow(QWidget):
    nextWin = pyqtSignal()
    nextNetWin = pyqtSignal()

    def __init__(self):
        super(startWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.newSoloGame.clicked.connect(self.nextWindow)
        self.ui.newNetGame.clicked.connect(self.nextNetWin)
    

    def nextWindow(self):
        self.close()
        self.nextWin.emit()
    
    def nextNetWindow(self):
        self.close()
        self.nextNetWin().emit()

    def positioning(self):
        x = self.width()//2 - self.ui.newSoloGame.width()//2
        y = self.height()//2 - self.ui.newSoloGame.height()//2
        self.ui.newSoloGame.setGeometry(x-120, y, self.ui.newSoloGame.width(), self.ui.newSoloGame.height())
        self.ui.newNetGame.setGeometry(x+120, y, self.ui.newNetGame.width(), self.ui.newNetGame.height())

    def resizeEvent(self, event):
        '''Подгоняет размер элементов под размер экрана.'''
        self.positioning()
        return super(startWindow, self).resizeEvent(event)


if __name__ == '__main__':
    app = MainApp(sys.argv)
    sys.exit(app.exec_())
