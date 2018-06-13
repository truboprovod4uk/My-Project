#рухає кульку по півколу, потребує доробики
#1зробити так щою попередня кулька на кожному кроці стиралась
#2, щоб кулька описувала коло повністю
import math
from tkinter import *

root = Tk()
root.title("PythonicWay Pong")

# встановлюєм канву
c = Canvas(root, width=400, height=400)
c.pack()

# радіус кола
r = 120
# радіус мячика
rc = 3
# створюєм пустий лист для запису в нього точок, по яких побудується нижня частина кола
circl1 = []
# створюєм пустий лист для запису в нього точок, по яких побудується верхня частина кола
circl2 = []
#створюєм змінну яка ставить центр кола в задані координати, якщо цього не зробити то коло побудується в 0б0 координатах
shift=200
x = -30
#в цьому циклі розраховуються та записуються в масив координати для побудови нижньої частини кола
def circle():
    global x,y
    global Ball
    x=x+1
    y =  math.sqrt((r**2)-x**2)
    Ball = c.create_oval(x-rc+shift,y-rc+shift,x+rc+shift,y+rc+shift, fill='white')
    y = -math.sqrt((r ** 2) - x ** 2)
    Ball = c.create_oval(x-rc+shift,y-rc+shift,x+rc+shift,y+rc+shift, fill='white')


def main():
    circle()
    root.after(30, main)

main()
root.mainloop()