def drawTriangle(myTurtle,sideLength):
        for i in range(3):
            myTurtle.forward(sideLength)
            myTurtle.right(120)

import turtle
t = turtle.Turtle()

t.color('red')
t.fillcolor('yellow')

t.begin_fill()

drawTriangle(t,100)

t.end_fill()

