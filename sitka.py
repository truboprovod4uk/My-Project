#дана програма рисує координатну сітку, та трубу в розрізі
from tkinter import *

#зміщення полота Canvas та усього що на ньому відображено на величини dx та dy
dx=30
dy=30

HEIGHT = 800 # довжина осі X
WIDTH = 800 # довжина осі Y

#створюємо батьківське вікно, та задаєм його параметри
root = Tk()
root.title("create circle")
root.geometry('1200x850')
root.resizable(False,False)


canvas = Canvas(root, width=WIDTH+50, height=HEIGHT+50, bg='gray')
canvas.pack(side='right')

#ця функція прорисовує координатну сітку, зі стрілками, та розмітками
def sitka(WIDTH, HEIGHT, dx,dy):
#лінії сітки по вертикалі
    for y in range (WIDTH//50+1):
        canvas.create_line(y*50+dx, dy, y*50+dx, HEIGHT+dy)

#лінії сітки по горизонталі
    for x in range (HEIGHT//50+1):
        canvas.create_line(dx, x*50+dy, WIDTH+dx, x*50+dy)

#лінії координат x та y, та їх значення
#стрілка осі Х
    canvas.create_line(dx,dy,WIDTH+dx,dy,width=2, arrow=LAST)
    canvas.create_text(WIDTH+dx-20,10+dy, text='X') #маркування осі Х
#розмітка по осі Х
    for y in range (1,WIDTH//50+1):
        canvas.create_text(y*50+dx, dy-10, text=y*50)

#стрілка осі У
    canvas.create_line(dx,dy,dx,HEIGHT+dy,width=2, arrow=LAST)
    canvas.create_text(10+dx,HEIGHT+dy-20, text='Y')#маркування осі У
#розмітка по осі Y
    for x in range (1,HEIGHT//2+1):
        canvas.create_text(dx-10, x*50+dy, text=x*50)

#стрілка осі У
    canvas.create_text(dx-10,dy-10, text='0')


#ця функція рисує січення труби та ізоляції
def circ(X,Y,DN,dx,dy,s,si):
    '''global c1,c2,c3
    c1,c2,c3 = 0,0,0'''
    c = canvas.create_oval(X-DN/2+dx,Y-DN/2+dy,X+DN/2+dx,Y+DN/2+dy, width=2)
    c = canvas.create_oval(X-DN/2+dx-si,Y-DN/2+dy-si,X+DN/2+dx+si,Y+DN/2+dy+si, width=1)
    c = canvas.create_oval(X-DN/2+dx+s,Y-DN/2+dy+s,X+DN/2+dx-s,Y+DN/2+dy-s, width=1)

def clean():
    canvas.delete('all')

#Лейбли віконечок
label_X = Label(root, text='X')
label_X.place(x=0,y=10)
label_Y = Label(root, text='Y')
label_Y.place(x=0,y=30)
label_DN = Label(root, text='DN')
label_DN.place(x=0,y=50)
label_s = Label(root, text='s, товщ')
label_s.place(x=0,y=70)
label_s = Label(root, text='товщ. ізол')
label_s.place(x=0,y=90)

#поля для введення даних
entry_X = Entry(root)               #тут задаємо координату центру труби по Х
entry_X.place(x=70,y=10,width=50)
entry_Y = Entry(root)               #тут задаємо координату центру труби по Y
entry_Y.place(x=70,y=30,width=50)
entry_DN = Entry(root)              #поле для введення зовнішнього діаметра труби, DN
entry_DN.place(x=70,y=50,width=50)
entry_s = Entry(root)               #поле для введення товщини стінки труби, s
entry_s.place(x=70,y=70,width=50)
entry_si = Entry(root)              #поле для введення товщини ізоляції труби, si
entry_si.place(x=70,y=90,width=50)

#ця кнопка запускає функцію circ, що рисує січення труби та ізоляції
btn_calc = Button(root, text='calc')
btn_calc.bind('<Button-1>',lambda  event: circ(int(entry_X.get()),
                                               int(entry_Y.get()),
                                               int(entry_DN.get()),
                                               dx,dy,
                                               int(entry_s.get()),
                                               int(entry_si.get()),
                                               ))
btn_calc.place(x=150,y=10,width=35)


btn_sitka=Button(root,text='sitka')
btn_sitka.bind('<Button-1>',lambda event: sitka(WIDTH, HEIGHT, dx, dy))
btn_sitka.place(x=150, y=40, width=35)

btn_clean = Button(root, text='clean')
btn_clean.bind('<Button-1>', lambda event: clean())
btn_clean.place(x=150,y=70, width=35)

root.mainloop()