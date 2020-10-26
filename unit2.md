## Programming Task 1:

In a game of guessing a number between 1-100 for two players, player A and player B. 
* The player A knows the number. 
* The player B is trying to guess with the least number of attempts.
* Player A can only reply to a guess from the other player B with “low”, “high”, or “That is the number”.

This programm represents player B

```.py
# This program guesses numbers from 1-100 a lot of times and 
# then prints the average number of attempts needed

# Inputs:
# N/A

# Outputs:
# average number of attempts needed

import random
number_of_variables = 100
number = random.randint(1,number_of_variables)
attempts = 0
all_attempts =[]
rand_numbers = []
avr_attempt = 0
number_of_cycles = 10000

for i in range(number_of_cycles):
    attempts = 0
    number = random.randint(1, number_of_variables)
    rand_numbers.append(number)

    guess = number_of_variables / 2 # 50

    if guess < rand_numbers[i]:  # bigger than 50
        attempts += 1
        guess = number_of_variables / 2 + number_of_variables / 4
        # 75
        if guess < rand_numbers[i]:  # bigger than 75
            attempts += 1
            while guess != rand_numbers[i]:
                guess += 1
                attempts += 1
            all_attempts.append(attempts)

        if guess > rand_numbers[i]:  # smaller than 75
            attempts += 1
            while guess != rand_numbers[i]:
                guess -= 1
                attempts += 1
            all_attempts.append(attempts)

        if number_of_variables / 2 + number_of_variables / 4 == number:  # number is 75
            attempts += 1
            all_attempts.append(attempts)

    if guess > rand_numbers[i]:  # smaller than 50
        attempts += 1
        guess = number_of_variables / 2 - number_of_variables / 4
        # 25
        if guess > rand_numbers[i]:  # smaller than 25
            attempts += 1
            while guess != rand_numbers[i]:
                guess -= 1
                attempts += 1
            all_attempts.append(attempts)

        if guess < rand_numbers[i]:  # bigger than 25
            attempts += 1
            while guess != rand_numbers[i]:
                guess += 1
                attempts += 1
            all_attempts.append(attempts)

        if (number_of_variables / 4) == rand_numbers[i]:  # number is 25
            attempts += 1
            all_attempts.append(attempts)

    if (number_of_variables / 2) == rand_numbers[i]:  # number is 50
        attempts += 1
        all_attempts.append(attempts)
print(all_attempts)
avr_attempt = sum(all_attempts)/number_of_cycles
print("Average number of attempts = ", avr_attempt)

```
