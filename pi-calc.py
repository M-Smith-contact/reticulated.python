import math

def archimedes(numSides):
    
    innerangleB = 360.0/numSides
    halfangleA = innerangleB/2

    onehalfsideS = math.sin(math.radians(halfangleA))

    sideS = onehalfsideS * 2

    polygonCircumference = numSides * sideS
    pi = polygonCircumference/2

    return pi

for sides in range(8,100,8):
    my_pi = archimedes(sides)
    print( sides, my_pi )
    
