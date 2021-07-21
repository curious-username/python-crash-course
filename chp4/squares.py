squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

#above code is the same as directly below
squares = [value**2 for value in range(1,11)]
print(squares)


#list of digits
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#lowest digit in list
print(min(digits))

#highest digit in list
print(max(digits))

#all digits in list added together
print(sum(digits))
