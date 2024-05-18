from turtle import *
import colorsys
import turtle
bgcolor('black')
pensize(1)
tracer(10)
h=0
for i in range(500):
    c=colorsys.hsv_to_rgb(h,1,1)
    h+=0.005
    pencolor(c)
    fillcolor('black')
    begin_fill()
    for j in range(3):
        fd(i*0.6)
        rt(120)
        fd(100)
        rt(120)
    rt(121)
    end_fill()
hideturtle()
done()        