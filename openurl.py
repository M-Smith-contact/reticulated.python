import urllib.request
page = urllib.request.urlopen("http://earthquake.usgs.gov/earthquakes/map/")

#pageText = page.readlines()
pageText = page.readlines()[:5]
print( pageText )

line = page.read().decode('utf-8')  
print( line )


