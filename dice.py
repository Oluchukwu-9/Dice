"""A simple die model."""

from random import randint

class Die:
    """A class that simulates a dice."""

    def __init__(self, sides=6):
        """Initialize the attribute of the Die class."""
        self.sides = sides

    def roll_die(self):
        """Display a random number between 1 and the number of sides."""
        chance = randint(1, self.sides)
        return chance
