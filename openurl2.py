import urllib.request

def countHead(url):
    page = urllib.request.urlopen(url)
    numHeadLines = 0
    numBodyLines = 0

    line = page.readline().decode('utf-8')  
    #print( line )
    while '<head>' not in line:
        line = page.readline().decode('utf-8')

    line = page.readline().decode('utf-8')  
    while '</head>' not in line:    
        numHeadLines = numHeadLines + 1
        line = page.readline().decode('utf-8')      
        #print( line )

    line = page.readline().decode('utf-8')  
    while "<body" not in line:     
        line = page.readline().decode('utf-8')      

    line = page.readline().decode('utf-8')  
    while "</body>" not in line:
        numBodyLines = numBodyLines + 1;
        line = page.readline().decode('utf-8')                  

    print ("number of lines in header = ", numHeadLines)
    print ("number of lines in body = ", numBodyLines)

    page.close()


countHead("http://www.tnstate.edu/")

