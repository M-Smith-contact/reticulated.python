ages = {'David':45, 'Brenda':46}
ages['Kelsey'] = 19

l = len( ages )

print( ages )
ages['Kelsey'] = ages['Kelsey'] + 1
print( ages )
print( l)
print( ages.keys() )
mykeys = list(ages.keys())
myvals = list(ages.values())
print( mykeys )
print( myvals )

myitems = ages.get('Kelsey')
print( myitems )

ch = 'John' in ages
print( ch)

del ages['Brenda']
print( ages )
