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


mylist = [5,2,1,1,3, 5,3, 5,6,3,1,5]
print(mylist)
frequencyTable(mylist)
