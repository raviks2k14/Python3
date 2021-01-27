from random import randint
from random import choice


class Lottery:

    def __init__(self, random_list):
        self.random_list = random_list

    def random_numbers(self):
        print(choice(self.random_list))


random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D']
lottery = Lottery(random_list)
print(lottery.random_numbers())
print(lottery.random_numbers())
print(lottery.random_numbers())
print(lottery.random_numbers())
