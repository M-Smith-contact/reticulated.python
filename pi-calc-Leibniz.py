def leibniz(terms):
    acc = 0    
    num = 4   
    den = 1      

    for aterm in range(terms):
        nextterm = num/den * (-1)**aterm

        acc = acc + nextterm  

        den = den + 2         

    return acc

myPI =  leibniz(1000)

print( myPI)
