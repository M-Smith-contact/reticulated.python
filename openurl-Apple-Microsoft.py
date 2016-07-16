import math
import urllib.request

def mean(alist):
    mean = sum(alist) / len(alist)
    return mean

def standardDev(alist):
    aMean = mean(alist)
    sum = 0
    
    for item in alist:
        difference = item - aMean
        diffsq = difference ** 2
        sum = sum + diffsq
        
    sdev = math.sqrt(sum/(len(alist)-1))
    return sdev

def correlation(xlist, ylist):
    xbar = mean(xlist)
    ybar = mean(ylist)
    xstd = standardDev(xlist)
    ystd = standardDev(ylist)
    num = 0.0
    for i in range(len(xlist)):
        num = num + (xlist[i]-xbar) * (ylist[i]-ybar)
    corr = num / ((len(xlist)-1) * xstd * ystd) 
    return corr

url1 = urllib.request.urlopen('http://ichart.yahoo.com/table.csv?s=AAPL')
url2 = urllib.request.urlopen('http://ichart.yahoo.com/table.csv?s=MSFT')

dataLength = 10
t1Data = url1.readlines()
print( t1Data[:dataLength] )

closePrice = []
for i in range(dataLength):
    if i == 0:
        continue
    firstLine = t1Data[i].decode("utf-8").split(',')
    closePrice.append( firstLine[4] )
    print( firstLine )


print( closePrice ) 


#t1DataAlt = [line.decode("utf-8").split(',') for line in t1Data[1:]]
#print( t1DataAlt[:3] )
