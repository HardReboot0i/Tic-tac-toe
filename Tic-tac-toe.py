pole = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


# Поле
def show():
    print("   | 0 | 1 | 2 |")
    print("----------------")
    for i, row in enumerate(pole):
        s_row = str(i) + " | " + " | ".join(row) + " |"
        print(" " + s_row + "\n----------------")


print('Здравствуйте! Добро пожаловать в игру "Крестики-нолики"!')
show()


# Отлавливание ошибок с вводом координат
def dec_try_inp(fninp_):
    def wrap(*args):
        result = fninp_(*args)
        count = 0
        while True:
            if count >= 1:
                result = input("Повторите ввод координат: ")
            count += 1
            if len(result) != 2:
                print("Введите 2 цифры.\n"
                      "----------------------------")
                continue
            x, y = result
            if not (x.isdigit()) or not (y.isdigit()):
                print("Введите только цифры.\n"
                      "----------------------------")
                continue
            x, y = int(x), int(y)
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("Клетка вне диапозона.\n"
                      "----------------------------")
                continue
            if pole[x][y] != " ":
                print("Клетка занята.\n"
                      "----------------------------")
                continue
            return x, y

    return wrap


# Ввод координат
@dec_try_inp
def input_0(step_):
    if step_ == 1:
        input_ = input("Вы играете за крестики! Ваш ход первый.\n"
                       "Введите координаты X Y, для расположения крестика"
                       "(без пробела): ").replace(" ", "")
        return input_
    elif step_ == 2:
        input_ = input("Вы играете за нолики. Ваш ход.\n"
                       "Введите координаты X Y, для расположения нолика"
                       "(без пробела): ").replace(" ", "")
        return input_
    elif step_ % 2 != 0:
        input_ = input("Крестики, Ваш ход!\nКоординаты: ")
        return input_
    elif step_ % 2 == 0:
        input_ = input("Нолики, Ваш ход!\nКоординаты: ")
        return input_


# Вывод полученных координат на поле
def output(out_):
    global pole
    global step
    x = out_[0]
    y = out_[1]
    if step % 2 == 0:
        pole[x][y] = "O"
        return pole
    elif step % 2 != 0:
        pole[x][y] = "X"
        return pole


# Проверка на победителя
def win():
    comb_chek = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                 ((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)))
    for comb in comb_chek:
        check_win = []
        for a in comb:
            check_win.append(pole[a[0]][a[1]])
        if check_win == ["X", "X", "X"]:
            return 1
        if check_win == ["O", "O", "O"]:
            return 2
    return False


# Конец игры/начало новой игры
def exit_game(num):
    if num == 1:
        cycle = input("Конец игры.\n\n"
                      "Введите \"Да\", если ещё хотите поиграть.\n"
                      "Другой ввод закончит игру.\n"
                      "--------------------\n"
                      "Ваш выбор - ")
        cycle = cycle.lower()
        if cycle != "да":
            print("нет. Спасибо за игру, всего доброго)")
            return 0
        elif cycle == "да":
            return 1
    elif num == 2:
        cycle = input("Поле зополнилось - ничья!\n"
                      "Конец игры.\n\n"
                      "Введите \"Да\", если ещё хотите поиграть.\n"
                      "Другой ввод закончит игру.\n"
                      "--------------------\n"
                      "Ваш выбор - ")
        cycle = cycle.lower()
        if cycle != "да":
            print("Спасибо за игру, всего доброго)")
            return 0
        elif cycle == "да":
            return 1


step = 0

#  Запуск игры
while True:
    step += 1

    # Проверка на заполнение поля = "Ничья"
    if step == 10:
        eg = exit_game(2)
        if not eg:
            break
        elif eg:
            step = 0
            pole = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
            print("--------------")

    inp = input_0(step)
    out = output(inp)
    show()
    w = win()

    if w == 1:
        print("Крестики победили!!!\n"
              "--------------------")
        eg = exit_game(1)
        if not eg:
            break
        elif eg:
            step = 0
            pole = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
            print("--------------")

    elif w == 2:
        print("Нолики победили!!!\n"
              "------------------")
        eg = exit_game(1)
        if not eg:
            break
        elif eg:
            step = 0
            pole = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
            print("--------------")
