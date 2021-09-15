import turtle # Установка графики Turtle
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange", "purple", "white", "grey"]

#Запросить имя пользователя с помощью всплывающего окна
# textinput
sides = int(turtle.numinput("Сколько сторон", "Сколько сторон вы хотите (1-8)?", 4, 1, 8))

#i = turtle.textinput("Окно запроса имени", "Как твое имя?")

#нарисовать спираль из имени повторяемого 100 раз
for x in range(360):
    t.pencolor (colors[x % sides])#по очереди выбрать 4 цвета
    #t.penup() # Не ресовать обычные линии спирали
    t.forward(x*3 / sides + x) # Переместить черепашку по экрану
    #t.pendown()
    #t.write(i, font= ("Arial", int( (x+4)/4), "bold"))
    t.left(360 / sides +1)
    t.width(x * sides / 200)
#print (i)
