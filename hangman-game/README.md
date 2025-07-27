# Hangman Game

A classic Hangman word guessing game implemented in Python. This project was created as part of a Python learning journey (Day 7).

## 🎮 Game Description

Hangman is a word guessing game where players try to guess a hidden word by suggesting letters. The game provides visual feedback with ASCII art showing the hangman's progress, and players have 6 lives to guess the word correctly.

## ✨ Features

- **Classic Gameplay**: Traditional hangman rules with 6 lives
- **ASCII Art**: Visual representation of the hangman at different stages
- **Large Word List**: Extensive collection of words to guess from
- **User-Friendly Interface**: Clear prompts and feedback
- **Input Validation**: Handles duplicate guesses and invalid inputs
- **Real-time Feedback**: Shows current word progress and remaining lives

## 📁 Project Structure

```
day-7-hangman/
├── app.py              # Main game logic
├── hangman_art.py      # ASCII art for hangman stages and logo
├── hangman_words.py    # Word list for the game
└── README.md          # This file
```

## 🚀 Installation & Setup

1. **Prerequisites**: Make sure you have Python 3.x installed on your system.

2. **Clone or Download**: Get the project files in your local directory.

3. **Run the Game**:
   ```bash
   python app.py
   ```

## 🎯 How to Play

1. **Start the Game**: Run `python app.py` in your terminal
2. **Guess Letters**: Type a single letter and press Enter
3. **Track Progress**: Watch the hangman ASCII art and word display
4. **Win Condition**: Guess all letters in the word before running out of lives
5. **Lose Condition**: Run out of lives (6 total)

### Game Rules:

- You have 6 lives to guess the word
- Each incorrect guess reduces your life count
- Correct guesses reveal the letter in the word
- You can't guess the same letter twice
- The game ends when you either guess the word or run out of lives

## 📋 File Details

### `app.py`

- Main game loop and logic
- Handles user input and game state
- Manages lives, word display, and win/lose conditions

### `hangman_art.py`

- Contains ASCII art for the hangman stages (6 different states)
- Includes the game logo
- Provides visual feedback for the game

### `hangman_words.py`

- Large collection of words for the game
- Includes various categories of words
- Ensures diverse gameplay experience

## 🎨 Game Screenshots

The game features:

- ASCII art hangman that updates with each wrong guess
- Word display showing guessed letters and blanks
- Clear feedback messages for correct/incorrect guesses
- Life counter and game status

## 🛠️ Technical Details

- **Language**: Python 3.x
- **Dependencies**: No external libraries required (uses only built-in Python modules)
- **Architecture**: Modular design with separate files for art, words, and game logic

## 🎓 Learning Objectives

This project demonstrates:

- Working with lists and strings
- File imports and modular code structure
- User input handling and validation
- ASCII art and text-based UI
- Game state management
- Random word selection

## 🤝 Contributing

Feel free to enhance this project by:

- Adding more words to the word list
- Implementing difficulty levels
- Adding sound effects or colors
- Creating a GUI version
- Adding multiplayer functionality

## 📝 License

This is a learning project created as part of a Python course.

---

**Happy Gaming! 🎮**
