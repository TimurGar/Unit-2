## Programming Task 1:

In a game of guessing a number between 1-100 for two players, player A and player B. 
* The player A knows the number. 
* The player B is trying to guess with the least number of attempts.
* Player A can only reply to a guess from the other player B with “low”, “high”, or “That is the number”.

This programm was created for Player B

```.py
# This is a program that allows you to guess a number from 1-100
# Inputs:
# Your guess what is the number

# Outputs:
# program prints: High, Low, That is the number

import random
number = random.randint(1,100)

while True:
    guess = int(input("Player B, write the number: "))

    if guess > number:
        print("High")
    if guess < number:
        print("Low")
    if guess == number:
        print("That is the number")
        break

```
