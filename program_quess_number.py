"""
You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user,
will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.
"""

import random

from_list = [0]
to_list = [101]
guess = 1
my_number = int(input("Give a number: "))
comp_number = random.randint(from_list[-1] + 1, to_list[0] - 1)
print(f"Guessing number: {comp_number}, tries: {guess}")

while True:

    hilow = input("too low, too high or this is the number: ")
    if hilow == "too high":
        from_list.append(comp_number)
        from_list = sorted(from_list)
        comp_number = random.randint(from_list[-1] + 1, to_list[0] - 1)
    elif hilow == "too low":
        to_list.append(comp_number)
        to_list = sorted(to_list)
        comp_number = random.randint(from_list[-1] + 1, to_list[0] - 1)
    elif hilow == "this is the number":
        print(f"I guessed {comp_number}, won in {guess} tries")
        break

    guess += 1
    print(f"Guessing number: {comp_number}, tries: {guess}")
