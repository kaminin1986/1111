# SquareSpiral - Разноцветная спираль, цвет берется из списка
import turtle
colors = ['blue', 'red', 'yellow', 'green', 'Pink']
t = turtle.Pen() # всроиный модуль turtle
for x  in range(360):
    turtle.bgcolor ("green")
    t.pencolor(colors[x%5])
    t.forward(x+50)
    t.left(90)

