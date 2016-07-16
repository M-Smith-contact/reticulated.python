def drawSpiral(myTurtle,maxSide):
        for sideLength in range(1,maxSide+1,5):
            myTurtle.forward(sideLength)
            myTurtle.right(90)

import turtle
t = turtle.Turtle()
#t.color('red')
t.up()

drawSpiral(t, 200)
            
