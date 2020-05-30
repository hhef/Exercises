import random

with open('words.txt', 'r') as file:
    words = file.readlines()
    word = random.choice(words).strip()