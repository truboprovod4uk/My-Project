#рисує коло по точках
import math
from tkinter import *

root = Tk()
root.title("PythonicWay Pong")

# встановлюєм канву
c = Canvas(root, width=400, height=400)
c.pack()

# радіус кола
r = 120
# створюєм пустий лист для запису в нього точок, по яких побудується нижня частина кола
circl1 = []
# створюєм пустий лист для запису в нього точок, по яких побудується верхня частина кола
circl2 = []
#створюєм змінну яка ставить центр кола в задані координати, якщо цього не зробити то коло побудується в 0б0 координатах
shift=200

#в цьому циклі розраховуються та записуються в масив координати для побудови нижньої частини кола
for x in range(-r,r+1):
  y =  math.sqrt((r**2)-x**2)
  circl1.append(x+shift)
  circl1.append(y+shift)

#в цьому циклі розраховуються та записуються в масив координати для побудови верхньої частини кола
for x in range(-r,r+1):
  y =  math.sqrt((r**2)-x**2)
  circl2.append(x+shift)
  circl2.append(-y+shift)

#будуємо дві половинки кола за допомогою методу create_line, та масиву точок
colo1 = c.create_line(circl1, width=3)
colo2 = c.create_line(circl2, width=3)
root.mainloop()