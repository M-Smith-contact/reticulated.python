quakedata =[]

def makeMagnitudeList():
        quakefile = open("earthquake-3-18-15.txt","r")
        maglist = [ ]
        for aline in quakefile:
            quakedata.append(aline)
            vlist = aline.split()
            maglist.append(float(vlist[4]))
        quakefile.close()
        return maglist

mag = makeMagnitudeList()
print(mag)

maxmag = max(mag)
maxidx = mag.index( maxmag)

print( maxmag)
print( maxidx)

print( quakedata[maxidx] )





# serach max mag location
#c = 0
#quakefile = open("earthquake-3-18-15.txt","r")
#for aline in quakefile:
#        if c == maxidx:
#            break
#        c = c + 1
#quakefile.close()
        
#print( aline )


#inputfile = open("earthquake-3-18-15.txt","r")
#outputfile = open("rainfallInCM.txt","w")

#for aline in inputfile:
#    values = aline.split()
    #print( values )
    #rainfallcm = float(values[1]) * 2.54
    #strcm = values[0] + ' ' + str(rainfallcm)+ '\n'
    #outputfile.write( strcm ) 

#inputfile.close()
#outputfile.close()

