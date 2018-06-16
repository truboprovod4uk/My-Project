# Це не мій проект, програма написана по прикладу з ютуба
# Ця програма генерує координатну сітку та синусоїду, приймаючи дані від користувача
from tkinter import *
import math
root = Tk()
root.title("Графік фунції")
root.geometry('1240x640')

canvas = Canvas(root, width=900, height=640, bg='#002')
canvas.pack(side='right')
# лінії сітки по вертикалі
for y in range(21):
    k = 50 * y
    canvas.create_line(10 + k, 610, 10 + k, 10, width=1, fill='#191938')

# лінії сітки по горизонталі
for x in range(13):
    k = 50 * x
    canvas.create_line(10, 10 + k, 1010, 10 + k, width=1, fill='#191938')

# лінії координат x та y
canvas.create_line(10,10,10,610, width=1, arrow=FIRST, fill='white')# вісь Y
canvas.create_line(0,310,1010,310,width=1, arrow=LAST, fill='white')# вісь X

canvas.create_text(10,10,text='300', fill='white')
canvas.create_text(10,610,text='-300', fill='white')
canvas.create_text(10,310,text='0', fill='white')
canvas.create_text(1020,310,text='1000', fill='white')

'''w = 0.0209  #циклічна частота
phi = 10    #зміщення графіка по Х
A = 200     #амплітуда
dy = 310    #зміщення графіка по У'''


label_w = Label(root,text='Циклічна частота:')
label_w.place(x=0,y=10)
label_phi = Label(root,text='Зміщення графіка по Х:')
label_phi.place(x=0,y=30)
label_A = Label(root,text='Aмплітуда:')
label_A.place(x=0,y=50)
label_dy = Label(root,text='Зміщення графіка по У:')
label_dy.place(x=0,y=70)

entry_w = Entry(root)
entry_w.place(x=150,y=10)
entry_phi = Entry(root)
entry_phi.place(x=150,y=30)
entry_A = Entry(root)
entry_A.place(x=150,y=50)
entry_dy = Entry(root)
entry_dy.place(x=150,y=70)

def sinus(w, phi, A, dy):
    global sin
    sin=0
    xy = []
    for x in range(1000):
        y = math.sin(x*w)
        xy.append(x+phi)
        xy.append(y*A+dy)
    sin=canvas.create_line(xy, fill='blue')

def clean():
    canvas.delete(sin)

btn_calc = Button(root, text='calc')
btn_calc.bind('<Button-1>',lambda event:sinus(float(entry_w.get()),
                                              float(entry_phi.get()),
                                              float(entry_A.get()),
                                              float(entry_dy.get())))

btn_calc.place(x=10,y=100)

btn_clean = Button(root, text='clean')
btn_clean.bind('<Button-1>', lambda event: clean())
btn_clean.place(x=100,y=100 )


root.mainloop()
