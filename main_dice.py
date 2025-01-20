"""A dice simulation."""

import dice

# makeing a 6 sided (in this case the default value ofthe attribute) and roll
# it ten times
six_sides = []
while len(six_sides) != 10:
    six = dice.Die() # created an instance of the Die class

    six_side = six.roll_die()
    six_sides.append(six_side)

print(six_sides)

# making a 10 sided-die and rolling it ten times
ten_sideds = []
while len(ten_sideds) != 10:
    ten = dice.Die(10) # created an instance of the Die class
    ten_sided = ten.roll_die()
    ten_sideds.append(ten_sided)

print(ten_sideds)

# Making a 20-sided die and rolling it 10 times
twenty_sideds = []
while len(twenty_sideds) != 10:
    twenty = dice.Die(20) # created an instance of the Die class
    twenty_sided = twenty.roll_die()
    twenty_sideds.append(twenty_sided)

print(twenty_sideds)
