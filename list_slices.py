list_slices = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight']
print("The first three items in the list are:")
for slice_data in list_slices[:3]:
	print(slice_data)

print("\nThree items from the middle of the list are:")
for slice_data in list_slices[2:5]:
	print(slice_data)

print("\nThe last three items in the list are:")
for slice_data in list_slices[-3:]:
	print(slice_data)

pizzas = ['cheese', 'pepparoni', 'chicken']
friend_pizzas = pizzas[:] #Copy one list to another
pizzas.append('veg')
friend_pizzas.append('mushroom')

print(pizzas)
print(friend_pizzas)