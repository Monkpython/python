#range this makes numbers go 1 2 3 4 5 down
for value in range(1, 6):
    print(value)

#Makes this as list goes straight across
numbers = list(range(1, 6))
print(numbers)

#Makes a list and only 
even_numbers = list(range(2, 11, 2))
print(even_numbers)

#put square of a range from 1 to 10
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)


print(squares)


#Statistics with a list of numbers
digits =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
min(digits)
max(digits)
sum(digits)
