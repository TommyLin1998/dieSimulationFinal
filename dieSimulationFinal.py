#! /usr/bin/env python

print('''This program simulates rolling several dice.
The user can choose how many dice are rolled.

How many dice would you like to roll? 3
How many sides on the dice? 4

Die 1 shows: 2
Die 2 shows: 4
Die 3 shows: 4\n''')

import random

dice = int(raw_input('How many dice would you like to roll? '))

for dice in range(0, dice):
    sides = int(raw_input('How many sides on your die? #{}'.format(dice)))
    if sides <= 2:
        print('Are you sure it\'s a die?')
        break
    number = random.randint(1, sides)
    print('The die shows: {}'.format(number))
