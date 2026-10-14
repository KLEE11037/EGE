from turtle import *
size = 30
screensize(2000,2000)
tracer(0)
down()
from turtle import *
k = 15
tracer(0)
x=3
down()
for i in range(5):
    forward(x*k)
    right(90)
    forward(3*k)
up()

for x in range(-10,10):
    for y in range(-20,10):
        setpos(x*k,y*k)
        dot(5,)
done()
