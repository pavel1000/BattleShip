import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal, QMargins
from PyQt5.QtGui import QPixmap

import field
from view.game_field import Ui_Form

turn = {"username": True, "enemy": False}

def RandomFieldFilling(field2):
    randomField = field.GetShipPlacement()
    for i in range(1, 11):
        for j in range(1, 11):
            if randomField.f[i][j] is True:
                field2.IndicateCell((i-1), (j-1))

class game_field(QWidget):
    def __init__(self, fields, shots):
        super(game_field, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.fields = fields
        self.shots = shots
        RandomFieldFilling(fields['enemy'])
        print('Поле противника')
        fields['enemy'].prints()
        self.UI()
    
    def UI(self):
        self.cells = self.ui.field.findChildren(QLabel)
        self.cells_2 = self.ui.field_2.findChildren(QLabel)
        #self.positioning()
        self.fieldAlignment(self.ui.field, self.cells)
        self.fieldAlignment(self.ui.field_2, self.cells_2)
    
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
        #поле 1
        fieldSize = min(self.width()*4//10, self.height()*8//10)
        fieldSize -= fieldSize % 10
        x = (self.width()//2-fieldSize)//2
        y = (self.height()-fieldSize)//2
        self.ui.field.setGeometry(x, y, fieldSize, fieldSize)
        #поле 2
        x = (self.width()//2-fieldSize)//2 + self.width()//2
        y = (self.height()-fieldSize)//2
        self.ui.field_2.setGeometry(x, y, fieldSize, fieldSize)
        self.checkCellsSize(self.cells)
        self.checkCellsSize(self.cells_2)
    
    def resizeEvent(self, event):
        '''Подгоняет размер элементов под размер экрана'''
        self.positioning()
        return super(game_field, self).resizeEvent(event)
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and turn['username'] is True:
            self.__mousePressPos = event.globalPos()
            click = event.pos() - self.ui.field.pos()
            x = click.x()
            y = click.y()
            m = min(self.cells[0].size().width()//2+1, self.cells[0].size().height()//2+1)
            cell = None
            for c in self.cells:
                cx = c.geometry().center().x()
                cy = c.geometry().center().y()
                dist = max(abs(cx-x), abs(cy-y))
                if dist <= m:
                    m = dist
                    cell = c
                    print(c.objectName())
            if cell is not None:
                size = self.cells[0].width()
                fp = self.ui.field.pos()
                pos = cell.pos()
                x, y = pos.x()//size, pos.y()//size
                print(y, x)
                if self.shots['username'].isHitted(y, x) is False:
                    self.shots['username'].IndicateCell(y, x)
                    self.shots['username'].prints()
                    strickenShips = self.fields['enemy'].GetStrickenShips(y, x, self.shots['username'])
                    if strickenShips is True:
                        livingShips = self.fields['enemy'].GetAvailableShips(self.shots['username'])
                        if livingShips == field.Ships(0, 0, 0, 0):
                            QMessageBox.about(self, 'The end', "Победил username")
                            turn['username'] = False
                        cell.setPixmap(QPixmap('../images/shape.png'))
                    else:
                        cell.setPixmap(QPixmap('../images/cross.png'))
                        turn['username'] = False
                        turn['enemy'] = True
                        self.enemyTurn('enemy', 'username')
        super(game_field, self).mousePressEvent(event)
    
    def enemyTurn(self, username, enemy):
        '''делаем рандомный выстрел за ИИ'''
        while turn[username] is True:
            flag = False
            while flag is False:
                row = random.randint(0, 100) % 10+1
                col = random.randint(0, 100) % 10+1
                if self.shots[username].f[row][col] is False:
                    flag = True
            row, col = row - 1, col - 1
            self.shots[username].IndicateCell(row, col)
            self.shots[username].prints()

            fp = self.ui.field_2.pos()
            size = self.cells_2[0].width()
            x, y = fp.x()+col*size, fp.y()+row*size
            m = min(self.cells[0].size().width()//2+1, self.cells[0].size().height()//2+1)
            cell = None
            for c in self.cells_2:
                cx = c.pos().x()+c.parent().pos().x()
                cy = c.pos().y()+c.parent().pos().y()
                dist = max(abs(cx-x), abs(cy-y))
                if dist <= m:
                    m = dist
                    cell = c
            if cell is not None:
                x, y = cell.pos().x()//size, cell.pos().y()//size
                print(y, x)
                cell.setPixmap(QPixmap('../images/cross.png'))
            else:
                print('Боту не удалось найти ячейку для выстрела '+str(row)+' '+str(col))
            
            strickenShips = self.fields[enemy].GetStrickenShips(row, col, self.shots[username])
            if strickenShips is True:
                livingShips = self.fields[enemy].GetAvailableShips(self.shots[username])
                if livingShips == field.Ships(0, 0, 0, 0):
                    print("Победил "+username)
                    QMessageBox.about(self, 'The end', "Победил"+username)
                    turn[username] = False
            else:
                turn[enemy] = True
                turn[username] = False