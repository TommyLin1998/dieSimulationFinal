#! /usr/bin/env python

import random

sides = int(raw_input('How many sides on your die? '))

number = random.randint(1, sides)

print('The die shows: {}'.format(number))
