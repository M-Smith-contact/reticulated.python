import urllib.request
url1 = urllib.request.urlopen('http://ichart.yahoo.com/table.csv?s=MSFT') # Microsoft

dataLen = 10
t1Data = url1.readlines()
print( t1Data[:dataLen] )

closePrice = []
for i in range(dataLen):
    if i == 0:
        continue
    firstLine = t1Data[i].decode("utf-8").split(',')
    closePrice.append( firstLine[4] )
    print( firstLine )
