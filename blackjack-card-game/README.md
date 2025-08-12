# Blackjack Card Game

A simple command-line implementation of the classic Blackjack card game built in Python.

## 🎮 Game Description

This project is a Day 10 capstone project from Angela Yu's 100 Days of Python course. It's a text-based Blackjack game where you play against the computer (dealer) using standard Blackjack rules.

## 🎯 How to Play

### Objective
Get as close to 21 as possible without going over. Beat the dealer's hand to win!

### Game Rules
- **Card Values**: 
  - Number cards (2-10) = their face value
  - Face cards (J, Q, K) = 10
  - Ace = 11 (or 1 if going over 21)
- **Gameplay**:
  1. You and the dealer each start with 2 cards
  2. You can see one of the dealer's cards
  3. Choose to "hit" (get another card) or "stand" (keep your current hand)
  4. The dealer must hit until they have at least 17
  5. Closest to 21 without going over wins!

### Winning Conditions
- **You win** if:
  - Your score is closer to 21 than the dealer's
  - The dealer goes over 21 (busts)
- **Dealer wins** if:
  - Their score is closer to 21 than yours
  - You go over 21 (bust)
- **Draw** if both players have the same score

## 🚀 How to Run

1. **Prerequisites**: Make sure you have Python installed on your system
2. **Clone or download** the project files
3. **Run the game**:
   ```bash
   python main.py
   ```

## 📁 Project Structure

```
day-10-capstone-project/
├── main.py          # Main game logic
├── art.py           # ASCII art for the game logo
└── README.md        # This file
```

## 🎨 Features

- **ASCII Art Logo**: Beautiful card-themed ASCII art display
- **Interactive Gameplay**: User-friendly command-line interface
- **Realistic Rules**: Follows standard Blackjack rules
- **Score Tracking**: Real-time score calculation and display
- **Replay Option**: Play multiple games in one session

## 🎲 Game Flow

1. **Start**: Choose whether to play a game of Blackjack
2. **Deal**: You and the dealer receive 2 cards each
3. **Player Turn**: Decide to hit or stand
4. **Dealer Turn**: Dealer plays according to house rules
5. **Result**: Winner is determined and displayed
6. **Repeat**: Option to play another game

## 🛠️ Technical Details

- **Language**: Python 3
- **Dependencies**: None (uses only built-in Python libraries)
- **Key Libraries Used**:
  - `random`: For card shuffling and selection
  - Custom `art` module: For ASCII art display

## 🎯 Learning Objectives

This project demonstrates:
- **Function definition and usage**
- **Control flow** (if/else statements, loops)
- **List manipulation**
- **Random number generation**
- **User input handling**
- **Modular programming** (separate art.py file)
- **Game logic implementation**

## 🎮 Sample Gameplay

```
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           

~~~~~~~Do you want to play a game of Blackjack? Type 'y' or 'n': y
   Your cards: [10, 7], current score: 17
   Computer's first card: 8

Type 'y' to get another card, type 'n' to pass: n
   Your final hand: [10, 7], final score: 17
   Computer's final hand: [8, 6, 4], final score: 18

Computer Won! 😊
```

## 🤝 Contributing

This is a learning project, but feel free to:
- Report bugs or issues
- Suggest improvements
- Fork and modify for your own learning

## 📚 About

This project is part of the **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu on Udemy. It represents Day 10's capstone project, focusing on applying fundamental Python concepts to build a complete game.

---

**Happy Gaming! 🃏**
