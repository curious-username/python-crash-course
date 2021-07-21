#list comprehension
one_million = [number for number in range(1,1000001)]
print(one_million)

#OR

one_million = []
for number in range(1,1000000):
    one_million.append(number)
print(one_million)