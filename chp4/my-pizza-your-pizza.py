#Exercise 4-11 My Pizzas, Your pizzas
#Create a pizza list, copy pizza list
pizzas = ["pesto brocolli chicken", "alfredo beef", "chicken bacon garlic"]
friend_pizzas = pizzas[:]

#Append each list with a unique value
pizzas.append('Pepperoni')
friend_pizzas.append('Anchovies')

#print pizzas list, used list comprehension
print("\nMy favorite pizzas are:")
[print(pizza) for pizza in pizzas]

#print friend_pizzas list, used list comprehension
print("\nMy friend's favorite pizzas are:")
[print(pizza) for pizza in friend_pizzas]

