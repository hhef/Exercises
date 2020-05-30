import random

with open('words.txt', 'r') as file:
    words = file.readlines()
    word = random.choice(words).strip()

player_letters = []
word_list = ["_" for i in range(len(word))]
print("Welcome to Hangman, here is your word:")
print(*word_list, sep=" ")
tries = 6

while tries >= 1:
    print("\nYour guessed letters: ", end="")
    print(*player_letters, sep=", ")
    print(f"You have {tries} more guesses")
    letter = input("Please guess a letter: ").upper()
