import random
import sys

# Deliberately increased fieldSize for more convenient checking the field
fieldSize = 12


class Ships:
    def __init__(self, SingleDecker, TwoDecker, ThreeDecker, FourDecker):
        self.SingleDecker = SingleDecker
        self.TwoDecker = TwoDecker
        self.ThreeDecker = ThreeDecker
        self.FourDecker = FourDecker
    
    def shrink(self, length):
        if length == 1:
            self.SingleDecker -= 1
        elif length == 2:
            self.TwoDecker -= 1
        elif length == 3:
            self.ThreeDecker -= 1
        elif length == 4:
            self.FourDecker -= 1
    
    def __str__(self):
        return ('('+str(self.SingleDecker)+', '+str(self.TwoDecker)+', ' +
                str(self.ThreeDecker)+', '+str(self.FourDecker)+')')
              
    def __eq__(self, other):
        if self.SingleDecker == other.SingleDecker and self.TwoDecker == other.TwoDecker \
            and self.ThreeDecker == other.ThreeDecker and self.FourDecker == other.FourDecker:
            return True
        else:
            return False
        

class Field:
    def __init__(self):
        '''f is a game field'''
        self.f = [[False]*fieldSize for i in range(fieldSize)]
            
    def clear(self):
        for i in range(0, fieldSize):
            for j in range(0, fieldSize):
                self.f[i][j] = False
    
    def IndicateCell(self, y, x):
        '''Принимает значения в диапозоне от 0 до 9.'''
        row = int(y) + 1
        col = int(x) + 1
        
        self.f[row][col] = True
            
    def GetAvailableShips(self, shots):
        '''Возвращает "живые" корабли в виде структуры(класса)'''
        ships = Ships(4, 3, 2, 1)
        seenCells = [[False]*fieldSize for i in range(fieldSize)]
            
        shipLength = 0
        
        for i in range(1, fieldSize-1):
            for j in range(1, fieldSize):
                if self.f[i][j] is True and self.f[i-1][j] is False and self.f[i+1][j] is False:
                    seenCells[i][j] = True
                    if self.f[i][j-1] is True:
                        shipLength += 1
                    else:
                        shipLength = 1
                elif shipLength != 0 and self.isDestroyed(i-1, j-2, shots):
                    ships.shrink(shipLength)
                    shipLength = 0
                else:
                    shipLength = 0

        for j in range(1, fieldSize-1):
            for i in range(1, fieldSize):
                if seenCells[i][j] is True:
                    continue
                if self.f[i][j] is True:
                    if self.f[i-1][j] is True:
                        shipLength += 1
                    else:
                        shipLength = 1
                elif shipLength != 0 and self.isDestroyed(i-2, j-1, shots):
                    ships.shrink(shipLength)
                    shipLength = 0
                else:
                    shipLength = 0
        return ships
    
    def GetOrientation(self, y, x):
        '''Определяет ориентацию корабля.Принимает значения в диапозоне от 0 до 9.\
        Возвращает true, если вертикальное направление и false если горизонтальное.'''
        row = int(y)+1
        col = int(x)+1
        if self.f[row][col-1] is True or self.f[row][col+1] is True:
            i = 1
            while self.f[row][col-i] is True:
                i += 1
            j = 1
            while self.f[row][col+j] is True:
                j += 1
            return False, i - 1, j - 1
        
        i = 1
        while self.f[row-i][col] is True:
            i += 1
        j = 1
        while self.f[row+j][col] is True:
            j += 1
        return True, i - 1, j - 1

    def isDestroyed(self, y, x, f):
        '''Проверяет уничтожен ли корабль.\
        Принимает значения в диапозоне от 0 до 9.'''
        row = int(y)+1
        col = int(x)+1
        vertical, k, m = self.GetOrientation(row-1, col-1)
        if self.f[row][col] is False:
            return False
        if vertical is True:
            for i in range(row-k, row+m+1):
                if f.f[i][col] is False:
                    return False
        else:
            for i in range(col-k, col+m+1):
                if f.f[row][i] is False:
                    return False
        return True

    def isHitted(self, y, x):
        return bool(self.f[y+1][x+1])

    def GetStrickenShips(self, row, col, shots):
        '''Возвращает статус выстрела (попал/не попал) и отмечает \
        соседние клетки при попадании'''
        shooted = []
        if self.isDestroyed(row, col, shots) is True:
            print("Уничтожен")
            vertical, k, m = self.GetOrientation(row, col)
            row += 1
            col += 1
            if vertical is True:
                for i in range(row-k-1, row+m+2):
                    for j in range(col-1, col+2):
                        if self.f[i][j] is False:
                            shots.f[i][j] = True
                            shooted.append([i-1, j-1])
            else:
                for i in range(col-k-1, col+m+2):
                    for j in range(row-1, row+2):
                        if self.f[i][j] is False:
                            shots.f[j][i] = True
                            shooted.append([i-1, j-1])
        elif self.isHitted(row, col) is True:
            print("Попал")
            row += 1
            col += 1
            shots.f[row-1][col-1] = True
            shots.f[row-1][col+1] = True
            shots.f[row+1][col-1] = True
            shots.f[row+1][col+1] = True
            shooted.append([row-2, col-2])
            shooted.append([row-2, col])
            shooted.append([row, col-2])
            shooted.append([row, col])
        else:
            return False, shooted
        return True, shooted
    
    def CheckPositionOfShips(self):
        seenCells = [[False]*fieldSize for i in range(fieldSize)]
        shipLength = 0
        #проход по горизонтал
        for i in range(1, fieldSize-1):
            for j in range(1, fieldSize):
                if self.f[i][j] is True:
                    if self.f[i][j-1] is True or self.f[i][j+1] is True:
                        shipLength += 1
                        seenCells[i][j] = True
                elif shipLength > 4:
                    return False
                elif shipLength != 0:
                    for k in range(j-shipLength-1, j+1):
                        if self.f[i-1][k] is True or self.f[i+1][k] is True:
                            return False
                    shipLength = 0
        #проход по вертикали
        for j in range(1, fieldSize-1):
            for i in range(1, fieldSize):
                if seenCells[i][j] is True:
                    continue
                if self.f[i][j] is True:
                    shipLength += 1
                elif shipLength > 4:
                    return False
                elif shipLength != 0:
                    for k in range(i-shipLength-1, i+1):
                        if self.f[k][j-1] is True or self.f[k][j+1] is True:
                            return False
                    shipLength = 0
        return True
    
    def prints(self):
        print("\n----------------------")
        print("  0 1 2 3 4 5 6 7 8 9")
        for i in range(1, fieldSize-1):
            sys.stdout.write(str(i-1)+" ")
            for j in range(1, fieldSize-1):
                if self.f[i][j] is True:
                    sys.stdout.write("X ")
                else:
                    sys.stdout.write("* ")
            print()
        sys.stdout.write("----------------------\n")


'''Автоматическая расстановка кораблей на поле'''
def GetShipPlacement():
    temp = Field()
    for lens in range(4, 0, -1):
        for k in range(lens, 5):
            flag = True
            row1, col1, row2, col2 = 0, 0, 0, 0
            while flag is True:
                flag = False
                orientation = random.randint(0, 100) % 2
                row1 = random.randint(0, 100) % (10-(lens-1)*(1-orientation))+1
                col1 = random.randint(0, 100) % (10-(lens-1)*orientation)+1
                if orientation == 1:
                    col2 = col1 + lens - 1
                    row2 = row1
                else:
                    row2 = row1 + lens - 1
                    col2 = col1
                #проверка, что корабль не пересекается с уже заданными
                for i in range(col1-1, col2+2):
                    for j in range(row1-1, row2+2):
                        if temp.f[j][i] is True:
                            flag = True
            for i in range(col1, col2+1):
                for j in range(row1, row2+1):
                    temp.f[j][i] = True
    return temp
