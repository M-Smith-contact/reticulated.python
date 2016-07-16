def drawPolygon(myTurtle,sideLength,numSides):
        turnAngle = 360 / numSides
        for i in range(numSides):
            myTurtle.forward(sideLength)
            myTurtle.right(turnAngle)

def drawCircle(myTurtle,radius):
        circumference = 2 * 3.1415 * radius
        sideLength = circumference / 360
        drawPolygon(myTurtle,sideLength,360)


import turtle
t = turtle.Turtle()

t.color('red')
t.fillcolor('yellow')

t.begin_fill()

drawCircle(t,50)

t.end_fill()

