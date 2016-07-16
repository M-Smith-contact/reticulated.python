def median(alist):
    copylist = alist[:]  #make a copy using slice operator
    copylist.sort()

    print( copylist )
    
    if len(copylist)%2 == 0: #even length
        rightmid = len(copylist)//2
        leftmid = rightmid - 1
        median = (copylist[leftmid] + copylist[rightmid])/2
    else:     #odd length
        mid = len(copylist)//2
        median = copylist[mid]
    return median

def getRange(alist):
    return max(alist)-min(alist)

mylist1 = [34, 56, 2, 23, 1, 3, 4, 5, 30, 145]


mymax = max( mylist1)
mymin = min( mylist1)
myave = sum( mylist1) / len(mylist1)

rng = getRange(mylist1)

print( mylist1)
print( mymax)
print( mymin)
print( myave)
print( rng)

md = median(mylist1)
print( md )


