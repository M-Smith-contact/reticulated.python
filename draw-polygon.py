
def drawPolygon(myTurtle,sideLength,numSides):
        turnAngle = 360 / numSides
        for i in range(numSides):
            myTurtle.forward(sideLength)
            myTurtle.right(turnAngle)


import turtle
t = turtle.Turtle()

drawPolygon(t, 50, 5)
