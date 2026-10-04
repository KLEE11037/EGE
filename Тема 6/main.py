from turtle import *
# Отключает анимацию черепахи (Рисунок выводится сразу)
tracer(0)
# Коэффициент, для увеличения масштаба изображения
koef = 20

# Алгоритм рисования фигуры
right(45)
for i in range(7):
    forward(5 * koef)
    right(45)
    forward(10 * koef)
    right(135)

# Алгоритм рисования сетки
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * koef, y * koef)
        dot(3)
exitonclick()