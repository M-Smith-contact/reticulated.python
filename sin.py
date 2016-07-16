# example 1a
import numpy as np # get access to fast arrays
import matplotlib . pyplot as plt # the plotting functions
x = np. arange ( -3.14 , 3.14 , 0.01) # create x- data
y = np.sin(x) # compute y- data
plt. plot (x, y) # create plot
plt. show () # show plot ( makes window pop up)
