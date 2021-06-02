import random
from PyQt5.QtWidgets import QFrame, QLabel, QGridLayout, QWidget
from PyQt5.QtCore import Qt, pyqtSignal, QMargins

import field
from view.ship_placement7 import Ui_Form


class DragFrame(QFrame):
    '''Вспомогательный класс-обертка, добавляющий \
    фреймам особенности "корабля".'''
    fix_pos = pyqtSignal()

    def __init__(self, f, p):
        super().__init__(p)
        self.clickSection = None
        self.onField = 0
        self.direction = 0        # 0 - horizontal
        self.labels = f.findChildren(QLabel)
        self.length = len(self.labels)

        # set position and layout
        self.setGeometry(f.x(), f.y(), f.height()*self.length, f.height())
        self.setLayout(QGridLayout())
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)
        self.layout().setContentsMargins(QMargins(0, 0, 0, 0))
        self.layout().setSpacing(0)
        for i in range(len(self.labels)):
            self.layout().addWidget(self.labels[i], 0, i)

        self.startGeometry = self.geometry()

    def restoreGeometry(self):
        self.setGeometry(self.startGeometry)
        if self.direction == 1:
            for i in range(len(self.labels)):
                self.layout().removeWidget(self.labels[i])
            for i in range(len(self.labels)):
                self.layout().addWidget(self.labels[i], 0, i)
            self.direction = 0
        self.onField = 0

    def saveSection(self, pos):
        if self.direction == 0:
            dist = pos.x()
            for i in range(len(self.labels)):
                if dist >= self.labels[i].pos().x() and dist <= self.labels[i].pos().x() + self.labels[i].size().width():
                    self.clickSection = i
        else:
            dist = pos.y()
            for i in range(len(self.labels)):
                if dist >= self.labels[i].pos().y() and dist <= self.labels[i].pos().y() + self.labels[i].size().height():
                    self.clickSection = i

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
            if moved.manhattanLength() > 3:
                self.fix_pos.emit()
                print('drop')
                event.ignore()
                return
            else:
                print('click')
                # изменение положения корабля с горизонтального
                # на вертикальное и наоборот
                if self.onField == 1:
                    self.changeDirection()
                    self.fix_pos.emit()
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

    def is_cross(self, x, y, w, h):
        # координаты x обеих точек корабля 1
        xA = [self.pos().x(), self.pos().x()+self.width()]
        # координаты x обеих точек корабля 2
        xB = [x, x+w]
        # координаты y обеих точек корабля 1
        yA = [self.pos().y(), self.pos().y()+self.height()]
        # координаты y обеих точек корабля 2
        yB = [y, y+h]

        if max(xB) < min(xA) or max(xA) < min(xB) or max(yA) < min(yB) or max(yB) < min(yA):
            return False
        return True


