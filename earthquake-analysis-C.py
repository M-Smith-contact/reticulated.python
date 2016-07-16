def makeMagnitudeList():
        quakefile = open("earthquake-3-18-15.txt","r")
        maglist = [ ]
        for aline in quakefile:
            vlist = aline.split()
            maglist.append(float(vlist[4]))
        quakefile.close()
        return maglist

mag = makeMagnitudeList()
print(mag)

