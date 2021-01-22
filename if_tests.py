alien_color = 'green'
if alien_color == 'green':
	print("You just earned 5 points")

alien_color = 'yellow'
if alien_color == 'green':
	print("You just earned 5 points")

alien_color = 'red'
if alien_color == 'green':
	print("You just earned 5 points")
else:
	print("You just earned 10 points")

if alien_color == 'green':
	print("You just earned 5 points")
if alien_color == 'yellow':
	print("You just earned 10 points")
if alien_color == 'red':
	print("You just earned 15 points")

age = 10
if age < 2:
	print("The person is a baby")
elif age < 4:
	print("The person is a toddler")
elif age < 13:
	print("The person is a kid")
elif age < 20:
	print("The person is a teenager")
elif age < 65:
	print("The person is an adult")
else:
	print("The person is elder")

favorite_fruits = ['mango', 'pineapple', 'apple']

if 'mango' in favorite_fruits:
	print("Mango is present in the fruit list!")
if 'pineapple' in favorite_fruits:
	print("Pineapple is present in the fruit list!")
if 'apple' in favorite_fruits:
	print("Apple is present in the fruit list!")
if 'orange' not in favorite_fruits:
	print("Orange is not present in the fruit list!")

users = ['admin', 'roshni', 'somaya', 'gowtham', 'aarnavi', 'emily', 'johana']

for user in users:
	if user == 'admin':
		print(f"Hello {user.title()}, would you like to see a status report?")
	else:
		print(f"Hello {user.title()}, thank you for logging in again")

users = []

if users:
	for user in users:
		print(f"Welcome {user.title()}")
else:
	print("We need to find some users")

current_users = ['admin', 'Roshni', 'somaya', 'gowtham', 'aarnavi', 'emily', 'johana']
current_users_copy = []

for current_user in current_users:
	current_users_copy.append(current_user.lower())

new_users = ['ROSHNI', 'somaya', 'tsering', 'elsa', 'anwita']

if new_users:
	for new_user in new_users:
		if new_user.lower() in current_users_copy:
			print("Please enter a new user name")
		else:
			print("Username is available")
else:
	print("Please provide the user names to check for existing records!!!")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

if numbers:
	for number in numbers:
		if number == 1:
			print(f"{number}st")
		elif number == 2:
			print(f"{number}nd")
		elif number == 3:
			print(f"{number}rd")
		else:
			print(f"{number}th")
else:
	print("The numbers list is empty")


















