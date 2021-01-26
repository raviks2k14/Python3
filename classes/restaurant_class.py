class Restaurant:

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(f"\nThe restaurant name is {self.restaurant_name}")
		print(f"The cuisine type is {self.cuisine_type}")

	def open_restaurant(self):
		print("\nThe restaurant is open now!!!")

restaurant_instance_01 = Restaurant('Sankranti', 'Non-Veg')
restaurant_instance_02 = Restaurant('Udupi', 'Veg')
restaurant_instance_03 = Restaurant('Ulavacharu', 'Veg/Non-Veg')

restaurant_instance_01.describe_restaurant()
restaurant_instance_01.open_restaurant()

restaurant_instance_02.describe_restaurant()
restaurant_instance_02.open_restaurant()

restaurant_instance_03.describe_restaurant()
restaurant_instance_03.open_restaurant()



