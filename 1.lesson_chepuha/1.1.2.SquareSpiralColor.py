# SquareSpiral - Разноцветная спираль, цвет берется из списка
import turtle
sides = eval (input ('Введите количество сторон от 2 до 8: '))
colors = ['blue', 'red', 'yellow', 'green', 'Pink','orange', 'yellow', 'green']
t = turtle.Pen() # всроиный модуль turtle
for x  in range(360):
    turtle.bgcolor ("black")
    t.pencolor(colors[x%sides])
    t.forward(x * 3/sides+x)
    t.left(360/sides+1)
    t.width (x * sides/200)8