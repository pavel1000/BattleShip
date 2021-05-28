import random
import socket
from PyQt5.QtWidgets import QWidget, QLabel, QFrame, QGridLayout, QMessageBox
from PyQt5.QtCore import Qt, QMargins, pyqtSignal
from PyQt5.QtGui import QPixmap

import field
import resources_rc
from view.game_field import Ui_Form


def RandomFieldFilling(field2):
    '''Метод для расстановки кораблей противника-бота.'''
    field2.clear()
    randomField = field.GetShipPlacement()
    for i in range(1, 11):
        for j in range(1, 11):
            if randomField.f[i][j] is True:
                field2.IndicateCell((i-1), (j-1))


class net_game_field(QWidget):
    closed = pyqtSignal()

    def __init__(self, fields, connect, turn):
        super(net_game_field, self).__init__()
        self.connect = connect
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.fields = fields
        self.shots = {"username": field.Field(), "enemy": field.Field()}
        if turn == 0:
            self.turn = {"username": True, "enemy": False}
        else:
            self.turn = {"username": False, "enemy": True}

        RandomFieldFilling(self.fields['enemy'])
        # print('Поле противника')
        # fields['enemy'].prints()
        self.UI()

    def UI(self):
        self.cells = self.ui.field.findChildren(QLabel)
        self.cells_2 = self.ui.field_2.findChildren(QLabel)
        self.fieldAlignment(self.ui.field, self.cells)
        self.fieldAlignment(self.ui.field_2, self.cells_2)
    
    def resetFields(self):
        for c in self.cells:
            c.setPixmap(QPixmap(':/images/square.png'))
        for c in self.cells_2:
            c.setPixmap(QPixmap(':/images/square.png'))
        # reset shots
        for s in self.shots.values():
            s.clear()
        RandomFieldFilling(self.fields['enemy'])
        # TODO: Надо будет добавить рандом для
        # выбора очередности хода в "сетевой игре"
        self.turn = {"username": True, "enemy": False}

    def fieldAlignment(self, field, cells):
        '''Метод расставляет лейблы на поле при помощи QGridLayot.'''
        field.setLayout(QGridLayout())
        field.setFrameShape(QFrame.Shape.NoFrame)
        field.setLineWidth(0)
        field.layout().setContentsMargins(QMargins(0, 0, 0, 0))
        field.layout().setSpacing(0)
        for i in range(10):
            for j in range(10):
                field.layout().addWidget(cells[i*10+j], i, j)
        self.checkCellsSize(cells)

    def checkCellsSize(self, cells):
        '''проверка корректности размера ячеек поля'''
        standartWidth, standartHeight = cells[0].width(), cells[0].height()
        equalWidth, equalHeight = True, True
        for c in cells:
            if c.width() != standartWidth:
                equalWidth = False
            if c.height() != standartHeight:
                equalHeight = False
        if not equalWidth:
            print('Неравная ширина ячеек')
        if not equalHeight:
            print('Неравная высота ячеек')

    def positioning(self):
        '''Задание относительного положения элементов'''
        # поле 1
        fieldSize = min(self.width()*4//10, self.height()*8//10)
        fieldSize -= fieldSize % 10
        x = (self.width()//2-fieldSize)//2
        y = (self.height()-fieldSize)//2
        self.ui.field.setGeometry(x, y, fieldSize, fieldSize)
        # поле 2
        x = (self.width()//2-fieldSize)//2 + self.width()//2
        y = (self.height()-fieldSize)//2
        self.ui.field_2.setGeometry(x, y, fieldSize, fieldSize)
        self.checkCellsSize(self.cells)
        self.checkCellsSize(self.cells_2)

    def resizeEvent(self, event):
        '''Подгоняет размер элементов под размер экрана'''
        self.positioning()
        return super(net_game_field, self).resizeEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.turn['username'] is True:
            self.__mousePressPos = event.globalPos()
            click = event.pos() - self.ui.field.pos()
            x = click.x()
            y = click.y()
            cell = self.findCellByIndex(self.cells, x, y)
            if cell is not None:
                size = self.cells[0].width()
                pos = cell.pos()
                x, y = pos.x()//size, pos.y()//size
                if self.shots['username'].isHitted(y, x) is False:
                    self.shots['username'].IndicateCell(y, x)
                    
                    shot = str(y)+","+str(x)
                    self.connect.sendall(shot.encode())
                    
                    while True:
                        data = self.connect.recv(1024)
                        if data.decode() == 0:
                            hitted = True
                            break;
                        else:
                            hitted = False
                            break;
                            
                    if hitted is True:
                        cell.setPixmap(QPixmap(':/images/shape.png'))
                        # отмечаем ячейки, в которые можно не стрелять                
                        livingShips = self.fields['username'].GetAvailableShips(self.shots['username'])
                        if livingShips == field.Ships(0, 0, 0, 0):
                            
                            self.connect.sendall("win")
                            QMessageBox.about(self, 'The end', "Username ПРОИГРАЛ")
                            
                            self.turn['username'] = False
                            self.close()
                            self.closed.emit()
                    else:
                        cell.setPixmap(QPixmap(':/images/cross.png'))
                        self.turn['username'] = False
                        self.turn['enemy'] = True
                        
                        self.connect.sendall("turn")
                        
                        self.enemyTurn('enemy', 'username')
            else:
                self.enemyTurn('username', 'enemy')
                #Нужно, зачем не помню
                
        super(net_game_field, self).mousePressEvent(event)

    def findCellByIndex(self, cells, x, y):
        m = min(cells[0].size().width()//2+1, cells[0].size().height()//2+1)
        cell = None
        for c in cells:
            cx = c.geometry().center().x()
            cy = c.geometry().center().y()
            dist = max(abs(cx-x), abs(cy-y))
            if dist <= m:
                m = dist
                cell = c
        return cell

    def enemyTurn(self, username, enemy):
        while True:
            data = self.connect.recv()
            if data is not "":  
                if data.decode() == "turn":
                    self.turn['username'] = True
                    self.turn['enemu'] = False
                    
                    return
                    #Ход меяется
                elif data.decode() == "win":
                    QMessageBox.about(self, 'The end', "Username Выиграл")
                    self.close()
                    self.closed.emit()
                    return
                    #Ты выиграл, соперник проиграл
                else:
                    strs = data.decode().split(',')
                    x,y = int(strs[0]),int(strs[1])
                
        '''делаем рандомный выстрел за ИИ'''
        while self.turn[username] is True:
            flag = False
            while flag is False:
                row = random.randint(0, 100) % 10
                col = random.randint(0, 100) % 10
                if self.shots[username].isHitted(row, col) is False:
                    flag = True
            self.shots[username].IndicateCell(row, col)

            size = self.cells_2[0].width()
            x, y = col*size+size//2, row*size+size//2
            cell = self.findCellByIndex(self.cells_2, x, y)
            if cell is None:
                print('Боту не удалось найти ячейку для выстрела '+str(row)+' '+str(col))
                print('Останавка игры...')
                self.turn[enemy] = False
                self.turn[username] = False
                return
            x, y = cell.pos().x()//size, cell.pos().y()//size

            hitted, shooted = self.fields[enemy].GetStrickenShips(y, x, self.shots[username])
            if hitted is True:
                cell.setPixmap(QPixmap(':/images/shape.png'))
                # отмечаем ячейки, в которые можно не стрелять
                for s in shooted:
                    self.cells_2[s[0]*10+s[1]].setPixmap(QPixmap(':/images/cross.png'))
                livingShips = self.fields[enemy].GetAvailableShips(self.shots[username])
                if livingShips == field.Ships(0, 0, 0, 0):
                    print("Победил "+username)
                    QMessageBox.about(self, 'The end', "Победил "+username)
                    self.turn[username] = False
                    self.close()
                    self.closed.emit()
            else:
                cell.setPixmap(QPixmap(':/images/cross.png'))
                self.turn[enemy] = True
                self.turn[username] = False
    
    