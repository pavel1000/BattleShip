import field as f


# now, to clear the screen


shots = {"username":f.Field(),"enemy":f.Field()}
shots["username"] = f.Field()
shots["enemy"] = f.Field()

fields = {"username":f.Field(),"enemy":f.Field()}
fields["username"] = f.Field()
fields["enemy"] = f.Field()

turn = {"username":False,"enemy":False}

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
        destroyedShips = fields[enemy].GetAvailableShips()
        turn[enemy] = False
        turn[username] = True
        if destroyedShips == f.Ships(4, 3, 2, 1):
            print("Победил 1-й игрок")
            #stillPlaying = False
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
    fields[username].prints()
    fields[enemy].prints()
    
    # Записали попадание в shots, после получили структуру
    # сбитых и прилежащих к сбитым ячеек, отправили ее для рендера
    # у себя, изменили ее для последующего рендера у 2-ого игрока
    # и записали эти изменения на его имя
    while stillPlaying==True:
        if turn[enemy] == True:
            stillPlaying=playerTurn(enemy,username)
        else:
            stillPlaying=playerTurn(username,enemy)
        
def RandomFieldFilling(name):
    fields[name] = f.Field()
    randomField = f.GetShipPlacement(fields[name])
    for i in range(1,11):
        for j in range(1,11):
            if randomField.f[i][j] == True:
                fields[name].IndicateCell((i-1), (j-1))
                 
Game()