# converter programd

def menu():
    print("(1) Convert Fahrenheit to Celsius")
    print("(2) Convert Celsius to Fahrenheit")
    print( "(3) Convert Kilograms to Pounds")
    print( "(4) Convert Pounds to Pounds")
    print( "(5) Convert Meters to Yards")
    print( "(6) Convert Yards to Meters")
    print( "(7) Convert Gallons to Liters")
    print( "(8) Convert Liters to Gallon")
    print( "(9) Convert Centimeters to Inches")
    print( "(10) Convert Inches to Centimeters")
    
def converter():
    menu();
    c = int(input('Enter menu number: '))
    if (c == 1):
        F2C();
    elif (c == 2):
        C2F();
    else:
        print ("Invalide choice: ", c)
    #print "Bye!";
    converter()

def C2F():
    Celsius = float(input('Enter degree in Celsius: '))
    Fahrenheit = (9.0 / 5.0) * Celsius + 32
    print (Celsius, 'Celsius = ', Fahrenheit, 'Fahrenheit')

def F2C():
    Fahrenheit  = float(input('Enter degree in Fahrenheit: '))
    Celsius = (Fahrenheit - 32) * (5.0 / 9.0)
    print (Fahrenheit,  'Fahrenheit = ', Celsius, 'Celsius')
    
converter()    
