
# SquareSpiralInput2 - Разноцветная спираль, цвет берется из списка

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

