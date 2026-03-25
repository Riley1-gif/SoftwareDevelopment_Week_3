# Challenge 2: Number Guessing Game
#Author: Riley
#Date: 03/06/2026

import random
number_to_guess = random.randint(1, 10)
guess = 0
number_of_attempts = 0
previous_guess = None

while guess != number_to_guess:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess != previous_guess:
        number_of_attempts += 1
    if guess < number_to_guess:
        print("Too low Try again.")
    elif guess > number_to_guess:
        print("Too high Try again.")
    else:
        print("Nice you guessed the number!")
        print(f"It took you {number_of_attempts} attempts to guess the number.")