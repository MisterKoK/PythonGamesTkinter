# Rock Scissors Paper with GUI
# Добавляем Менюшку Файл.
from tkinter import*
from tkinter import messagebox
from random import*

k = 0   # переменные для счетчика
p = 0

root = Tk()

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

def about_us():
    messagebox.showinfo('Правила игры:','Выбирайте иконку камня, ножниц или бумаги'
                                                    ' https://vk.com/misterkok') # мессаджбокс
# Create the submenu
subMenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label="File",menu=subMenu)
subMenu.add_command(label="Help", command = about_us)
subMenu.add_command(label="Exit", command = root.destroy)


def stone():
    playerChoice['text'] = "Камень"
    global theFirst # объявим глобальную переменную
    theFirst = 'rock'
    randomComp()
def scissors():
    playerChoice['text'] = "Ножницы"
    global theFirst # объявим глобальную переменную
    theFirst = 'scissors'
    randomComp()
def paper():
    playerChoice['text'] = "Бумага"
    global theFirst # объявим глобальную переменную
    theFirst = 'paper'
    randomComp()

# команда для рандомного выбора компом
def randomComp():
    rps = 'rock', 'paper', 'scissors'
    theSecond = choice(rps) # внимательно random.choice(rps)
    if theSecond == 'rock': # Заменим английские слова на русский вывод в виджете
        compChoice['text'] = "Камень"
    elif theSecond == 'paper':
        compChoice['text'] = "Бумага"
    elif theSecond == 'scissors':
        compChoice['text'] = "Ножницы"

    # вызываем функцию победителя и заполняем виджет кто победил
    WinnerLabel['text'] = whoWin(theFirst, theSecond)

    print('Комп выбрал ', theSecond)
    print('Игрок выбрал', theFirst)
    # print((whoWin(theFirst, theSecond)),'\n') # убираем, чтобы не вызывать два раза фунцию

# определяем победителя
def whoWin(theFirst, theSecond):
    rps = 'rock', 'paper', 'scissors'
    if rps.index(theFirst) == rps.index(theSecond):
        return 'Draw!'
    elif (rps.index(theSecond) - rps.index(theFirst)) % 3 == 1:
        global p # счетчик побед игрока
        p+=1
        playerPoint['text'] = p
        return 'You Win!'
    else:
        global k
        k+=1
        compPoint['text'] = k
        return 'Comp Win!'


def count():
    pass



root.title("Камень-Ножницы-Бумага") # название окна
root.iconbitmap(r'icon/b2.ico') # подключаем иконку для окна

# Приветтвенный текст-лейбл вверху окна
text = Label(root, text = 'Lets play some game!') # Текст лейбл и обязательно его упаковать
text.pack(pady=5) # отступы по оси y
labelfont = ('times', 20, 'bold') # шрифт, размер, толщина
text.config(font=labelfont) # применим шрифт

# Фрейм для группировки кнопок
middleframe = Frame(root, relief=RAISED, borderwidth=3)
middleframe.config(bg="#666666") # цвет фона
middleframe.pack(padx=10, pady=10) # оттупы по оси x, y

# Кнопка Камень
stonePhoto = PhotoImage(file='icon/k.png')
stoneBtn = Button(middleframe, image = stonePhoto, command = stone) # кнопка уже с картинкой и командой
stoneBtn.pack(side=LEFT, padx=5, pady=5)

# Кнопка Ножницы
scissorsPhoto = PhotoImage(file='icon/n.png')
scissorsBtn = Button(middleframe, image = scissorsPhoto, command = scissors) # кнопка уже с картинкой и командой
scissorsBtn.pack(side=LEFT, padx=5, pady=5)

# Кнопка Бумага
paperPhoto = PhotoImage(file='icon/b.png') # описываем кнопку бумага
paperBtn = Button(middleframe, image = paperPhoto, command = paper) # кнопка уже с картинкой и командой
paperBtn.pack(side=LEFT, padx=5, pady=5)


# Фрейм для второй группы кнопок - bottomframe
bottomframe = Frame(root, relief=RAISED, borderwidth=3)
# bottomframe.config(bg="#666666") # цвет фона
bottomframe.pack(padx=10, pady=10) # оттупы по оси x, y

# Лейбл Выбор Игрока
playerLabel = Label(bottomframe, text = 'Выбор Игрока:') # Текст лейбл и обязательно его упаковать
playerLabelfont = ('times', 15, 'bold') # шрифт, размер, толщина
playerLabel.config(font=playerLabelfont) # применим шрифт
playerLabel.pack(side=LEFT, padx=5, pady=5) # выравнивание и отступы

# Statusbar Что выбрали игроки.
playerChoice = Label(bottomframe, text='Welcome to Game!', width = 20, relief = SUNKEN, anchor = S) # рельеф-вдаленная надпись, W=west, S=south
playerChoice.pack(side=LEFT, fill=X) # прижать к низу, и растянуть по оси Х

compChoice = Label(bottomframe, text='Welcome to Game!', width = 20, relief = SUNKEN, anchor = S) # рельеф-вдаленная надпись, S=South
compChoice.pack(side=LEFT, fill=X) # прижать к низу, и растянуть по оси Х

# Лейбл Выбор Компа
compLabel = Label(bottomframe, text = ':Выбор Компьютера') # Текст лейбл и обязательно его упаковать
compLabel.config(font=playerLabelfont) # применим шрифт тот же, что и у игрока
compLabel.pack(side=LEFT, padx=5, pady=5) # выравнивание и отступы


# Вывод Победителя
WinnerLabel = Label(root, text = 'Press!', width = 20) # Текст лейбл и обязательно его упаковать
WinnerLabelfont = ('times', 20, 'bold') # шрифт, размер, толщина
WinnerLabel.config(bg='black', fg='yellow') # Цвет и фон
WinnerLabel.config(font=WinnerLabelfont) # применим шрифт
WinnerLabel.pack(padx=5, pady=5) # выравнивание и отступы


# Фрейм для Третьей группы кнопок Подсчет Очков - bottomframe3
bottomframe3 = Frame(root, relief=RAISED , borderwidth=3) #
bottomframe3.pack(side=BOTTOM, padx=10, pady=10) # оттупы по оси x, y

playerLabelPoint = Label(bottomframe3, text = 'Очки Игрок', width = 20, relief = SUNKEN) # Текст лейбл и обязательно его упаковать
playerLabelPoint.pack(side=LEFT, fill=X) # выравнивание и отступы

# Счет игрока
playerPoint = Label(bottomframe3, text='0', width = 10, relief = SUNKEN) # рельеф-вдаленная надпись, W=west
playerPoint.pack(side=LEFT, fill=X) # прижать к низу, и растянуть по оси Х
# Счет компа
compPoint = Label(bottomframe3, text='0', width = 10, relief = SUNKEN) # рельеф-вдаленная надпись, W=west
compPoint.pack(side=LEFT, fill=X) # прижать к низу, и растянуть по оси Х

compLabelPoint = Label(bottomframe3, text = 'Очки Компьютер', width = 20, relief = SUNKEN) # Текст лейбл и обязательно его упаковать
compLabelPoint.pack(side=LEFT, fill=X) # выравнивание и отступы

root.mainloop()
