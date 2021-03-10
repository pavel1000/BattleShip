import random
import sys

# Deliberately increased fieldSize for more convenient checking the field
fieldSize = 12
class StrickenShips:
    def __init__(self):
        self.Ambient = []
        self.Hitted = ""
        
class Ships:
    def __init__(self,SingleDecker,TwoDecker,ThreeDecker,FourDecker):
        self.SingleDecker = SingleDecker
        self.TwoDecker = TwoDecker
        self.ThreeDecker = ThreeDecker
        self.FourDecker = FourDecker
    
    def shrink (self, length):
        if length == 1:
            self.SingleDecker -= 1
        elif length == 2:
            self.TwoDecker -= 1
        elif length == 3:
            self.ThreeDecker -= 1
        elif length == 4:
            self.FourDecker -= 1
        
        
        
class Field:
    def __init__(self):
        """Constructor"""
        self.f = [[False]*fieldSize for i in range(fieldSize)]
            
    #f is a game field
    def IndicateCell (self, y, x):
        row = int(y) + 1
        col = int(x) + 1
        
        if self.f[row][col] == False:
            self.f[row][col] = True
            
    def GetAvailableShips (self):
        ships = Ships(4, 3, 2, 1)
        seenCells = [[False]*fieldSize for i in range(fieldSize)]
            
        shipLength = 0
        
        for i in range(1,fieldSize-1):
            for j in range (1,fieldSize):
                if self.f[i][j] == True:
                    if self.f[i][j-1] == True or self.f[i][j+1] == True:
                        shipLength +=1
                        seenCells[i][j] = True
                elif shipLength != 0:
                    ships.shrink(shipLength)
                    shipLength = 0
        
        for j in range(1,fieldSize-1):
            for i in range(1,fieldSize):
                if seenCells[i][j] == True:
                    continue
                if self.f[i][j] == True:
                    shipLength +=1
                elif shipLength != 0:
                    ships.shrink(shipLength)
                    shipLength = 0
        return ships
    
    # GetOrientation returns orientation of ship: false if the ship is horizontal and
    # true if the ship is vertical; i,j - positions of shift to left and right
    def GetOrientation(self, y, x):
        row = int(y)+1
        col = int(x)+1
        if self.f[row][col-1] == True or self.f[row][col+1] == True:
            i = 1
            while self.f[row][col-i] == True:
                i += 1
            j = 1
            while self.f[row][col+j] == True:
                j += 1
            return False, i - 1, j - 1
	
        i = 1
        while self.f[row-i][col] == True:
            i += 1
        j = 1
        while self.f[row+j][col] == True:
            j += 1
        return True, i - 1, j - 1
    
    def isDestroyed(self, y, x, f):
        row = int(y)+1
        col = int(x)+1
        direction, k, l = self.GetOrientation(row-1, col-1)
        if self.f[row][col] == False:
            return False
        if direction == True:
            for i in range(row-k, row+l+1, 1):
                if f.f[i][col] == False:
                    return False
        else:
            for i in range(col-k, col+l+1, 1):
                if f.f[row][i] == False:
                    return False
        
        return True

    def isHitted(self, y, x):
        return bool(self.f[y+1][x+1])
    
    #Возвращает уничтоженные корабли
    def GetStrickenShips(self, msg, shots):
        Stricken = StrickenShips()
        if self.isDestroyed(int(msg[0]), int(msg[1]), shots)==True:
            print("Уничтожен")
            Stricken.Hitted = msg
            return Stricken
        if self.isHitted(int(msg[0]), int(msg[1]))==True:
            print("Попал")
            Stricken.Hitted = msg
            Stricken.Ambient = msg
            return Stricken
        row = int(msg[0])+1
        col = int(msg[1])+1
        direction, k, l = self.GetOrientation(row, col)
        Stricken = StrickenShips()
        if direction == True:
            #отмечаем поля вокруг "убитого" корабля на бэкэнде?
            for i in range(row-k-1,row+l+2):
                pass
            #    Stricken.Ambient.append([i, col-1])
            #    Stricken.Ambient.append((i, col+1))
            #Stricken.Ambient.append((row-k-1, col))
            #Stricken.Ambient.append((row+l+1, col))
            for i in range(col - k,col+l+1):
                self.f[i+1][col+1]=False
        else:
            for i in range(col-k-1,col+l+2):
                pass
            #    Stricken.Ambient.append((row-1, i))
            #    Stricken.Ambient.append((row+1, i))
            #Stricken.Ambient.append((row, col-k-1))
            #Stricken.Ambient.append((row, col+l+1))
            for i in range(col - k,col+l+1):
                self.f[row+1][i+1] = False
        return Stricken
    
    def CheckPositionOfShips(self):
        if self.f.GetAvailableShips() != Ships(0, 0, 0, 0):
            return False
        seenCells = [[False]*fieldSize for i in range(fieldSize)]
        shipLength = 0
        #проход по горизонтал
        for i in range(1,fieldSize-1):
            for j in range(1,fieldSize):
                if self.f[i][j] == True:
                    if self.f[i][j-1] == True or self.f[i][j+1] == True:
                        shipLength += 1
                        seenCells[i][j] = True
                elif shipLength > 4:
                    return False
                elif shipLength != 0:
                    for k in range(j-shipLength-1, j+1):
                        if self.f[i-1][k] == True or self.f[i+1][k] == True:
                            return False
                    shipLength = 0
        #проход по вертикали
        for j in range(1,fieldSize-1):
            for i in range(1,fieldSize):
                if seenCells[i][j] == True:
                    continue
                if self.f[i][j] == True:
                    shipLength += 1
                elif shipLength > 4:
                    return False
                elif shipLength != 0:
                    for k in range(i-shipLength-1, i+1):
                        if self.f[k][j-1] == True or self.f[k][j+1] == True:
                            return False
                    shipLength = 0
        return True
    
    def prints(self):
        print("\n----------------------")
        print("  0 1 2 3 4 5 6 7 8 9")
        for i in range(1,fieldSize-1):
        #for i in range(0,fieldSize):
            sys.stdout.write(str(i-1)+" ")
            for j in range(1,fieldSize-1):
            #for j in range(0,fieldSize):
                if self.f[i][j] == True:
                    sys.stdout.write("X ")
                else:
                    sys.stdout.write("O ")
            print()
        sys.stdout.write("----------------------\n")
    
#Автоматическая расстановка кораблей на поле
def GetShipPlacement(temp):
    for lens in range (4,0,-1):#Тут переделал, посмотреть везде такие условия
        for k in range (lens, 5):#Тут переделал, посмотреть везде такие условия
            flag = True
            row1,col1,row2,col2 = 0,0,0,0
            while flag == True:
                flag = False
                orientation = random.randint(0, 100) % 2
                row1 = random.randint(0,100)%(10-(lens-1)*(1-orientation))+1
                col1 = random.randint(0,100)%(10-(lens-1)*orientation)+1
                if orientation == 1:
                    col2 = col1 + lens - 1
                    row2 = row1
                else:
                    row2 = row1 + lens - 1
                    col2 = col1
                #проверка, что корабль не пересекается с уже заданными
                for i in range(col1-1,col2+2):
                    for j in range(row1-1,row2+2):
                        if temp.f[j][i] == True:
                            flag=True
            for i in range(col1,col2+1):
                for j in range(row1,row2+1):
                    temp.f[j][i]=True
    return temp
