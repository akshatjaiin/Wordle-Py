import random

# ANSI color codes
GREEN = "\033[92m"  # Correct letter and correct position (*)
YELLOW = "\033[93m"  # Correct letter but wrong position (+)
RED = "\033[91m"  # Incorrect letter (-)
RESET = "\033[0m"  # Reset color to default

def generate_word():
    # A small sample list of 5-letter words
    word_list = ["apple", "grape", "pearl", "stone", "house", "plant"]
    return random.choice(word_list)

def get_feedback(guess, target_word):
    feedback = [""] * 5
    used_indices = set()

    # First, mark the correct letters in the correct position
    for i in range(5):
        if guess[i] == target_word[i]:
            feedback[i] = GREEN + guess[i] + RESET
            used_indices.add(i)

    # Then, mark the correct letters in the wrong position
    for i in range(5):
        if feedback[i] == "" and guess[i] in target_word:
            for j in range(5):
                if guess[i] == target_word[j] and j not in used_indices:
                    feedback[i] = YELLOW + guess[i] + RESET
                    used_indices.add(j)
                    break

    # Any remaining letters are incorrect
    for i in range(5):
        if feedback[i] == "":
            feedback[i] = RED + guess[i] + RESET

    return "".join(feedback)

def play_wordle():
    target_word = generate_word()
    attempts = 6

    print("Welcome to Wordle! Guess the 5-letter word.")
    
    for _ in range(attempts):
        guess = input("Enter your guess: ").lower()

        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        feedback = get_feedback(guess, target_word)
        print(f"Feedback: {feedback}")

        if guess == target_word:
            print("Congratulations! You guessed the word correctly.")
            return

    print(f"Sorry, you've run out of attempts. The word was: {target_word}")

if __name__ == "__main__":
    play_wordle()
