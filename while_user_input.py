# message = ''
# while message != 'quit':
# 	message = input("Please enter pizza toppings. When done enter quit.")
# 	if(message != 'quit'):
# 		print(f"Adding {message}...")

# message = ''
# while True:
# 	message = input("Enter your age to know the ticket price")
# 	age = int(message)
# 	if(age < 3):
# 		print("The ticket is free")
# 	elif(age >= 3 and age <= 12):
# 		print("The ticket price is $10")
# 	else:
# 		print("The ticket price is $15")

# x = 1
# while x <=5:
# 	print(x)
# 	x += 1

# unconfirmed_users = ['ravi', 'greeshu', 'prati']
# confirmed_users = []

# while unconfirmed_users:
# 		unconfirmed_user = unconfirmed_users.pop()
# 		print(f"Verifying {unconfirmed_user}...")
# 		confirmed_users.append(unconfirmed_user)

# if confirmed_users:
# 	print("Below users are confirmed...")
# 	for confirmed_user in confirmed_users:
# 		print(f"{confirmed_user}")

# responses = {}

# polling_active = True

# while polling_active:
# 	name = input("\nWhat is your name?")
# 	response = input("Please tell something about you?")

# 	responses[name] = response

# 	repeat = input("Would you like to let another person respond? (yes/no)")
# 	if repeat != 'yes':
# 		polling_active = False

# if responses:
# 	print("\n---Poll Results---")
# 	for name, response in responses.items():
# 		print(f"{name}'s about : {response}")

# sandwich_orders = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's7', 's7']
# finished_sandwiches = []

# print("Deli has run out of 's7' sandwich")

# while 's7' in sandwich_orders:
# 	sandwich_orders.remove('s7')

# while sandwich_orders:
# 	finished_sandwich = sandwich_orders.pop()
# 	print(f"\nI made your {finished_sandwich} sandwich")
# 	finished_sandwiches.append(finished_sandwich)

# if finished_sandwiches:
# 	print("\n---Finished Sandwiches---")
# for finished_sandwich in finished_sandwiches:
# 	print(f"{finished_sandwich}")

dream_vacations = {}

poll_active = True

while poll_active:
	name = input("\nWhat is your name")
	place = input("If you could visit one place in the world, where would you go?")

	dream_vacations[name] = place

	poll_end = input("Would you let another person to take the poll? (yes/no)")
	if poll_end == 'no':
		poll_active = False

if dream_vacations:
	print("\n---Poll Results---")
	for name, place in dream_vacations.items():
		print(f"{name.title()} would like to visit {place.title()}")


















