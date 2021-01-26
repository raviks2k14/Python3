# def display_message():
# 	"""Display message..."""
# 	print("I am learning about the functions in this chapter")

# display_message()

# def favorite_book(title):
# 	"""Mentioning favorite book"""
# 	print(f"My favorite book is {title}")

# favorite_book('Alice in wonderland')

# def make_shirt(size, message):
# 	"""This function prints the size and the message on the shirt"""
# 	print(f"The shirt is of the {size} with text {message}")

# make_shirt('L', 'long shirt')
# make_shirt(size='M', message='medium sized shirt')
# make_shirt(message='medium sized shirt', size='M')

# def make_shirt(size='L', message='I love python'):
# 	"""This function is of size L by default and the message 'I love python'"""
# 	print(f"The shirt is of size {size} and message {message}")

# make_shirt(size='L')
# make_shirt(size='M')
# make_shirt(size='S', message='This is of small size')

# def describe_city(city, country='Iceland'):
# 	"""Prints city and the country it belongs to"""
# 	print(f"{city} is in {country}")

# describe_city('ABC')
# describe_city('XYZ', 'India')
# describe_city(city='XYZ', country='India')
# describe_city(country='America', city='Sunnyvale')

# def city_country(city, country):
# 	content='----------------------'
# 	content+=f'\n{city}, {country}'
# 	content+='\n----------------------'
# 	return content

# content = city_country('Bangalore', 'India')
# print(content)

# content = city_country('Mysore', 'India')
# print(content)

# content = city_country('Santiago', 'Chile')
# print(content)

def make_album(artist, album, songs=None):
	"""This function prints """
	if songs:
		art_dictionary = {'artist' : artist, 'album' : album, 'songs' : songs}
	else:
		art_dictionary = {'artist' : artist, 'album' : album}
	return art_dictionary

# art_disc = make_album('ARTIST1', 'ALBM1')
# print(art_disc)

# art_disc = make_album('ARTIST2', 'ALBM2')
# print(art_disc)

# art_disc = make_album('ARTIST3', 'ALBM3')
# print(art_disc)

# art_disc = make_album('ARTIST3', 'ALBM3', 20)
# print(art_disc)

while True:
	artist = input("Please enter the name of the artist. If you don't want to enter, type q")
	album = input("Please enter the name of the album")

	if artist != 'q':
		art_disc = make_album(artist, album)
		print(art_disc)
	else:
		break































































