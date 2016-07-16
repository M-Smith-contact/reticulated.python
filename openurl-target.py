import urllib.requests
#url1 = urllib.request.urlopen('http://ichart.yahoo.com/table.csv?s=AAPL') # Aple Inc.
#url1 = urllib.request.urlopen('http://ichart.yahoo.com/table.csv?s=TGT') # Target
url1 = urllib.request.urlopen('http://ichart.yahoo.com/table.csv?s=MSFT') # Microsoft

t1Data = url1.readlines()
print( t1Data[:10] )

firstLine = t1Data[0].decode("utf-8").split(',')
print( firstLine )

t1DataAlt = [line.decode("utf-8").split(',') for line in t1Data[1:]]
print( t1DataAlt[:3] )
