# Reading words
infile = open("word.txt", "r")
for line in infile:
    line = line.strip()
    word_list = line.split()
    for word in word_list:
        print(word)
infile.close()

# Hangman Game
import random

# Guess and Turns
guesses = ""
turns = 10

# Open file
infile = open("hangman.txt", "r")
lines = infile.readlines()
words = random.choice(lines)

while turns > 0:
    failed = 0
    for letter in words:
        if letter in guesses:
            print(letter, end = '')
        else:
            print("_", end = '')
            failed += 1
    if failed == 0:
        print("Player wins!")
        break
    print("")
    guess = input("Guess the word: ")
    guesses += guess 
    if guess not in words:
        turns -= 1
        print("Wrong guess!")
        print(str(turns) + " chances left!")
        if turns == 0:
            print("Player loses! The answer was " + words)

infile.close()
