# програма імітує рух кульки по різних траекторіях
from tkinter import *
import math


# настройки вікна
WIDTH = 600
HEIGHT = 200

# радіус мяча
BALL_RADIUS = 25

# встановлюєм вікно
root = Tk()
root.title("PythonicWay Pong")

# встановлюєм канву
c = Canvas(root, width=WIDTH, height=HEIGHT, background="#003300")
c.pack()

shift = 50
board_top = c.create_line(WIDTH/shift,HEIGHT/shift,WIDTH-WIDTH/shift,HEIGHT/shift, width=2)
board_bot = c.create_line(WIDTH/shift,HEIGHT-HEIGHT/shift,WIDTH-WIDTH/shift,HEIGHT-HEIGHT/shift, width=2)
board_left = c.create_line(WIDTH/shift,HEIGHT/shift,WIDTH/shift,HEIGHT-HEIGHT/shift, width=2)
board_right = c.create_line(WIDTH-WIDTH/shift,HEIGHT/shift,WIDTH-WIDTH/shift,HEIGHT-HEIGHT/shift, width=2)

# створюєм мяч

dy=20
BALL = c.create_oval(WIDTH/2-BALL_RADIUS/2,
                     HEIGHT/2-BALL_RADIUS/2,
                     WIDTH/2+BALL_RADIUS/2,
                     HEIGHT/2+BALL_RADIUS/2, fill="white")

'''BALL2 = c.create_oval(WIDTH/2-BALL_RADIUS/2,
                     HEIGHT/2+dy-BALL_RADIUS/2,
                     WIDTH/2+BALL_RADIUS/2,
                     HEIGHT/2+dy+BALL_RADIUS/2, fill="gray")'''



'''BALL = c.create_oval(50-BALL_RADIUS/2,
                    650-BALL_RADIUS/2,
                     50+BALL_RADIUS/2,
                     650+BALL_RADIUS/2, fill="white")'''



BALL_X_CHANGE = 10
BALL_Y_CHANGE = 0

# Ця функція рухає мячик як білярдну кульку
def move_ball_1():
    global BALL_Y_CHANGE
    global BALL_X_CHANGE
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center_Y = (ball_top + ball_bot) / 2
    ball_center_X = (ball_left + ball_right) / 2
    if ball_center_Y < c.coords(board_top)[1]+BALL_RADIUS/2:
        BALL_Y_CHANGE = -BALL_Y_CHANGE
    elif ball_center_Y > c.coords(board_bot)[1]-BALL_RADIUS/2:
        BALL_Y_CHANGE = -BALL_Y_CHANGE
    elif ball_center_X < c.coords(board_left)[0]+BALL_RADIUS/2:
        BALL_X_CHANGE = -BALL_X_CHANGE
    elif ball_center_X > c.coords(board_right)[0]-BALL_RADIUS/2:
        BALL_X_CHANGE = -BALL_X_CHANGE
    c.move(BALL, BALL_X_CHANGE, BALL_Y_CHANGE)


# Ця функція рухає мячик по периметру
def move_ball_2():
    speed = 3
    BALL_X_CHANGE = 0
    BALL_Y_CHANGE = -speed
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center_Y = (ball_top + ball_bot) / 2
    ball_center_X = (ball_left + ball_right) / 2
    if ball_center_Y < c.coords(board_top)[1]+20:#поворот вправо, біля верхньої границі
        BALL_X_CHANGE = speed
        BALL_Y_CHANGE = 0
    if ball_center_X > (c.coords(board_right)[0]-20):#поворот вниз, біля верхньої границі
        BALL_X_CHANGE = 0
        BALL_Y_CHANGE = speed
    if ball_center_Y > (c.coords(board_bot)[1]-20):#поворот вліво, біля нижньої границі
        BALL_X_CHANGE = -speed
        BALL_Y_CHANGE = 0
        if ball_center_X < (c.coords(board_left)[0]+20):#поворот вверх, біля нижньої границі
            BALL_X_CHANGE = 0
            BALL_Y_CHANGE = -speed

    c.move(BALL, BALL_X_CHANGE, BALL_Y_CHANGE)




