import numpy
# demo curve fitting : xdata and ydata are input data
xdata = numpy . array ([0.0 , 1.0 , 2.0 , 3.0 , 4.0 , 5.0])
ydata = numpy . array ([0.0 , 0.8 , 0.9 , 0.1 , -0.8, -1.0])
#now do fit for cubic ( order = 3) polynomial
z = numpy . polyfit (xdata , ydata , 3)
#z is an array of coefficients , highest first , i.e.
# x^3 X^2 X 0
#z= array ([ 0.08703704 , -0.81349206 , 1.69312169 , -0.03968254])
#It is convenient to use `poly1d ` objects for dealing with polynomials :
p = numpy . poly1d (z) # creates a polynomial function p from coefficients
# and p can be evaluated for all x then .
# create plot
xs = [0.1 * i for i in range (50)]
ys = [p(x) for x in xs] # evaluate p(x) for all x in list xs

from matplotlib import pyplot

pyplot.plot (xdata , ydata , 'o', label ='data ')
pyplot.plot (xs , ys , label ='fitted curve ')
pyplot.ylabel ('y')
pyplot.xlabel ('x')
pyplot.savefig ('polyfit .pdf ')
pyplot.show ()
