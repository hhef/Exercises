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

    for i in range(len(word)):
        if letter == word[i]:
            word_list[i] = letter

    if letter in player_letters:
        print("You already tried this letter, please pick another one")
    elif letter not in word:
        tries -= 1

    if "_" not in word_list or letter == word:
        print(f"cg, you won, the word was {word}")
        break

    player_letters.append(letter)
    print(*word_list, sep=" ")
