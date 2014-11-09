#! /usr/bin/env python

import random

dice = int(raw_input('How many dice would you like to roll? '))

for dice in range(0, dice):
    sides = int(raw_input('How many sides on your die? #{}'.format(dice)))
    number = random.randint(1, sides)
    print('The die shows: {}'.format(number))
