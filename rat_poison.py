# -*- coding: utf-8 -*-
"""
Created on Fri Feb  9 15:08:29 2024

@author: admin
"""

import random
from functools import reduce
import math
import sys
from pprint import pprint

num_drinks = 16
num_mouse = int(math.ceil(math.log(num_drinks, 2)))
print(f'Number of mouse needed: {num_mouse}')

# label the list of drink 0 to n-1
drink_labels = (list(range(num_drinks)))

# convert drink label to binary
drink_labels_bin = [{'num': bin(i)[2:].zfill(num_mouse), 'poison': False} for i in drink_labels]
poison_id = random.randint(0, num_drinks-1)

print('Put poison in cup (expected answer): ', poison_id, '\n')
poison = drink_labels_bin[poison_id]['poison'] = True

# create empty drink list for each mouse
mouse_drank_list = []
for i in range(num_mouse):
    mouse_drank_list.append([])


print('The list of drinks and one is poisoned: ', drink_labels_bin, '\n')


# calculate if each mouse drank the poison
for drink in drink_labels_bin:
    for ind, mouse in enumerate(mouse_drank_list):
        if drink['num'][ind] == '1':
            mouse.append(drink)

print('The list of drinks each mouse drank: ')
print(str(mouse_drank_list)[:1000] +  '...')
#pprint(mouse_drank_list)
print('\n')

poison_bin = ''
for ind, mouse_drank in enumerate(mouse_drank_list):
    # print('mouse drank: ', mouse_drank, '\n')
    result = reduce(lambda x, y: x or y['poison'], mouse_drank, False)

    print(f'Mouse {ind+1} drank poison (binary digit {ind+1}): {result} = {1 if result else 0}')
    poison_bin += str(int(result))

print(f'Binary digit is: "{poison_bin}"', '\n')
print('Convert back to decimal. The cup contains the poison is (calculated answer): ', int(poison_bin,2))


print('Cup was poisoned:  (expected answer) ', poison_id)