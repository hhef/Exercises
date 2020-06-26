"""
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is
a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the
correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the
user at the end.
"""

import random

random_number = [random.randint(1, 9) for i in range(4)]


def game():
    while True:
        try:
            input_numbers = input("Guess a 4 digit number between 0 to 9: ")
            user_numbers = []
            for i in input_numbers:
                if i not in "1234567890" or len(input_numbers) != 4:
                    game()
                user_numbers.append(int(i))

            cows = 0
            bulls = 0
            for index in range(4):
                if user_numbers[index] == random_number[index]:
                    cows += 1
                elif user_numbers[index] in random_number:
                    bulls += 1

            if cows == 4:
                print("cg dudz")
                break

            print(f"{cows} cows, {bulls} bulls")
            print(f"Last guess: {input_numbers}")
        except:
            break


game()
