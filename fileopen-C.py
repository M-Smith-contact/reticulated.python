inputfile = open("rainfall.txt","r")
outputfile = open("rainfallInCM.txt","w")


mystr = inputfile.readlines()
print( mystr )

#for aline in inputfile:
#    values = aline.split()
#    rainfallcm = float(values[1]) * 2.54
#    strcm = values[0] + ' ' + str(rainfallcm)+ '\n'
    outputfile.write( strcm ) 

inputfile.close()
outputfile.close()
