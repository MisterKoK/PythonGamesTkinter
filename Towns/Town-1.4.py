from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Города 1.4")  # название окна
root.geometry('500x350')

canvas = Canvas(root, width=800, height=500)
canvas.pack()


def load_image(name):
    img = Image.open(name)
    #   img.thumbnail((200, 200), Image.Resampling.LANCZOS)
    img = img.resize((250, 250), Image.Resampling.LANCZOS)
    #  img.thumbnail((200, 200), Image.ANTIALIAS)
    return ImageTk.PhotoImage(img)

def set_image(image):
    canvas.delete("all")
    canvas.create_image(100, 115, image=image)  # Размер фотки в окне

image1 = load_image("images/Chehov.png")
image2 = load_image("images/Serpuhov.png")
image3 = load_image("images/Pushino.png")
image4 = load_image("images/Podolsk.png")

# set_image(image)

def cheh():
    t1['text'] = "Город Чехов был так назван \nв честь писателя \nАнтона Павловича Чехова."
    set_image(image1)
def serp():
    t1['text'] = "Город Серпухов назван так \nпотому, что река Серпейка \nсерпообразно огибала \nСоборную (Красную) гору"
    set_image(image2)
def push():
    t1['text'] = "Город получил название \nот деревни Пущино, \nкоторая находится на его \nсеверо-западной окраине."
    set_image(image3)
def pod():
    t1['text'] = "По легенде императрица \nЕкатерина II, проезжая через \nсело, случайно намочила \nподол своего платья."
    set_image(image4)

t1 = Label(root, font='Georgia')
t1.place(x=250, y=50)

'''
t2 = Label(root, text="Описание 2")
t2.place(x=250, y=100)

t3 = Label(root, text="Описание 3")
t3.place(x=250, y=150)
'''

btn1 = Button(root, text="Чехов", width=25, command=cheh)
btn1.place(x=25, y=260)

btn2 = Button(root, text="Серпухов", width=25, command=serp)
btn2.place(x=240, y=260)

btn3 = Button(root, text="Пущино", width=25, command=push)
btn3.place(x=25, y=300)

btn4 = Button(root, text="Подольск", width=25, command=pod)
btn4.place(x=240, y=300)

root.mainloop()
