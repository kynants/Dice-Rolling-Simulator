# PROJECT IDEA FROM:
# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

import time     # Used for pausing the program
import random   # Used for generating random numbers

# Prints out a message
print('Rolling the dice...')

# Pause for 2 seconds while the dice rolls.
time.sleep(2)

# "Constants"
MIN_NUM = 1
MAX_NUM = 6

for x in range(MIN_NUM, MAX_NUM):
    print(random.randint(MIN_NUM, MAX_NUM))