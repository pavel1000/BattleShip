import field as f
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QMimeData, QPoint
from PyQt5.QtGui import QDrag, QMouseEvent, QPixmap
from view.ship_placement5 import Ui_MainWindow
from view.form import Ui_Form
import sys

import sys
shots = {"username": f.Field(), "enemy": f.Field()}
shots["username"] = f.Field()
shots["enemy"] = f.Field()

fields = {"username": f.Field(), "enemy": f.Field()}
fields["username"] = f.Field()
fields["enemy"] = f.Field()

turn = {"username": False, "enemy": False}
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
        destroyedShips = fields[enemy].GetAvailableShips(shots[username])
        print(destroyedShips)
        turn[enemy] = False
        turn[username] = True
        if destroyedShips == f.Ships(4, 3, 2, 1):
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
        

def RandomFieldFilling(name):
    fields[name] = f.Field()
    randomField = f.GetShipPlacement(fields[name])
    for i in range(1, 11):
        for j in range(1, 11):
            if randomField.f[i][j] is True:
                fields[name].IndicateCell((i-1), (j-1))


class DragButton(QPushButton):
    def __init__(self, but, p):
        super().__init__(but.text(), p)
        self.setGeometry(but.geometry())
        but.deleteLater()

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

        super(DragButton, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.__mouseMovePos = globalPos

        super(DragButton, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos 
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        super(DragButton, self).mouseReleaseEvent(event)

class DragFrame(QFrame):
    def __init__(self, f, p):
        super().__init__(p)
        self.setGeometry(f.geometry())
        self.setLayout(f.layout())
        for c in f.findChildren(QLabel):
            c.setParent(self)

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

        super(DragFrame, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            # adjust offset from clicked point to origin of widget
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            newPos = self.mapFromGlobal(currPos + diff)
            self.move(newPos)

            self.__mouseMovePos = globalPos

        super(DragFrame, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos 
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        super(DragFrame, self).mouseReleaseEvent(event)

class mywindow(QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.startWidget = QWidget()
        self.ui.startWidget = Ui_Form()
        self.ui.startWidget.setupUi(self)

        pixmap = QPixmap('e:/программы/Python/GitProjects/BattleShip/images/cross.png').scaled(self.ui.frame_4.size().width()-2, self.ui.frame_4.size().height()-2)
        self.ui.pushButton_1 = DragButton(self.ui.pushButton_1, self.ui.pushButton_1.parent())
        self.ui.frame_4 = DragFrame(self.ui.frame_4, self.ui.frame_4.parent())
        self.ui.frame_5 = DragFrame(self.ui.frame_5, self.ui.frame_5.parent())
        self.ui.frame_6 = DragFrame(self.ui.frame_6, self.ui.frame_6.parent())
        self.ui.frame_7 = DragFrame(self.ui.frame_7, self.ui.frame_7.parent())
        self.ui.centralwidget.hide()
        self.ui.startWidget.pushButton.clicked.connect(self.on_click)


    def on_click(self):
        self.ui.centralwidget.show()
        self.ui.startWidget.pushButton.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    #ex = MainWindow()
    application = mywindow()
    application.show()
    sys.exit(app.exec_())
