#Exercise 4-13
#Buffet

#first tuple
foods = ("mac and cheese", "steak", "salad", "pizza", "ice cream")

print("\nThe restaurant buffet offers:")
for food in foods:
    print(food)

#attempt in modifying tuple, throws a type error
#foods[0] = "brocolli"

#Revised tuple
foods = ("potatoes", "steak", "pie", "pizza", "ice cream")
print("\nThe restaurant revised buffet menu offers:")
for food in foods:
    print(food)

