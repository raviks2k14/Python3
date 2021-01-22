aliens = [] #Nesting in this example shows the embedding of dictionary in the list

for alien_number in range(30):
	new_alien = {'color' : 'green', 'points' : '5', 'speed' : 'slow'}
	aliens.append(new_alien)

for alien in aliens[:3]:
	if(alien['color'] == 'green'):
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10

for alien in aliens[:5]:
	print(alien)
print("...")

print(f"Total number of aliens : {len(aliens)}")

#Exercises
people_0 = {'name' : 'ravi', 'city' : 'sunnyvale', 'county' : 'santa clara',}
people_1 = {'name' : 'greeshu', 'city' : 'sunnyvale', 'county' : 'santa clara',}
people_2 = {'name' : 'prati', 'city' : 'sunnyvale', 'county' : 'santa clara',}

peoples = [people_0, people_1, people_2]

for people in peoples:
	print(f"Name : {people['name'].title()}")
	print(f"City : {people['city'].title()}")
	print(f"County : {people['county'].title()}")

favorite_places = {
		'ravi' : ['sfo', 'sunnyvale', 'cupertino'], 
		'greeshu' : ['disney', 'hollywood', 'vegas'], 
		'prati' : ['liberty', 'tahoe', 'yosemite'],
}

for name, places in favorite_places.items():
	print(f"Favorite places of {name.upper()} are :")
	for place in places:
		print(f"{place.title()}")

cities = {
	'Bangalore' : {
		'country' : 'india',
		'population' : '3 million',
		'fact' : 'traffic city',
	},
	'Mysore' : {
		'country' : 'india',
		'population' : '2 million',
		'fact' : 'beautiful city',
	},
	'Mandya' : {
		'country' : 'india',
		'population' : '1 million',
		'fact' : 'normal city',
	},
}


for city, infos in cities.items():
	print(f"\nAbout the city '{city.upper()}'")
	for k, v in infos.items():
		print(f"{k.title()} : {v.title()}")























