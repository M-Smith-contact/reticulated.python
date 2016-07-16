import urllib.request
#page = urllib.request.urlopen("http://earthquake.usgs.gov/earthquakes/map/")
page = urllib.request.urlopen("http://www.tnstate.edu//")

pageText = page.read()
print( pageText )
decodedPageText = pageText.decode("UTF-8")  
print( decodedPageText )


