inputfile = open("rainfall.txt","r")
outputfile = open("rainfallInCM.txt","w")

for aline in inputfile:
    values = aline.split()
    rainfallcm = float(values[1]) * 2.54

    #print( values[0], rainfallcm )
    print( "%s had %f cm of rain" %(values[0], rainfallcm) )

    #strcm = values[0] + ' ' + str(rainfallcm)+ '\n'
    #outputfile.write( strcm ) 

inputfile.close()
outputfile.close()
