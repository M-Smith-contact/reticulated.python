def mode(alist):
    countdict = {}
    
    for item in alist:
        if item in countdict:
            countdict[item] = countdict[item]+1
        else:
            countdict[item] = 1
        #print( countdict )
            
    countlist = countdict.values()
    maxcount = max(countlist)
    
    modelist = [ ]
    for item in countdict:
        if countdict[item] == maxcount:
            modelist.append(item)
    
    return modelist

mylist = [5,2,1,1,3, 5,3, 5,6,3,1,5]

mylist2 = mode(mylist)
print(mylist)
print(mylist2)
