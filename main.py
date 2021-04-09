import field as f
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QMimeData, QPoint, pyqtSignal, QMargins
from PyQt5.QtGui import QDrag, QMouseEvent, QPixmap
from view.ship_placement5 import Ui_MainWindow
from view.form import Ui_Form
import sys
import math

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
    fix_pos = pyqtSignal()
    
    def __init__(self, f, p):
        super().__init__(p)
        self.section = None
        self.setGeometry(f.geometry())
        self.setLayout(QGridLayout())
        self.layout().setContentsMargins(QMargins(0, 0, 0, 0))
        self.layout().setSpacing(0)
        self.labels = f.findChildren(QLabel)
        self.shipLength = len(self.labels)
        for i in range(len(self.labels)):
            self.layout().addWidget(self.labels[i], 0, i)
        self.direction = 0        #horizontal
        
    def saveSection(self, pos):
        if self.direction == 0:
            dist = pos.x()
            for i in range(len(self.labels)):
                if dist >= self.labels[i].pos().x() and dist <= self.labels[i].pos().x() + self.labels[i].size().width():
                    self.section = i
        else:
            dist = pos.y()
            for i in range(len(self.labels)):
                if dist >= self.labels[i].pos().y() and dist <= self.labels[i].pos().y() + self.labels[i].size().height():
                    self.section = i
    
    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()
            self.saveSection(self.mapFromGlobal(self.__mousePressPos))
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
            self.lastPos = self.__mousePressPos
            self.fix_pos.emit()
            if moved.manhattanLength() > 3:
                print('drop')
                event.ignore()
                return
            else:
                print('click')
                #изменение положения корабля с горизонтального на вертикальное и наоборот
                self.changeDirection()
        super(DragFrame, self).mouseReleaseEvent(event)
    
    def changeDirection(self):
        for i in range(len(self.labels)):
            self.layout().removeWidget(self.labels[i])
        self.setGeometry(self.x(), self.y(), self.height(), self.width())
        if self.direction == 0:
            for i in range(len(self.labels)):
                self.layout().addWidget(self.labels[i], i, 0)
        else:
            for i in range(len(self.labels)):
                self.layout().addWidget(self.labels[i], 0, i)
        self.direction = 1 - self.direction

class startWindow(QMainWindow):
    def __init__(self, window):
        super(startWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.window = window
        self.ui.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        self.hide()
        self.window.show()

class myWindow(QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.UI()

    def UI(self):
        pixmap = QPixmap('e:/программы/Python/GitProjects/BattleShip/images/cross.png').scaled(self.ui.frame_4.size().width()-2, self.ui.frame_4.size().height()-2)
        self.ui.pushButton_1 = DragButton(self.ui.pushButton_1, self.ui.pushButton_1.parent())
        self.ui.frame_4 = DragFrame(self.ui.frame_4, self.ui.frame_4.parent())
        self.ui.frame_5 = DragFrame(self.ui.frame_5, self.ui.frame_5.parent())
        self.ui.frame_6 = DragFrame(self.ui.frame_6, self.ui.frame_6.parent())
        self.ui.frame_7 = DragFrame(self.ui.frame_7, self.ui.frame_7.parent())
        self.ui.frame_4.fix_pos.connect(self.fixCell)
        self.ui.frame_5.fix_pos.connect(self.fixCell)
        self.ui.frame_6.fix_pos.connect(self.fixCell)
        self.ui.frame_7.fix_pos.connect(self.fixCell)

        self.saveShipsGeometry()

        self.ui.pushButton_1.clicked.connect(self.returnFrames)
        self.ui.pushButton_2.clicked.connect(self.loadGame)

    def saveShipsGeometry(self):
        self.framesGeometry = []
        for i in self.findChildren(DragFrame):
            self.framesGeometry.append(i.geometry())

    def returnFrames(self):
        frames = self.findChildren(DragFrame)
        for j in range(len(frames)):
            frames[j].setGeometry(self.framesGeometry[j])
            if frames[j].direction == 1:
                for i in range(len(frames[j].labels)):
                    frames[j].layout().removeWidget(frames[j].labels[i])
                for i in range(len(frames[j].labels)):
                    frames[j].layout().addWidget(frames[j].labels[i], 0, i)
                frames[j].direction = 0
    
    def fixCell(self):
        dragged_ship = self.sender()
        cells = self.ui.frame_3.findChildren(QLabel)
        x = dragged_ship.pos().x()+dragged_ship.labels[dragged_ship.section].geometry().center().x()
        y = dragged_ship.pos().y()+dragged_ship.labels[dragged_ship.section].geometry().center().y()
        m = min(cells[0].size().width()//2+1, cells[0].size().height()//2+1)
        pos = None
        for c in cells:
            cx = c.geometry().center().x()+c.parent().pos().x()
            cy = c.geometry().center().y()+c.parent().pos().y()
            dist = max(abs(cx-x), abs(cy-y))
            if dist <= m:
                m = dist
                pos = c.pos()+c.parent().pos()-dragged_ship.labels[dragged_ship.section].pos()
                print(c.objectName())
        if pos != None:
            dragged_ship.setGeometry(pos.x(),pos.y(),dragged_ship.width(),dragged_ship.height())
    
    def loadGame(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    placement = myWindow()
    start = startWindow(placement)
    start.show()
    sys.exit(app.exec_())
