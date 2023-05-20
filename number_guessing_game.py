#!/usr/bin/env python3

"""
number guessing game
"""

import random
import math

# taking inputs
lower = int(input("Enter lower bound:- "))
upper = int(input("Enter Upper bound:- "))

# Minimum number of guesses
minimum_of_guesses = math.log(upper - lower + 1, 2)

# generating random number between the lower and upper
x = random.randint(lower, upper)

# number of chances
print("\n\t You've only ", round(minimum_of_guesses),
      " chances to guess the integer!\n")

# Initializing the number of guesses
COUNT = 0

while COUNT < minimum_of_guesses:
    COUNT += 1

    # guessing number input
    guess = int(input("Enter a guess number: "))

    if x == guess:
        print(f"Congratulations you did it in {COUNT} try!")
        break

    if x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

if COUNT >= minimum_of_guesses:
    print(f"the number is {x}")
    print("Better luck next time!")
