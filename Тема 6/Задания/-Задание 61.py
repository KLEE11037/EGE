from turtle import *
tracer(0)
screensize(2000,2000)
k = 10
down()
rt(180)
for i in range(9):
    fd(59*k)
    lt(90)
    fd(84*k)
    lt(90)
up()
fd(18*k)
lt(90)
fd(38*k)
rt(90)
down()
for i in range(9):
    fd(120*k)
    rt(90)
    fd(99*k)
    rt(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x*k,y*k)
        dot(3,)
exitonclick()







answer = 158

#

from tests.conftest import result_register
if answer is not Ellipsis:
    print(result_register(6, 61, answer, 'aab3238922bcc25a6f606eb525ffdc56'))