import turtle
import time
pen = turtle.Turtle()
a = [3, 4, 5, 6, 7, 8, 9]
angle = [120, 90, 72, 60, 51.45, 45, 40]
dist = [-5, -10, -15, -20, -25, -30, -40]
penForward = [40, 60, 85, 95, 105, 120, 130]
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'darkblue', 'purple']

for i in range(7):

    pen.color(colors[i])
    pen.width(a[i]/2)
    for j in range(a[i]):
        pen.forward(penForward[i])
        pen.left(angle[i])
    pen.penup()
    pen.setpos(dist[i], 3.5*(dist[i]))
    pen.pendown()

time.sleep(5)