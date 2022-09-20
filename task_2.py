from random import randint



def how_many_candys(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x



player_1 = input("Имя первого игрока: ")
player_2 = input("Имя второго игрока: ")
value_candys = int(input("Сколько всего конфет будет на столе: "))
move = randint(0,2)
if move :
    print (f"Первым ходит игрок: {player_1}")
else:
    print(f"Первым ходит игрок: {player_2}")


while value_candys >= 28:
    if move: 
        value_candys -= how_many_candys(player_1)
        move = False
        print(f"На столе осталось: {value_candys} конфет")
    else:
        
        value_candys -= how_many_candys(player_2)
        move = True
        print(f"На столе осталось: {value_candys} конфет")

if value_candys:
    print(f"Выиграл игрок: {player_1}")
else:
    print(f"Выиграл игрок: {player_2}")