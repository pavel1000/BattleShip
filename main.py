from placement import *
from view.form import Ui_Form

import sys

shots = {"username": field.Field(), "enemy": field.Field()}

fields = {"username": field.Field(), "enemy": field.Field()}

def playerTurn(username, enemy):
    print(username)
    print("Выберите точку удара: ")
    shots[username].prints()
    msg = input().split(" ")
    shots[username].IndicateCell(int(msg[0]), int(msg[1]))
    strickenShips = fields[enemy].GetStrickenShips(msg, shots[username])
    #print("Ваше поле")
    #fields[username].prints()
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


class startWindow(QMainWindow):
    def __init__(self, fields, shots):
        super(startWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.placement = ship_placement(fields, shots)

        self.ui.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        self.close()
        self.placement.show()
    
    def positioning(self):
        x = self.width()//2 - self.ui.pushButton.width()//2
        y = self.height()//2 - self.ui.pushButton.height()//2
        self.ui.pushButton.setGeometry(x, y, self.ui.pushButton.width(), self.ui.pushButton.height())
    
    def resizeEvent(self, event):
        '''Подгоняет размер элементов под размер экрана'''
        self.positioning()
        return super(startWindow, self).resizeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    start = startWindow(fields, shots)
    start.show()
    sys.exit(app.exec_())