import math
from turtle import *

def heart_x(k):
    return 15*math.sin(k)**3

def heart_y(k):
    return 12*math.cos(k) - 5*math.cos(2*k) - 2*math.cos(3*k) - math.cos(4*k)

speed(0)  # fastest speed
bgcolor("black")

penup()
goto(0, 0)
pendown()

color("#f73487")  # set the pen color to pink

for i in range(2000):  # reduced the number of iterations
    k = i * math.pi / 90  # increased the step size
    x = heart_x(k) * 20
    y = heart_y(k) * 20
    goto(x, y)

done()