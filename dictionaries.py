person = {
	'first_name' : 'john',
	'last_name' : 'doe',
	'age' : '25',
	'place' : 'california',
}

print(f"{person['first_name'].title()}")
print(f"{person['last_name'].title()}")
print(f"{person['age'].title()}")
print(f"{person['place'].title()}")

favorite_numbers = {
	'mickey' : '25',
	'donald' : '30',
	'goofy' : '100',
}

for k, v in favorite_numbers.items():
	print(f"Favorite number of {k.title()} is {v}")

rivers = {
	'nile' : 'egypt',
	'ganga' : 'india',
	'pacific' : 'america',
	'kaveri' : 'india',
}

for k,v in rivers.items():
	print(f"The {k.title()} runs through {v.title()}")

for river in rivers.keys():
	print(f"{river.title()}")

for country in rivers.values():
	print(f"{country.title()}")

for country in set(rivers.values()): #Set - Avoids duplicates
	print(f"{country.title()}")

for country in sorted(rivers.values()): #sorted - sorts the list in alphabetical order
	print(f"{country.title()}")


favorite_languages = {
	'ravi' : 'kannada',
	'mike' : 'english',
	'jordan' : 'spanish',
}

people = ['ravi', 'greeshu', 'prati']

for person in people:
	if person in favorite_languages.keys(): #Checking person for presence in the dictionary keys
		print(f"Thank you {person} for responding to the poll.")
	else:
		print(f"Hi {person}, Please take the poll.")

		














