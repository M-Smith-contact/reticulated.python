inputfile = open("bmi-data.txt","r")
outputfile = open("bmi-result.txt","w")

name = []
weight = []
height = []
c = 0
for aline in inputfile:
    if c != 0:
        values = aline.split()
        name.append( values[0] )
        weight.append ( values[1] )
        height.append ( values[2] )
        print( values )
    c = c + 1
inputfile.close()

#print( name )
#print( weight )
#print( height )

# calculate BMI
bmi = []
num = len(name)
outputfile.write( "Name BMI\n")
for i in range( num ):
    h = float( height[i] ) * 12
    w = float( weight[i] )
    b = w / (h*h) * 703
    b_roundup = "%4.1f" % (b) 
    bmi.append( b_roundup )
    #print( b_roundup )

    s = name[i] + " " + bmi[i] + "\n"
    outputfile.write( s )
print( bmi )


# highest BMI
maxbmi = max( bmi )
ind = bmi.index( maxbmi )
s = name[ ind ]
print( "Highest BMI is %s, BMI value is %4.1f" % (s, float(maxbmi)) )
s2 = "\nHighest BMI is %s, BMI value is %4.1f\n\n" % (s, float(maxbmi))
outputfile.write( s2 )

# lowest BMI
minbmi = min( bmi )
ind = bmi.index( minbmi )
s = name[ ind ]
print( "Lowest BMI is %s, BMI value is %4.1f" % (s, float(minbmi) ) )
s2 = "Lowest BMI is %s, BMI value is %4.1f\n\n" % (s, float(minbmi) ) 
outputfile.write( s2 )

# find underweight peoples 
outputfile.write( "Underweight people:\n")
for i in range( num ):
    if float(bmi[i]) < 18.5:
        print( "%s is underweight, BMI value is %4.1f" % (name[i], float(bmi[i]) ) )
        s2 = "%s , BMI = %4.1f\n" % (name[i], float(bmi[i]) ) 
        outputfile.write( s2 )

# find overweight peoples 
outputfile.write( "\nOverweight people:\n")
for i in range( num ):
    if float(bmi[i]) >= 25:
        print( "%s is overweight, BMI value is %4.1f" % (name[i], float(bmi[i]) ) )
        s2 = "%s , BMI = %4.1f\n" % (name[i], float(bmi[i]) ) 
        outputfile.write( s2 )
outputfile.close()

        
