####################################################################
## move to (x,y)
####################################################################
def moveTo( myTurtle, x, y):
    myTurtle.up()
    xpos = myTurtle.xcor()  # get current position
    ypos = myTurtle.ycor()
    heading = myTurtle.heading() # get heading
    if x > xpos:
        myTurtle.forward( x - xpos)
    else:
        myTurtle.backward( xpos - x)
    if y > ypos:
        myTurtle.left(90)
        myTurtle.forward( y - ypos)
    else:
        myTurtle.right(90)
        myTurtle.forward( ypos - y)

    myTurtle.setheading(heading) # set original heading

    myTurtle.down() # tail down

####################################################################
## draw a polygon
####################################################################
def drawPolygon(myTurtle,sideLength,numSides):
    turnAngle = 360 / numSides
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.right(turnAngle)

    myTurtle.setheading(0) # set original heading

####################################################################
## draw a polygon
####################################################################
def drawCircle(myTurtle,center_x, center_y, radius, lineColor, fillColor):
    moveTo( myTurtle, center_x, center_y + radius)
     
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360

    myTurtle.color( lineColor )
    myTurtle.fillcolor( fillColor )
        
    myTurtle.begin_fill()
    drawPolygon(myTurtle,sideLength,360)
    myTurtle.end_fill()

    myTurtle.setheading(0) # set original heading

    myTurtle.up()
    myTurtle.home()
    myTurtle.down()

####################################################################
## draw a line determined by (x1,y1) and (x2,y2)
####################################################################
def drawLine(myTurtle, x1, y1, x2, y2, mycolor):
    #print( mycolor )
    moveTo( myTurtle, x1, y1)
    lineLen = math.sqrt( (x2-x1)**2 + (y2-y1)**2)  
    angle = math.atan2( y2-y1, x2-x1) / math.pi * 180

    #print(angle)
    if angle < 0:
        angle = 360 + angle
        
    myTurtle.setheading(angle) # set turtle heading
    myTurtle.color( mycolor )
    myTurtle.forward( lineLen )

    myTurtle.setheading(0) # set original heading

    myTurtle.up()
    myTurtle.home()
    myTurtle.down()

####################################################################
## draw a triangle determined by (x1,y1), (x2,y2), and (x3,y3)
####################################################################
def drawTriangle(myTurtle, x1, y1, x2, y2, x3, y3, lineColor, fillColor):

    myTurtle.color( lineColor )
    myTurtle.fillcolor( fillColor )

    # first side
    moveTo( myTurtle, x1, y1)

    myTurtle.begin_fill()
    lineLen = math.sqrt( (x2-x1)**2 + (y2-y1)**2)  
    angle = math.atan2( y2-y1, x2-x1) / math.pi * 180

    if angle < 0:
        angle = 360 + angle
        
    myTurtle.setheading(angle) # set turtle heading
    myTurtle.forward( lineLen )

    # second side
    lineLen = math.sqrt( (x3-x2)**2 + (y3-y2)**2)  
    angle = math.atan2( y3-y2, x3-x2) / math.pi * 180

    if angle < 0:
        angle = 360 + angle
        
    myTurtle.setheading(angle) # set turtle heading
    myTurtle.forward( lineLen )

    # third side
    lineLen = math.sqrt( (x1-x3)**2 + (y1-y3)**2)  
    angle = math.atan2( y1-y3, x1-x3) / math.pi * 180

    if angle < 0:
        angle = 360 + angle
        
    myTurtle.setheading(angle) # set turtle heading
    myTurtle.forward( lineLen )

    myTurtle.end_fill()


    myTurtle.setheading(0) # set original heading
    myTurtle.up()
    myTurtle.home()
    myTurtle.down()

    
####################################################################
## draw a rectangle, left-top: (x,y), size: width x heeight 
####################################################################
def drawRectangle(myTurtle,  x, y, width, height, lineColor, fillColor):
    moveTo( myTurtle, x, y)

    myTurtle.color( lineColor )
    myTurtle.fillcolor( fillColor )

    myTurtle.begin_fill()

    myTurtle.forward( width )
    myTurtle.right( 90 )
    myTurtle.forward( height )
    myTurtle.right( 90 )
    myTurtle.forward( width )
    myTurtle.right( 90 )
    myTurtle.forward( height )
    myTurtle.right( 90 )

    myTurtle.end_fill()

    myTurtle.setheading(0) # set original heading

    myTurtle.up()
    myTurtle.home()
    myTurtle.down()

import turtle
import math

t = turtle.Turtle()
t.width(3)
#moveTo(t, -200, 200)

#drawLine(t , -200, 50, 100, -100, 'blue' )

drawCircle( t, 0, 0, 93, 'red', 'green')
drawCircle( t, 0, 0, 83, 'red', 'blue')
#drawRectangle( t, -50, 200, 100, 50, 'orange', 'pink')
drawTriangle( t, -60, 60, 14, 14, -14, -14, 'red', 'white')
drawTriangle( t, 60, -60, 14, 14, -14, -14, 'red', 'white')
drawTriangle( t, 60, 60, 14, -14, -14, 14, 'red', 'white')
drawTriangle( t, -60, -60, 14, -14, -14, 14, 'red', 'white')

drawCircle( t, 0, 0, 43, 'red', 'orange')
drawCircle( t, 0, 0, 33, 'red', 'yellow')

drawTriangle( t, 0, 85, 20, 0, -20, 0, 'red', 'white')
drawTriangle( t, 0, -85, 20, 0, -20, 0, 'red', 'white')
drawTriangle( t, 85, 0, 0, 20, 0, -20, 'red', 'white')
drawTriangle( t, -85, 0, 0, 20, 0, -20, 'red', 'white')

drawCircle( t, 0, 0, 23, 'red', 'blue')
drawCircle( t, 0, 0, 8, 'red', 'green')

moveTo(t, -150, 0)
