#Any lines of codes that should be a part of the loop, should always be indented. 
#Else it won't be part of the loop. Regular print statements where for loop is not used need not be indented

pizzas = ['cheese', 'veg', 'chicken']
for pizza in pizzas:
	print(f"I like {pizza} pizza")
print("\nI like the veg pizza")
print("I really love pizza") 
print("\n")

pets = ['dog', 'cat', 'rabbit']
for pet in pets:
	print(f"A {pet} would make a good pet")

print("Any of these animals make a good pet")
print("\n")

#range() function - prints until the last but one item. The following example prints from 1 to 5 excluding 6
for value in range(1, 6):
	print(value)

for value in range(6):
	print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

odd_numbers = list(range(1, 11, 2))
print(odd_numbers)

squares = []
for value in range(1, 11):
	value = value ** 2
	squares.append(value)

print(squares)

#List Comprehensions
squares = [value**2 for value in range(1, 11)] 
print(squares)

for value in range(1, 21):
	print(value)

#Printing numbers from 1 to million
numbers_list = [value for value in range(1, 1000000)]
#print(numbers_list)

#Printing the min, max and sum of range from 1 to million
print(min(numbers_list))
print(max(numbers_list))
print(sum(numbers_list))

odd_numbers = []
for value in range(1, 21, 2):
	print(value)
	odd_numbers.append(value)

print(odd_numbers)

three_multiples = []
for value in range(3, 31):
	three_multiples.append(value*3)

print(three_multiples)

cubes = []
for value in range(1, 10):
	cubes.append(value**3)

print(cubes)

#Cube Comprehension
cubes = [value**3 for value in range(1, 10)]
print(cubes)
