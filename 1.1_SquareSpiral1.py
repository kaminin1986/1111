# SquareApiral1.py -рисование квадратной спирали
# https://docs.python.org/3/library/turtle.html?highlight=turtle#module-turtle
import turtle
t = turtle.Pen() # всроиный модуль turtle

for x  in range(100):
    t.forward(x)
    t.left(90)