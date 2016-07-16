mydict = {}

# read 5 employee name and age from keyboard
for i in range(5):
    print("Employee Name:")
    name = input()
    print("Employee Age:")
    age = int( input())

    mydict[name] = age



print (mydict)
mydict['Anna'] = 26
print (mydict)


    
    