# Ця функція рухає мячик по синусоїді
def move_ball_3():
    global BALL_X_CHANGE
    global BALL_Y_CHANGE
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center_Y = (ball_top + ball_bot) / 2
    ball_center_X = (ball_left + ball_right) / 2
    if ball_center_Y < c.coords(board_top)[1]:
        BALL_Y_CHANGE = -BALL_Y_CHANGE
    elif  ball_center_Y > c.coords(board_bot)[1]:
        BALL_Y_CHANGE = -BALL_Y_CHANGE
    elif ball_center_X < c.coords(board_left)[0]:
        BALL_X_CHANGE = -BALL_X_CHANGE
    elif ball_center_X > c.coords(board_right)[0]:
        BALL_X_CHANGE = -BALL_X_CHANGE
    BALL_Y_CHANGE = math.cos(ball_center_X*(-3))*5
    c.move(BALL, BALL_X_CHANGE, BALL_Y_CHANGE)


# Ця функція НЕ рухає мячик по колу
def move_ball_4():
    r = 100
    global BALL_X_CHANGE
    global BALL_Y_CHANGE
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center_Y = (ball_top + ball_bot) / 2
    ball_center_X = (ball_left + ball_right) / 2

    if ball_center_X > (WIDTH/2)+50:
        BALL_X_CHANGE = -BALL_X_CHANGE
    if ball_center_X < (WIDTH/2)-50:
        BALL_X_CHANGE = -BALL_X_CHANGE

    BALL_Y_CHANGE = 400 - math.sqrt(r ** 2 - (ball_center_X-200)** 2)# тут вираховується координата, а треба зсув
    c.move(BALL, BALL_X_CHANGE, BALL_Y_CHANGE)
    print(BALL_Y_CHANGE)


# Ця функція прискорює мячик з кожним відскоком від стінки(тільки по Х), до максимально допустимої швидкості -------
def move_ball_5():
    global BALL_X_CHANGE
    global BALL_Y_CHANGE
    max_spead = 15
    koef = 1.1
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center_Y = (ball_top + ball_bot) / 2
    ball_center_X = (ball_left + ball_right) / 2

    if ball_center_X < c.coords(board_left)[0]+BALL_RADIUS/2:
        if abs(BALL_X_CHANGE) < max_spead:
           BALL_X_CHANGE = -BALL_X_CHANGE*koef
        else:
            BALL_X_CHANGE = -BALL_X_CHANGE
    if ball_center_X > c.coords(board_right)[0]-BALL_RADIUS/2:
        if abs(BALL_X_CHANGE) < max_spead:
           BALL_X_CHANGE = -BALL_X_CHANGE*koef
        else:
            BALL_X_CHANGE = -BALL_X_CHANGE

    c.move(BALL, BALL_X_CHANGE, BALL_Y_CHANGE)
    print(BALL_X_CHANGE)


# Ця функція рухає мячик по Х від стінки до стінки, та сповільнює його рух при наближенні до стінки
def move_ball_6():
    global BALL_X_CHANGE
    global BALL_Y_CHANGE
    ball_left, ball_top, ball_right, ball_bot = c.coords(BALL)
    ball_center_Y = (ball_top + ball_bot) / 2
    ball_center_X = (ball_left + ball_right) / 2

    if ball_center_X > c.coords(board_right)[0]-(WIDTH/4):
        koef = abs(ball_center_X - c.coords(board_right)[0])/(WIDTH/4)
    elif ball_center_X < c.coords(board_left)[0]+(WIDTH/4):
        koef = abs(ball_center_X - c.coords(board_left)[0])/(WIDTH/4)
    else:
        koef=1
        
    if ball_center_X < c.coords(board_left)[0]+BALL_RADIUS/2:
        BALL_X_CHANGE = -BALL_X_CHANGE

    if ball_center_X > c.coords(board_right)[0]-BALL_RADIUS/2:
        BALL_X_CHANGE = -BALL_X_CHANGE

    c.move(BALL, BALL_X_CHANGE*koef, BALL_Y_CHANGE)
    
    print(BALL_X_CHANGE*koef)

    
def main(): 
    move_ball_6() # move_ball_х(), де х траекторія руху кульки, потрібно вручну прописати траекторію
    root.after(30, main)


# запускаємо рух
main()


# запускаємо роботу вікна
root.mainloop()
