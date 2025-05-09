from random import randint

class Die:
    '''Initialize the die class'''

    def __init__(self, num_sides=6):
        #Six sided die
        self.num_sides = num_sides

    def roll(self):
        #Return the number of single die after rolled
        return randint(1, self.num_sides)




