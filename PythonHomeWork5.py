
# Задача 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?


# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет от 1 до 28, которое возьмете: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Игрок {name} сделал ход, взял {k} конфет, теперь у него {counter} конфет. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))

# # очередность
# flag = randint(0,2)

# if flag:
#     print(f"Первым ходит игрок {player1}")
# else:
#     print(f"Первым ходит игрок {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл игрок {player1}")
# else:
#     print(f"Выиграл игрок {player2}")



# a) Добавьте игру против бота

# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет от 1 до 28, которое возьмете: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x

# def p_print(name, k, counter, value):
#     print(f"Игрок {name} сделал ход, взял {k} конфет, теперь у него {counter} конфет. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))

# очередность
# flag = randint(0,2) 
# if flag:
#     print(f"Первым ходит {player1}")
# else:
#     print(f"Первым ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = randint(1,28)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл игрок {player1}")
# else:
#     print(f"Выиграл игрок {player2}")


# b) * Подумайте как наделить бота ""интеллектом""

# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет от 1 до 28, которое возьмете: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x

# def p_print(name, k, counter, value):
#     print(f"Игрок {name} сделал ход, взял {k} конфет, теперь у него {counter} конфет. Осталось на столе {value} конфет.")

# def bot_calc(value):
#     k = randint(1,28)
#     while value-k <= 28 and value > 29:
#         k = randint(1,28)
#     return k

# player1 = input("Введите имя первого игрока: ")
# player2 = "Bot"
# value = int(input("Введите количество конфет на столе: "))

# flag = randint(0,2) 
# if flag:
#     print(f"Первым ходит {player1}")
# else:
#     print(f"Первым ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = bot_calc(value)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)


# if flag:
#     print(f"Выиграл игрок {player1}")
# else:
#     print(f"Выиграл игрок {player2}")



# Задача 2. Создайте программу для игры в ""Крестики-нолики"".

# Инициализация карты
maps = [1,2,3,
        4,5,6,
        7,8,9]
 
# Инициализация победных линий
victories = [[0,1,2],
             [3,4,5],
             [6,7,8],
             [0,3,6],
             [1,4,7],
             [2,5,8],
             [0,4,8],
             [2,4,6]]
 
# Вывод карты на экран
def print_maps():
    print(maps[0], end = " ")
    print(maps[1], end = " ")
    print(maps[2])
 
    print(maps[3], end = " ")
    print(maps[4], end = " ")
    print(maps[5])
 
    print(maps[6], end = " ")
    print(maps[7], end = " ")
    print(maps[8])    
 
# Сделать ход в ячейку
def step_maps(step,symbol):
    ind = maps.index(step)
    maps[ind] = symbol
 
# Получить текущий результат игры
def get_result():
    win = ""
 
    for i in victories:
        if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
            win = "X"
        if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
            win = "O"   
    
    return win
 
# Основная программа
game_over = False
player1 = True
 
while game_over == False:
 
    # 1. Показываем карту
    print_maps()
 
    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))
 
    step_maps(step,symbol) # делаем ход в указанную ячейку
    win = get_result() # определим победителя
    if win != "":
        game_over = True
    else:
        game_over = False
 
    player1 = not(player1)        
 
# Игра окончена. Покажем карту. Объявим победителя.        
print_maps()
print("Победил", win)



# Задача 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# Данные в файле RLE input.txt: ggggggggggggggggggmmmmmmmmmmmrrrrrrrrrfllllll

# with open('RLE input.txt', 'r') as data:
#     my_rle_text = data.read()

# def coding(txt):
#     count = 1
#     res = ''
#     for i in range(len(txt)-1):
#         if txt[i] == txt[i+1]:
#             count += 1
#         else:
#             res = res + str(count) + txt[i]
#             count = 1
#     if count > 1 or (txt[len(txt)-2] != txt[-1]):
#         res = res + str(count) + txt[-1]
#     return res

# def decoding(txt):
#     number = ''
#     res = ''
#     for i in range(len(txt)):
#         if not txt[i].isalpha():
#             number += txt[i]
#         else:
#             res = res + txt[i] * int(number)
#             number = ''
#     return res

# print(f"Текст после сжатия данных: {coding(my_rle_text)}")
# print(f"Текст после восстановления данных: {decoding(coding(my_rle_text))}")

# # Записываем в файл RLE output.txt после сжатия: 18g11m9r1f6l
# with open('RLE output.txt', 'w') as data2:
#     data2.write(coding(my_rle_text))  

