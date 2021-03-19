import turtle

colors = ['orange', 'red', 'pink', 'yellow', 'blue', 'green']

screen = turtle.Screen()
trtl = turtle.Turtle()
trtl.speed(0)
screen.bgcolor('black')

for x in range(360):
    trtl.pencolor(colors[x % 6]) ''' here we can decrease [x%6] to x%5 or x%4 to decrease the width of spiral'''
    trtl.width(x / 5 + 1)
    trtl.forward(x)
    trtl.left(20)