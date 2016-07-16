def drawPolygon(myTurtle,sideLength,numSides):
        turnAngle = 360 / numSides
        for i in range(numSides):
            myTurtle.forward(sideLength)
            myTurtle.right(turnAngle)



import turtle
t = turtle.Turtle()
t.color('red')
t.fillcolor('yellow')
t.begin_fill()
drawPolygon(t, 100, 3)
t.end_fill()
