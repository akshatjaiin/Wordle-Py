# 🟩 Wordle Clone in Python 🟨

This is a command-line Wordle game built in Python, inspired by the popular word puzzle game. The goal is to guess a 5-letter word within 6 attempts. With each guess, you'll receive feedback on how close your guess is to the actual word. 

## 🎮 How to Play

- **Guess the Word**: The game selects a random 5-letter word from a list, and you have 6 attempts to guess it.
- **Feedback Colors**:
  - 🟩 **Green**: The letter is in the correct position.
  - 🟨 **Yellow**: The letter is in the word but in the wrong position.
  - ⬜ **White**: The letter is not in the word.

## ✨ Features

- **Word Validation**: The game only accepts valid 5-letter words from a predefined list.
- **Command-Line Interface**: A simple text-based UI that prints feedback for each guess.
- **Replayability**: The word is chosen randomly from a list, making each game unique.

## 🛠️ Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/wordle-clone-python.git
    cd wordle-clone-python
    ```
2. **Requirements**:
    - Python 3.x
    - `tabulate` library (Install via `pip install tabulate`)

3. **Add your word list**:
    - The game requires a list of 5-letter words in a file named `words.txt`. Each word should be on a new line.

## 🚀 How to Run

To start the game, simply run the `main.py` script:

```bash
python main.py
Enter the word: crane
------------------
|  c  |  r  |  a  |  n  |  e  |
------------------
Enter the word: slate
------------------
|  c  |  r  |  a  |  n  |  e  |
|  s  |  l  |  a  |  t  |  e  |
------------------

Word: grace
You find the word in 4 tries
💡 How It Works
The game uses the random.choice() function to select a word from the words.txt file.
Players input a 5-letter word, which is validated against the word list.
Feedback is provided using colored text to indicate how close the guess is to the target word.
After 6 attempts or a correct guess, the game ends.
🛠️ Code Breakdown
get_input(words): Validates the player's input, ensuring it is a 5-letter word from the provided word list.
wordle(word, words): Manages the game loop, providing feedback after each guess.
main(): Initializes the game by loading the word list and starting the game loop.
🧑‍💻 Contributions
Feel free to fork this repository, submit pull requests, or open issues for any bugs or feature requests.


Happy guessing! 🎉

This README covers all the essential details about your Wordle clone, including how to play, instally 
