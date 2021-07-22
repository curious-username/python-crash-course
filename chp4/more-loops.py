#Exercise 4-12
#More Loops

#Created list and copy of list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

#adding individual string to each list to verify the copies are different
my_foods.append('cannoli')
friend_foods.append('ice cream')

#utilized list comprehension to list out foods from my_foods list
print("\n\tMy favorite foods are:")
[print(food) for food in my_foods]

#utilized list comprehension to list out foods from friend_foods list
print("\n\tMy friend's favorite foods are:")
[print(food) for food in friend_foods]