#! /usr/bin/env python

import random

dice = int(raw_input('How many dice would you like to roll? '))
sides = int(raw_input('How many sides on your die? '))

for dice in range(0, sides + 1):
    number = random.randint(1, sides)
    print('The die shows: {}'.format(number))
