import random

with open('words.txt', 'r') as file:
    words = file.readlines()
    word = random.choice(words).strip()

player_letters = []
word_list = ["_" for i in range(len(word))]
print("Welcome to Hangman, here is your word:")
print(*word_list, sep=" ")
tries = 6