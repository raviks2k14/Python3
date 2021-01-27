from random import randint

class Die:

    def __init__(self, side):
        self.side = side

    def roll_die(self):
        print(randint(1, self.side))


die_6 = Die(6)
die_10 = Die(10)
die_20 = Die(20)
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()
die_6.roll_die()

die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()
die_10.roll_die()

die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()
die_20.roll_die()




