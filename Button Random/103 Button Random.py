from tkinter import *  # библиотека Ткинтер
import random


def frandom():
    R = random.randint(1, 15)
    inserter(R)
    print(R)


# функция вставки информации
def inserter(value):
    #  output.delete("0.0","end") # стирает поле
    output.insert("0.0", value)  # вводит аргумиент валуе в окно output
    output.insert("0.0", "  ")


root = Tk()
root.title("Рандомайзер от 1 до 15")  # название окна
root.minsize(325, 215)
root.resizable(width=FALSE, height=FALSE)  # запрет на изменение окна

# создаем рабочую область
frame = Frame(root)
frame.grid()

# Кнопка решить
but = Button(frame, text="Мне повезет!", command=frandom).grid(row=1, column=4, padx=(10, 0))

# место вывода решения
output = Text(frame, bg="lightblue", font="Arial 12", width=35, height=10)
output.grid(row=2, columnspan=8)

# запускает окно
root.mainloop()
