#print("DZ Problem")
#problem = input("Введите задачу или 'q', чтобы выйти: ")
#while (problem! = "q" ):
#    print ("Ответ на ", problem, " - это ", eval (problem))
#    problem = input("Введите ещё одну задачу или 'q', чтобы выйти: ")# SquareCircle - нарисовали круги по спирали спомощью черепашки (цветные)
#colors = ['blue', 'red', 'yellow', 'green', 'Pink','orange', 'yellow', 'green']
# SquareSpiral - Разноцветная спираль, цвет берется из списка
#turtle.bgcolor ("black")
    #t.pencolor(colors[x%sides])

import turtle
sides = eval (input ('Введите количество сторон от 2 до 8: '))
t = turtle.Pen() # всроиный модуль turtle
for x  in range(sides):
    t.circle(60) # всроиный модуль turtle
    t.forward(x * 3/sides+x)
    t.left(360/sides+1)
    t.width (x * sides/200)