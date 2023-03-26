import os
import time

def playing_field(A,row,col):
    print(f"     {col[0]}     {col[1]}     {col[2]}")
    print(f"{row[0]}    {A[0][0]}  │  {A[0][1]}  │  {A[0][2]}  ")
    print(f"   ─────┼─────┼─────")
    print(f"{row[1]}    {A[1][0]}  │  {A[1][1]}  │  {A[1][2]}  ")
    print(f"   ─────┼─────┼─────")
    print(f"{row[2]}    {A[2][0]}  │  {A[2][1]}  │  {A[2][2]}  ")

def coordinates(player):
    col = ["1", "2", "3"]
    row = [" ", " ", " "]
    print(f'Ходит игрок "{player}"')
    playing_field(A,row,col)
    x = input("Выберите столбец : ")
    while x not in col:
        x = input("Неправильное значение! Выберите столбец 1, 2 или 3: ")
    if x == "1":
        col = ["▼", " ", " "]
    elif x == "2":
        col = [" ", "▼", " "]
    else:
        col = [" ", " ", "▼"]
    row = ["1", "2", "3"]
    os.system('cls')
    print(f'Ходит игрок "{player}"')
    playing_field(A,row,col)
    y = input("Выберите строку: ")
    while y not in row:
        y = input("Неправильное значение! Выберите строку 1, 2 или 3: ")
    return x,y

def nextstep(player):
    os.system('cls')
    coord = coordinates(player)
    if (A[int(coord[1])-1][int(coord[0])-1] == "X") or (A[int(coord[1])-1][int(coord[0])-1] == "O"):
        print(f"В это поле уже был ход. Выберите другие координаты.")
        time.sleep(2)
    else:
        A[int(coord[1])-1][int(coord[0])-1] = player
        player = change_player(player)
    return player

def change_player(player):
    if player == "X":
        player = "O"
    else:
        player = "X"
    return player

A = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player = "X"
draw = None
print('Добро пожаловать в игру "Крестики-Нолики"')
time.sleep(2)

while True:
    player = nextstep(player)
    if any([(A[0][0] == A[0][1] == A[0][2] != " "),
            (A[1][0] == A[1][1] == A[1][2] != " "),
            (A[2][0] == A[2][1] == A[2][2] != " "),
            (A[0][0] == A[1][0] == A[2][0] != " "),
            (A[0][1] == A[1][1] == A[2][1] != " "),
            (A[0][2] == A[1][2] == A[2][2] != " "),
            (A[0][0] == A[1][1] == A[2][2] != " "),
            (A[0][2] == A[1][1] == A[2][0] != " ")]):
        player = change_player(player)
        os.system('cls')
        print(f'Победил игрок "{player}"!')
        row = [" ", " ", " "]
        col = [" ", " ", " "]
        playing_field(A, row, col)
        time.sleep(5)
        break
    elif ((' '.join(map(str, A))).find("' '") == -1):
        os.system('cls')
        print("Ничья!")
        row = [" ", " ", " "]
        col = [" ", " ", " "]
        playing_field(A, row, col)
        time.sleep(5)
        break






