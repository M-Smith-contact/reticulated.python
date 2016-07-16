def getRange(alist):
    return max(alist)-min(alist)

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

def mean(alist):
    mean = sum(alist) / len(alist)
    return mean

def median(alist):
    copylist = alist[:]  #make a copy using slice operator
    copylist.sort()
    if len(copylist)%2 == 0: #even length
        rightmid = len(copylist)//2
        leftmid = rightmid - 1
        median = (copylist[leftmid] + copylist[rightmid])/2
    else:     #odd length
        mid = len(copylist)//2
        median = copylist[mid]
    return median

def mode(alist):
    countdict = {}
    
    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1
            
    countlist = countdict.values()
    maxcount = max(countlist)
    
    modelist = [ ]
    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)
    
    return modelist

def frequencyTable(alist):
    countdict = {}

    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1
    
    itemlist = list(countdict.keys())
    itemlist.sort()
    
    print("ITEM","FREQUENCY")
    
    for item in itemlist:
        print(item, "     ",countdict[item])


quakeM = makeMagnitudeList()
print("Magnitude: ")
print(quakeM)

quakeRange = getRange(quakeM)
print("Range: ")
print(quakeRange)

quakeMean = mean(quakeM)
print("Mean: ")
print( quakeMean )

quakeMedian = median(quakeM)
print("Median: ")
print( quakeMedian )

quakeMode = mode(quakeM)
print("Mode: ")
print( quakeMode )

frequencyTable(quakeM)






