# ИСПРАВЛЯЕМ ПРАВУЮ КНОПКУ И ДОБАВЛЯЕМ ФУНКЦИЮ

import random
from tkinter import *  # библиотека Ткинтер
import os
import sys

# Основное окно
window = Tk()
window.title("КуБиКи 1.4")  # название окна
window.config(background="black")  # фон
# window.iconbitmap(default="favicon.ico")  # установка иконки в Виндовс
window.iconbitmap('@favicon.xbm')  # для линукс!
window.geometry('600x420')

label = Label(text="Let's play my game!")  # создаем текстовую метку
label.pack()  # размещаем метку в окне

# добавляю код из файла рандом 1.2
PHOTO_COUNTER = 0

print('PHOTO_COUNTER = ', PHOTO_COUNTER)

photo_list = [
    PhotoImage(file="image/kubik1.png"),
    PhotoImage(file="image/kubik2.png"),
    PhotoImage(file="image/kubik3.png"),
    PhotoImage(file="image/kubik4.png"),
    PhotoImage(file="image/kubik5.png"),
    PhotoImage(file="image/kubik6.png")
]


# Здесь описываются функции
count_player1 = 0  # количество очков 1 игрок
counter1 = 0
def _on_click_kubikleft(button):
    global counter1
    if counter1 <= 10:
       counter1 += 1
       print('counter1 = ', counter1)
       global count_player1
       PHOTO_COUNTER1 = random.randint(0, 5)  # функция с рандомом
       print('PHOTO_COUNTER1 = ', PHOTO_COUNTER1)
       button.config(image=photo_list[PHOTO_COUNTER1])
       count_player1 = count_player1 + PHOTO_COUNTER1 + 1
       print('count_player1 = ', count_player1)
       playerChoice1['text'] = count_player1
    else:
        print('ходы закончились')
        WinnerLabel['text'] = 'Игрок 1 ходы закончились!'


count_player2 = 0  # количество очков 2 игрок
counter2 = 0
def _on_click_kubikright(button):
    global counter2
    if counter2 <= 10:
       counter2 += 1
       print('counter2 = ', counter2)
       global count_player2
       PHOTO_COUNTER2 = random.randint(0, 5)  # функция с рандомом
       print('PHOTO_COUNTER1 = ', PHOTO_COUNTER2)
       button.config(image=photo_list[PHOTO_COUNTER2])
       count_player2 += (PHOTO_COUNTER2 + 1)
       playerChoice2['text'] = count_player2
    else:
        print('ходы закончились')
        WinnerLabel['text'] = 'Игрок 2 ходы закончились!'


def restart_program():
    # window.destroy() # эта команда закрывает окно
    """Restarts the current program.
    Note: this function does not return. Any cleanup action (like
    saving data) must be done before calling this function."""
    python = sys.executable
    os.execl(python, python, * sys.argv)
    # еще можно так os.startfile("main.py")


# Фрейм для группировки кнопок кубиков
middleframe = Frame(window, relief=RAISED, borderwidth=3)
middleframe.config(bg="#333333")  # цвет фона
middleframe.pack(padx=10, pady=10)  # отступы по оси x, y

# Кнопка Кубик Левый
KubikPhoto1 = Button(middleframe, text="ClickMe!", image=photo_list[PHOTO_COUNTER])
KubikPhoto1.config(command=lambda: _on_click_kubikleft(KubikPhoto1))
KubikPhoto1.pack(side=LEFT, padx=10, pady=5)
# Кнопка Кубик Правый
KubikPhoto2 = Button(middleframe, text="ClickMe!", image=photo_list[PHOTO_COUNTER])
KubikPhoto2.config(command=lambda: _on_click_kubikright(KubikPhoto2))
KubikPhoto2.pack(side=RIGHT, padx=10, pady=5)


# Добавляю лейбл в подсчет очков
text = Label(window, text = 'Подсчет очков!')  # Текст лейбл и обязательно его упаковать
text.pack(pady=5) # отступы по оси y
labelfont = ('times', 20, 'bold') # шрифт, размер, толщина
text.config(font=labelfont, fg='red', bg='black')  # применим шрифт



# Фрейм для второй группы кнопок - bottomframe
bottomframe = Frame(window, relief=RAISED, borderwidth=3)
# bottomframe.config(bg="#666666") # цвет фона
bottomframe.pack(padx=10, pady=10) # оттупы по оси x, y

# Лейбл Выбор Игрока
playerLabel = Label(bottomframe, text = ' Игрок1 ') # Текст лейбл и обязательно его упаковать
playerLabelfont = ('times', 15, 'bold') # шрифт, размер, толщина
playerLabel.config(font=playerLabelfont) # применим шрифт
playerLabel.pack(side=LEFT, padx=5, pady=5) # выравнивание и отступы

# Statusbar Что выбрали игроки.
playerChoice1 = Label(bottomframe, text='Welcome to Game!', width = 20, relief = SUNKEN, anchor = S) # рельеф-вдаленная надпись, W=west, S=south
playerChoice1.pack(side=LEFT, fill=X) # прижать к низу, и растянуть по оси Х

playerChoice2 = Label(bottomframe, text='Welcome to Game!', width = 20, relief = SUNKEN, anchor = S) # рельеф-вдаленная надпись, S=South
playerChoice2.pack(side=LEFT, fill=X) # прижать к низу, и растянуть по оси Х

# Лейбл Выбор Компа
compLabel = Label(bottomframe, text = ' Игрок2 ') # Текст лейбл и обязательно его упаковать
compLabel.config(font=playerLabelfont) # применим шрифт тот же, что и у игрока
compLabel.pack(side=LEFT, padx=5, pady=5) # выравнивание и отступы


# Вывод Победителя
WinnerLabel = Label(window, text = 'Press!', width = 30) # Текст лейбл и обязательно его упаковать
WinnerLabelfont = ('times', 20, 'bold') # шрифт, размер, толщина
WinnerLabel.config(bg='black', fg='yellow') # Цвет и фон
WinnerLabel.config(font=WinnerLabelfont) # применим шрифт
WinnerLabel.pack(padx=5, pady=5) # выравнивание и отступы


Button(window, text="Restart", command=restart_program).pack()

# основной цикл
window.mainloop()
