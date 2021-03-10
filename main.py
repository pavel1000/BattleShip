import field as f


# now, to clear the screen


shots = {"username":f.Field(),"enemy":f.Field()}
shots["username"] = f.Field()
shots["enemy"] = f.Field()

fields = {"username":f.Field(),"enemy":f.Field()}
fields["username"] = f.Field()
fields["enemy"] = f.Field()

turn = {"username":False,"enemy":False}

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
    while stillPlaying==True:
        if turn[enemy] == True:
            print("Игрок 2")
            print("Выберите точку удара: ")
            shots[enemy].prints()
            msg = input().split(" ")
            shots[enemy].IndicateCell(int(msg[0]), int(msg[1]))
            strickenShips = fields[username].GetStrickenShips(msg, shots[enemy])
            #print("Ваше поле")
            #fields[enemy].prints()
            print("Поле соперника")
            shots[enemy].prints()
            if strickenShips.Hitted != "":
                destroyedShips = fields[username].GetAvailableShips()
                turn[username] = False
                turn[enemy] = True
                if destroyedShips == f.Ships(4, 3, 2, 1):
                    print("Победил 2-й игрок")
                    stillPlaying = False
                    continue
            else:
                turn[username] = True
                turn[enemy] = False
                print("Промазал")
            print()
		# Записали попадание в shots, после получили структуру
		# сбитых и прилежащих к сбитым ячеек, отправили ее для рендера
		# у себя, изменили ее для последующего рендера у 2-ого игрока
		# и записали эти изменения на его имя
        else:
            print("Игрок 1")
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
                destroyedShips = fields[enemy].GetAvailableShips()
                turn[enemy] = False
                turn[username] = True
                if destroyedShips == f.Ships(4, 3, 2, 1):
                    print("Победил 1-й игрок")
                    stillPlaying = False
                    continue
            else:
                turn[enemy] = True
                turn[username] = False
                print("Промазал")
            print()
        
def RandomFieldFilling(name):
    fields[name] = f.Field()
    randomField = f.GetShipPlacement(fields[name])
    for i in range(1,11):
        for j in range(1,11):
            if randomField.f[i][j] == True:
                fields[name].IndicateCell((i-1), (j-1))
                 
Game()