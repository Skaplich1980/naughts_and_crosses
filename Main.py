# игра крестики-нолики

# хранение игрового поля в списке, где хранятся строки игрового поля в виде списков
# P[ [], [], [] ]

import random

# программа написана с учетом возможности доработки игры для любого игрового поля, свыше размера 3 на 3

# размер матрицы игрового поля Column=String
Psize = 3
Mark = 0
choice = 0
move_count = 0  # всего шагов Psize*Psize


# заполнение матрицы игрового поля пустыми значениями


# вывод игрового поля
def ShowP():
    global Psize
    global P
    # вывод кол-ва столбцов
    s = ''
    for i in range(Psize):
        # печать верхней строки
        s += '   ' + str(i + 1)
    print(s)
    s_separator = '--'  # создаем строку разделитель по нужной длине
    for i in range(Psize):
        s_separator += '----'
    print(s_separator)
    for i in range(Psize):  # перебираем строки
        s = str(i + 1)
        for j in range(Psize):
            if P[i][j] is not None:  # есть значение
                if P[i][j] == 0:
                    s += '| O '
                elif P[i][j] == 1:
                    s += '| X '
            else:
                s += '|   '
        print(s + '|')
    print('')


# приветствие
def Hi():
    global Psize
    print('')
    print('Привет, это игра крестики-нолики')
    print('x- номер строки, y - номер столбца')
    print(f'Выбрано поле для игры {Psize}x{Psize}')
    print('Крестики ходят первыми!')


# ход игрока
def move_user():
    global Psize
    global P
    global choice
    global move_count
    print('Ход игрока:')
    while True:
        while True:
            try:
                x = int(input(f'Введите номер строки x (от 1 до {Psize}):'))
                if 0 < x <= Psize:
                    break
                else:
                    print('Вы ввели значение не в разрешенном диапазоне, попробуйте еще раз.')
            except ValueError:
                print('Вы ввели значение неверное значение, попробуйте еще раз.')
        while True:
            try:
                y = int(input(f'Введите номер столбца y (от 1 до {Psize}):'))
                if 0 < y <= Psize:
                    break
                else:
                    print('Вы ввели значение не в разрешенном диапазоне, попробуйте еще раз.')
            except ValueError:
                print('Вы ввели значение неверное значение, попробуйте еще раз.')

        if P[x - 1][y - 1] is not None:
            print(f'Поле {x - 1},{y - 1} занято, попробуйте еще раз')
        else:
            P[x - 1][y - 1] = choice
            break
    move_count+=1
    ShowP()

# ход компа
def move_comp_random():
    global Psize
    global P
    global choice
    global move_count
    # комп ходит произвольно
    #print('Ход компьютера произвольно:')
    #первый ход в центр делаем
    if move_count==0:
        P[1][1] = (choice + 1) % 2
    elif move_count==1 and P[1][1] is None:
        P[1][1] = (choice + 1) % 2
    else:
        while True:
            x = random.randint(0, Psize - 1)
            y = random.randint(0, Psize - 1)
            if P[x][y] is None:
                P[x][y] = (choice + 1) % 2  # проставляем крестик или нолик, смотря что выбрал пользователь
                break
    move_count += 1
    ShowP()

# комп ходит более умно
def move_comp():
    global Psize
    global P
    global choice
    global move_count
    old_move_count=move_count
    #print('Ход компьютера обдуманно:')
    # стратегия
    # если ноликом играем, тогда ходим в любой угол, когда занят центр
    # если крестиком играем, то ходим в центр обязательно на 1 ходу
    if move_count==0 and choice==0: # 1 ход и играем крестиками
        P[1][1]=1 # ходим в центр
        move_count += 1
    #Правило 1. Если игрок может немедленно выиграть, он это делает.
    # elif :
    #     # рассматриваем выигрышные варианты
    #     if choice==0:
    #         # диагонали
    #         if P[0][0] == 0 and P[1][1] == 0 and (P[2][2] is None):
    #             P[2][2] = 0
    #         if P[0][0] == 0 and P[1][1] == 0 and (P[2][2] is None):
    #             P[2][2] = 0
    #
    #         ...
    #
    #         # горизонтальные линии
    #         if P[0][0] == 0 and P[0][1] == 0 and (P[0][2] is None):
    #             P[0][2]=0
    #         if P[1][0] == 0 and P[1][1] == 0 and (P[1][2] is None):
    #             P[1][2]=0
    #         if P[2][0] == 0 and P[2][1] == 0 and (P[2][2] is None):
    #             P[1][2]=0
    #         ...
    #     if choice == 1:
    #         ...
    #Правило 2. Если игрок не может немедленно выиграть, но его противник мог бы немедленно выиграть,
    #  сделав ход в какую-то клетку, игрок сам делает ход в эту клетку, предотвращая немедленный проигрыш.

    #if move_count==old_move_count:
    # в коде выше не произошло хода
        # ходим произвольно
        #move_comp_random():
    #else:ShowP()
    ...
    ShowP()

