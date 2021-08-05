# SquareCircle - нарисовали круги по спирали спомощью черепашки (цветные)
import turtle
colors = ['blue', 'red', 'yellow', 'green', 'Pink']
t = turtle.Pen() # всроиный модуль turtle
for x  in range(360):
    turtle.bgcolor (colors[x%4])
   # t.pencolor(colors[x%5])
   # t.circle(x)
   # t.left(90)
print ()