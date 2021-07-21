#building a list
from functools import total_ordering


motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#replacing element value
# motorcycles[0] = 'ducati'
# print(motorcycles)

#inserting a element value into a list
motorcycles.insert(0, 'ducati')
print(motorcycles)

#removing an element at specific element
# del motorcycles[0]
# print(motorcycles)

#popping out of the list, defaults to last
# popped_motorcycle = motorcycles.pop(0)
# print("This first motorcycle I owned was a " + popped_motorcycle)

#remove by value
expensive = 'ducati'
motorcycles.remove(expensive)
print(motorcycles)
print("\nA " + expensive.title() + " is too expensive for me.")
