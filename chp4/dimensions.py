#Tuple is like a list that doesn't change so a constant for lists. It uses parentheses vs square brackets.

dimensions = (200, 50)

#Attempt to modify a tuple, gives typeerror
#dimensions[0] = 250

#printing each element in the tuple
#print(dimensions[0])
#print(dimensions[1])

#loop throught tuple
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

#Reuse a tuple to modify the data within a tuple
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


