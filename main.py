import field as fil


# now, to clear the screen


shots = {"username":fil.Field(),"enemy":fil.Field()}
shots["username"] = fil.Field()
shots["enemy"] = fil.Field()

fields = {"username":fil.Field(),"enemy":fil.Field()}
fields["username"] = fil.Field()
fields["enemy"] = fil.Field()

turn = {"username":False,"enemy":False}

def HitEnemyShips():
    username = "username"
    RandomFieldFilling(username)
    enemy = "enemy"
    RandomFieldFilling(enemy)
    WinWrapper = False
    while not WinWrapper:
        if turn[enemy] == True:
            print("Игрок 2")
            print("Выберите точку удара: ")
            shots[enemy].prints()
            msg = input().split(",")
            shots[enemy].IndicateCell(int(msg[0]), int(msg[1]))
            strickenShips = fields[username].GetStrickenShips(msg, username)
            print("Ваши корабли \n")
            fields[enemy].prints()
            print("Корабли соперника \n")
            shots[enemy].prints()
            if strickenShips.Hitted != "":
                qua = fields[enemy].GetAvailableShips()
                turn[enemy] = False
                if qua == fil.Ships(4, 3, 2, 1):
                    print("Победил 2 игрок")
                    WinWrapper = True
                    continue
                print("Попал")
                turn[enemy] = True
            else:
                print("Промазал")
                turn[username] = True
                turn[enemy] = False
            print("Конец хода, введите любой символ для продолжения")
            input()
            print(100*'\n')
		# Записали попадание в shots, после получили структуру
		# сбитых и прилежащих к сбитым ячеек, отправили ее для рендера
		# у себя, изменили ее для последующего рендера у 2-ого игрока
		# и записали эти изменения на его имя
        else:
            print("Игрок 1")
            print("Выберите точку удара: ")
            shots[username].prints()
            msg = input().split(",")
            shots[username].IndicateCell(int(msg[0]), int(msg[1]))
            strickenShips = fields[enemy].GetStrickenShips(msg, username)
            print("Ваши корабли \n")
            fields[username].prints()
            print("Корабли соперника \n")
            shots[username].prints()
            if strickenShips.Hitted != "":
                qua = fields[enemy].GetAvailableShips()
                turn[enemy] = False
                if qua == fil.Ships(4, 3, 2, 1):
                    print("Победил 1 игрок")
                    WinWrapper = True
                    continue
                print("Попал")
                turn[username] = True
            else:
                print("Промазал")
                turn[enemy] = True
                turn[username] = False
            print("Конец хода, введите любой символ для продолжения")
            input()
            print(100*'\n')
        
def RandomFieldFilling(username):
    fields[username] = fil.Field()
    randomField = fil.GetRandomField(fil.Field())
    for i in range(1,11):
        for j in range(1,11):
             if randomField.f[i][j] == True:
                 fields[username].IndicateCell((i-1), (j-1))
                 
HitEnemyShips()