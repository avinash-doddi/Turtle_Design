import turtle

colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green'] """we can use any colour"""

screen = turtle.Screen()
trtl = turtle.Turtle()
trtl.speed(0)
screen.bgcolor('black') """this is background colour"""

for x in range(360):  """if we change this to 180 or 250 we would get pre-complleted spiral"""
    trtl.pencolor(colors[x % 6]) #here we can decrease [x%6] to [x%5] or [x%4] to decrease the width of spiral
    trtl.width(x / 5 + 1)
    trtl.forward(x)
    trtl.left(20)
