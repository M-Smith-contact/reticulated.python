import math

x1 = 20
y1 = 0
theta = -math.pi/4
x2 = x1 * math.cos(theta) - y1 * math.sin(theta)
y2 = x1 * math.sin(theta) + y1 * math.cos(theta)


print(x2, y2)