class ship_placement(QWidget):
    nextWin = pyqtSignal()
    closed = pyqtSignal()

    def __init__(self):
        super(ship_placement, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.fields = {"username": field.Field(), "enemy": field.Field()}
        self.UI()

    def UI(self):
        self.labels = [self.ui.label_111, self.ui.label_112, self.ui.label_113, self.ui.label_114]
        self.cells = self.ui.field.findChildren(QLabel)
        self.framesToShips()
        self.fieldAlignment()
        self.ui.start_button.setDisabled(True)

        self.ui.reset_button.clicked.connect(self.returnShips)
        self.ui.start_button.clicked.connect(self.loadGame)
        self.ui.random_button.clicked.connect(self.randomFilling)

    def framesToShips(self):
        '''Преобразует фрейм в класс с функционалом корабля'''
        self.singleDecker = []
        self.singleDecker.append(DragFrame(self.ui.One_1, self.ui.One_1.parent()))
        self.singleDecker.append(DragFrame(self.ui.One_2, self.ui.One_2.parent()))
        self.singleDecker.append(DragFrame(self.ui.One_3, self.ui.One_3.parent()))
        self.singleDecker.append(DragFrame(self.ui.One_4, self.ui.One_4.parent()))
        self.twoDecker = []
        self.twoDecker.append(DragFrame(self.ui.Two_1, self.ui.Two_1.parent()))
        self.twoDecker.append(DragFrame(self.ui.Two_2, self.ui.Two_2.parent()))
        self.twoDecker.append(DragFrame(self.ui.Two_3, self.ui.Two_3.parent()))
        self.threeDecker = []
        self.threeDecker.append(DragFrame(self.ui.Three_1, self.ui.Three_1.parent()))
        self.threeDecker.append(DragFrame(self.ui.Three_2, self.ui.Three_2.parent()))
        self.fourDecker = []
        self.fourDecker.append(DragFrame(self.ui.Four_1, self.ui.Four_1.parent()))
        # присоединяем события "drop'a" корабля
        self.ships = [self.singleDecker, self.twoDecker, self.threeDecker, self.fourDecker]
        for ship in self.ships:
            for i in range(len(ship)):
                ship[i].fix_pos.connect(self.fixCell)

    def returnShips(self):
        for ship in self.ships:
            for s in ship:
                s.restoreGeometry()
        self.fields['username'].clear()
        self.updateCounts()

    def fieldAlignment(self):
        '''Метод расставляет лейблы на поле при помощи QGridLayot.'''
        self.ui.field.setLayout(QGridLayout())
        self.ui.field.setFrameShape(QFrame.Shape.NoFrame)
        self.ui.field.setLineWidth(0)
        self.ui.field.layout().setContentsMargins(QMargins(0, 0, 0, 0))
        self.ui.field.layout().setSpacing(0)
        for i in range(10):
            for j in range(10):
                self.ui.field.layout().addWidget(self.cells[i*10+j], i, j)
        self.checkCellsSize()

    def checkCellsSize(self):
        '''Проверка корректности размера ячеек поля\
        (то есть равенства ширины и высоты).'''
        standartWidth, standartHeight = self.cells[0].width(), self.cells[0].height()
        equalWidth, equalHeight = True, True
        for c in self.cells:
            if c.width() != standartWidth:
                equalWidth = False
            if c.height() != standartHeight:
                equalHeight = False
        if not equalWidth:
            print('Неравная ширина ячеек')
        if not equalHeight:
            print('Неравная высота ячеек')

    def fixCell(self):
        '''Фиксирует корабль над ячейкой поля.'''
        dragged_ship = self.sender()
        x = dragged_ship.pos().x()+dragged_ship.labels[dragged_ship.clickSection].geometry().center().x()
        y = dragged_ship.pos().y()+dragged_ship.labels[dragged_ship.clickSection].geometry().center().y()
        m = min(self.cells[0].size().width()//2+1, self.cells[0].size().height()//2+1)

        pos = None
        for c in self.cells:
            cx = c.geometry().center().x()+c.parent().pos().x()
            cy = c.geometry().center().y()+c.parent().pos().y()
            dist = max(abs(cx-x), abs(cy-y))
            if dist <= m:
                m = dist
                pos = c.pos()+c.parent().pos()-dragged_ship.labels[dragged_ship.clickSection].pos()

        if pos is not None and self.shipsIntersection(pos.x(), pos.y(), dragged_ship) is False:
            # устанавлка позиции корабля
            dragged_ship.setGeometry(pos.x(), pos.y(), dragged_ship.width(), dragged_ship.height())
            dragged_ship.onField = 1
            # проверка выхода за границы поля
            self.checkOutOfBounds(dragged_ship)
        else:
            dragged_ship.onField = 0
            dragged_ship.restoreGeometry()
        self.updateCounts()

    def shipsIntersection(self, x, y, sample):
        '''проверка на пересечения кораблей'''
        for ship in self.ships:
            for s in ship:
                if s is sample:
                    continue
                if s.is_cross(x, y, sample.width(), sample.height()) is True:
                    return True
        return False

    def checkOutOfBounds(self, ship):
        '''Проверка выхода за границы поля'''
        pos = ship.pos() - self.ui.field.pos()
        size = self.cells[0].width()
        x, y = pos.x()//size, pos.y()//size
        if ship.direction == 0:
            # первое слагаемое от 0 до 9, второе от 1 до 4
            shift = x + ship.length - 10
            if (shift > 0):     # проверка на выход за правую границу
                if self.shipsIntersection(ship.pos().x()-shift*size, ship.pos().y(), ship) is True:
                    ship.onField = 0
                    ship.restoreGeometry()
                    return
                ship.setGeometry(ship.pos().x()-shift*size, ship.pos().y(), ship.width(), ship.height())
            elif x < 0:     # проверка на выход за левую границу
                if self.shipsIntersection(ship.pos().x()-x*size, ship.pos().y(), ship) is True:
                    ship.onField = 0
                    ship.restoreGeometry()
                    return
                ship.setGeometry(ship.pos().x()-x*size, ship.pos().y(), ship.width(), ship.height())
        else:
            shift = pos.y()//size + ship.length - 10
            if (shift > 0):     # проверка на выход за верхнюю границу
                if self.shipsIntersection(ship.pos().x(), ship.pos().y()-shift*size, ship) is True:
                    ship.onField = 0
                    ship.restoreGeometry()
                    return
                ship.setGeometry(ship.pos().x(), ship.pos().y()-shift*size, ship.width(), ship.height())
            elif y < 0:     # проверка на выход за верхнюю границу
                if self.shipsIntersection(ship.pos().x(), ship.pos().y()-y*size, ship) is True:
                    ship.onField = 0
                    ship.restoreGeometry()
                    return
                ship.setGeometry(ship.pos().x(), ship.pos().y()-y*size, ship.width(), ship.height())
            

    def updateCounts(self):
        j, k = 0, 0
        for ship in self.ships:
            n = 0
            for i in range(len(ship)):
                n += ship[i].onField
            k += len(ship)-n
            self.labels[j].setText('x'+str(len(ship)-n))
            j += 1
        if k == 0:
            self.ui.start_button.setEnabled(True)
        else:
            self.ui.start_button.setDisabled(True)

    def positioning(self):
        '''Задание относительного положения элементов'''
        self.returnShips()
        # поле
        fieldSize = min(self.width()*4//10, self.height()*8//10)
        fieldSize -= fieldSize % 10
        x = (self.width()//2-fieldSize)//2
        y = (self.height()-fieldSize)//2
        self.ui.field.setGeometry(x, y, fieldSize, fieldSize)
        self.checkCellsSize()
        # корабли
        x = self.width()*6.5//10
        j = 0.0
        for ship in self.ships:
            for i in range(len(ship)):
                ship[i].setGeometry(x, y+(j*fieldSize)//10, ship[i].length*fieldSize//10, fieldSize//10)
                ship[i].startGeometry = ship[i].geometry()
            j += 1.5
        # лейблы
        x = self.width()*6//10
        y = (self.height()-fieldSize)//2
        j = 0.0
        for lbl in self.labels:
            lbl.setGeometry(x, y+(j*fieldSize)//10, fieldSize//10, fieldSize//10)
            font = lbl.font()
            font.setPixelSize(fieldSize//10)
            lbl.setFont(font)
            j += 1.5
        # кнопки
        x = self.width()*5.5//10
        h = 1.5
        y = (self.height()-fieldSize)//2+fieldSize*(10-h)//10
        kw = 1.7
        w = self.width()*kw//10
        self.ui.random_button.setGeometry(self.width()*7.5//10 - w//2, y - (h+0.75)*fieldSize//10, w, fieldSize*h//10)
        self.ui.reset_button.setGeometry(x, y, w, fieldSize*h//10)
        self.ui.start_button.setGeometry(x+self.width()*(4-kw)//10, y, w, fieldSize*h//10)

    def resizeEvent(self, event):
        '''Подгоняет размер элементов под размер экрана'''
        self.positioning()
        return super(ship_placement, self).resizeEvent(event)

    def loadGame(self):
        self.initField()
        # self.fields['username'].prints()
        if self.fields['username'].CheckPositionOfShips() is True:
            print('Корабли расставлены верно')
            self.nextWin.emit()
            self.close()
        else:
            print('Корабли расставлены НЕ верно')
            self.ui.start_button.setDisabled(True)

    def initField(self):
        self.fields['username'].clear()
        size = self.cells[0].width()
        fp = self.ui.field.pos()
        for ship in self.ships:
            for s in ship:
                pos = s.pos() - fp
                x, y = pos.x()//size, pos.y()//size
                for i in range(s.length):
                    self.fields['username'].IndicateCell(y+s.direction*i, x+(1-s.direction)*i)

    def randomFilling(self):
        self.fields['username'].clear()
        self.returnShips()
        temp = field.Field()
        size = self.cells[0].width()
        fp = self.ui.field.pos()
        for lens in range(3, -1, -1):
            for k in range(lens-4, 0):
                flag = True
                row1, col1, row2, col2 = 0, 0, 0, 0
                while flag is True:
                    flag = False
                    orientation = random.randint(0, 100) % 2
                    row1 = random.randint(0, 100) % (10-lens*orientation)+1
                    col1 = random.randint(0, 100) % (10-lens*(1-orientation))+1
                    if orientation == 0:
                        col2 = col1 + lens
                        row2 = row1
                    else:
                        row2 = row1 + lens
                        col2 = col1
                    # проверка, что корабль не пересекается с уже заданными
                    for i in range(row1-1, row2+2):
                        for j in range(col1-1, col2+2):
                            if temp.f[i][j] is True:
                                flag = True
                for i in range(row1, row2+1):
                    for j in range(col1, col2+1):
                        temp.f[i][j] = True
                row1, col1 = row1 - 1, col1 - 1
                self.ships[lens][k].setGeometry(fp.x()+col1*size, fp.y()+row1*size, self.ships[lens][k].width(), self.ships[lens][k].height())
                self.ships[lens][k].onField = True
                if orientation == 1:
                    self.ships[lens][k].changeDirection()
        for i in range(1, 11):
            for j in range(1, 11):
                if temp.f[i][j] is True:
                    self.fields['username'].IndicateCell((i-1), (j-1))
        self.fields['username'].prints()
        self.ui.start_button.setEnabled(True)
        self.updateCounts()
