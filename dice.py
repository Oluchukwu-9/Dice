"""A simple die model
"""
from random import randint

class Die:
    """A class that simulates a dice 
    """

    def __init__(self):
        """Initialize the attribute of the Die class
        """        
        self.sides = 6


    def roll_die(self, number_of_sides):
        """Displays a random number between 1 and the number of sides

        Args:
            number_of_sides (int): The number of sides of a die
        """
        self.sides = number_of_sides
        chance = randint(1, self.sides)
        print(chance)
