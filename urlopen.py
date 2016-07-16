import urllib.request
page = urllib.request.urlopen("http://earthquake.usgs.gov/earthquakes/map/")
pageText = page.read()

print(page)
print(pageText)

