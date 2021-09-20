#print("DZ Problem")
#problem = input("Введите задачу или 'q', чтобы выйти: ")
#while (problem! = "q" ):
#    print ("Ответ на ", problem, " - это ", eval (problem))
#    problem = input("Введите ещё одну задачу или 'q', чтобы выйти: ")# SquareCircle - нарисовали круги по спирали спомощью черепашки (цветные)

# SquareSpiral - Разноцветная спираль, цвет берется из списка

import turtle # Установка графики Turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green"]
sides = eval (input ('Введите количество сторон от 2 до 8: '))
#Запросить имя пользователя с помощью всплывающего окна
# textinput
i = turtle.textinput("Окно запроса имени", "Как твое имя?")

#нарисовать спираль из имени повторяемого 100 раз
for x in range(100):
    t.circle(x)
    t.pencolor (colors[x%4])#по очереди выбрать 4 цвета
    t.penup() # Не ресовать обычные линии спирали
    t.forward(x*4) # Переместить черепашку по экрану
    t.pendown()
    #t.write(i, font= ("Arial", int( (x+4)/4), "bold"))
    t.left(360/sides+1)
    t.width (x * sides/200)
print (i)

#import turtle
#sides = eval (input ('Введите количество сторон от 2 до 8: '))
#colors = ['blue', 'red', 'yellow', 'green', 'Pink','orange', 'yellow', 'green']
#t = turtle.Pen() # всроиный модуль turtle
#for x  in range(sides):
#    t.circle(60) # всроиный модуль turtle
    #turtle.bgcolor ("black")
    #t.pencolor(colors[x%sides])
#    t.forward(x * 3/sides+x)
#    t.left(360/sides+1)
#    t.width (x * sides/200)