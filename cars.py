#SORT IS perminent

cars = ['bmw', 'audi', 'toyota', 'subaru']

#pre-sort print
print(cars)
cars.sort()

#post-sort print
print(cars)

#reverse-sort arguement
# cars.sort(reverse=True)
# print(cars)

#SORTED IS TEMPORARY
print("here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

#reverse method, must be done pre-print and perminent 
cars.reverse()
print(cars)

#length of a list
print(len(cars))