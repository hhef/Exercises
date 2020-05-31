import random

random_number = [random.randint(1, 9) for i in range(4)]

while True:
    input_numbers = input("Guess a number: ")
    user_numbers = []
    if input_numbers not in "1234567890":
        continue
    else:
        user_numbers.append(int(input_numbers))
    cows = 0
    bulls = 0

