def drawPolygon(myTurtle,sideLength,numSides):
        turnAngle = 360 / numSides
        for i in range(numSides):
            myTurtle.forward(sideLength)
            myTurtle.right(turnAngle)



import turtle

t = turtle.Turtle()
t.color('red')
drawPolygon(t, 20, 12)
