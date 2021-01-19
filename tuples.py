print("Initial Tuple")
foods = ('fries', 'salad', 'burger') #This is a tuple meaning constants, Just like list but can't be modified
for food in foods:
	print(food)

#foods[0] = 'nuggets' #Tuple object doesn't support item assignment
#print(foods) #This will result in an error

print("\nOverwritten Tuple")
foods = ('burrito', 'fries', 'toast', 'salad') #Variable can be assigned with new set of values
for food in foods:
	print(food)