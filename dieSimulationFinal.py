#! /usr/bin/env python

import random

<<<<<<< HEAD
=======
dice = int(raw_input('How many dice would you like to roll? '))
>>>>>>> askDice
sides = int(raw_input('How many sides on your die? '))

for dice in range(0, sides + 1):
    number = random.randint(1, sides)
    print('The die shows: {}'.format(number))