# проверка выигрышной ситуации
def check_win():
    global Psize
    global P
    global move_count
    # return None - никто не выиграл - ничья
    # return 1 - крестики
    # return 0 - нолики
    if Psize == 3:  # поиск выигрыша для стандартного поля 3 на 3
        # любая линия заполнена 0 или 1 или диагональ
        # рассмотрим диагонали
        if P[0][0] == 0 and P[1][1] == 0 and P[2][2] == 0:
            return 0
        if P[0][0] == 1 and P[1][1] == 1 and P[2][2] == 1:
            return 1
        if P[0][2] == 0 and P[1][1] == 0 and P[2][0] == 0:
            return 0
        if P[0][2] == 1 and P[1][1] == 1 and P[2][0] == 1:
            return 1
        for i in range(2):
            # построчно
            if P[i][0] == 0 and P[i][1] == 0 and P[i][2] == 0:
                return 0
            # по столбцам
            if P[0][i] == 0 and P[1][i] == 0 and P[2][i] == 0:
                return 0
            # построчно
            if P[i][0] == 1 and P[i][1] == 1 and P[i][2] == 1:
                return 1
            # по столбцам
            if P[0][i] == 1 and P[1][i] == 1 and P[2][i] == 1:
                return 1
        return None # нет выигрышной комбинации
    else:
        ...  # общий алгоритм поиска выигрыша для любого поля

# отображение сообщений о победе
def show_win(s):
    global Psize
    global move_coun
    global move_count
    if s is not None:
        move_count = Psize * Psize
        if s==0: # выиграли нолики
            print('');
            print('Выиграли нолики');
            if not choice:
                print('Поздравляем вас с победой!')
        else:# выиграли крестики
            print('');
            print('Выиграли крестики');
            if choice:
                print('Поздравляем вас с победой!')


# играем
P = [[None] * Psize for i in range(Psize)]  # заполнение матрицы (выбранного размера) пустыми значениями
print(P)
Hi()  # приветствие
ShowP()  # отображение пустого поля игры для визуальности игроку
try:
    choice = int(input('Если будете играть ноликами введите 0, если крестиками 1:'))
except ValueError:
    choice = 1
if choice != 0: # на всякий случай, если не ноль, то
    choice = 1

if choice==1:
    print('Игрок играет крестиками, компьютер ноликами')
else:
    print('Игрок играет ноликами, компьютер крестиками')
while move_count<Psize*Psize:
    if move_count==0 and choice == 1:  # первый ходит крестик, игрок на 1 ходу
        move_user()

    if move_count!=Psize * Psize:
        move_comp_random()
        show_win(check_win())
    if move_count!=Psize * Psize:
        move_user()
        show_win(check_win())
    if move_count==Psize * Psize: # конец игры
        s = input('Хотите еще раз сыграть(Y/N)?')
        if s.upper()=='Y':
            move_count = 0
            print('')
            print('НОВАЯ ИГРА')
            P = [[None] * Psize for i in range(Psize)] # очистка игрового поля
            choice=(choice + 1) % 2 # меняем местами, кто чем играет !
            if choice == 1:
                print('Игрок играет крестиками, компьютер ноликами')
            else:
                print('Игрок играет ноликами, компьютер крестиками')
            ShowP()

