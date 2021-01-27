class User:

	def __init__(self, first_name, last_name, age, dob):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.dob = dob

	def describe_user(self):
		print(f" The user's first name is {self.first_name}")
		print(f" The user's last name is {self.last_name}")
		print(f" The user's age is {self.age}")
		print(f" The user's dob is {self.dob}")

	def greet_user(self):
		print(f"Hello {self.first_name} {self.last_name}, Welcome to Python Programming!!!")

user_instance_01 = User('Ravikumar Kumbalore', 'Shankarappa', 35, '04/19/1985')
user_instance_02 = User('Greeshma', 'Ravikumar', 6, '10/19/2010')
user_instance_03 = User('Pratibha', 'Ravikumar', 25, '04/19/1995')

user_instance_01.describe_user()
user_instance_01.greet_user()

user_instance_02.describe_user()
user_instance_02.greet_user()

user_instance_03.describe_user()
user_instance_03.greet_user()

