def makeMagnitudeList():
        quakefile = open("2.5_day.txt","r")

        aline = quakefile.readline() # skip header

        maglist = [ ]
        for aline in quakefile:
            vlist = aline.split()
            #print( vlist )
            maglist.append(float(vlist[4]))

        quakefile.close()
        return maglist



quakeM = makeMagnitudeList()
print(quakeM)    
