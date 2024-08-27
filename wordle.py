from random import choice
from tabulate import tabulate
import tkinter as tk

def get_input(words):
    while True:
        guess = input("Enter the word: ").replace(" ", "").lower()
        if len(guess) == 5 and isinstance(guess, str) and guess in words:
            return guess



def wordle(word, words):
    combo = []
    for i in range(6):
        row = []
        guess = get_input(words)
        if guess == word:
            return i + 1
        for j in range(5):
            if guess[j] == word[j]:
                row.append(f"\033[97;102m {guess[j]} \033[0m")
            elif guess[j] in word:
                row.append(f"\033[91;103m {guess[j]} \033[0m")
            else:
                row.append(f"\033[90;107m {guess[j]} \033[0m")
        combo.append(row)
        print(tabulate(combo))
    print(f"Word: {word} ")
    return False


def main():
    with open("words.txt", "r") as file:
        words = [word.strip() for word in file.readlines()]
       

    word = choice(words)
    chance = wordle(word, words)
    if chance:
        print(f"You find the word in {chance} tries")
    



if __name__=="__main__":
    main()
