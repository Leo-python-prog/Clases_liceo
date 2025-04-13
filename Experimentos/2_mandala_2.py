from turtle import *
from colorsys import *
speed(0)
bgcolor("black")
h = 0.1
def fun():
    global h
    for i in range(4):
        c = hsv_to_rgb(h, 1, 1)
        fillcolor(c)
        h += 0.004
        begin_fill()
        forward(40)
        right(20)
        forward(40)
        right(9)
        end_fill()
        
for i in range(100):
    fun()
    goto(0, 0)
    right(10)
done()