# Python Learning Projects 🐍

Welcome to my Python learning journey! This repository contains all the projects I've built while following the **100 Days of Code: The Complete Python Pro Bootcamp** course by Angela Yu.

## 🎯 Learning Methodology

**Important Note**: I follow a unique learning approach where I:

1. **First, I build the projects** - I read the project requirements and attempt to build them independently
2. **Then, I watch the video solutions** - After completing my version, I watch Angela's video to understand different approaches and best practices
3. **Finally, I compare and learn** - I analyze the differences between my implementation and the course solution to deepen my understanding

This methodology helps me:

- Develop problem-solving skills independently
- Learn from mistakes and different approaches
- Build confidence in my coding abilities
- Understand multiple ways to solve the same problem

## 🚀 Projects in This Repository

### Day 7: Hangman Game 🎮

**Location**: `hangman-game/`

A classic word guessing game with ASCII art visualization. Players have 6 lives to guess a hidden word by suggesting letters one at a time.

### Day 8: Caesar Cipher 🔐

**Location**: `ceaser-cipher/`

A Python implementation of the classic Caesar Cipher encryption and decryption algorithm. Features interactive CLI, custom shift values, and ASCII art.

### Day 10: Blackjack Card Game 🃏

**Location**: `blackjack-card-game/`

Command-line Blackjack game played against a computer dealer with realistic rules. Features ASCII art, score tracking, and replay functionality.

### Day 15: Coffee Machine ☕

**Location**: `coffee-maker-v1/`

Coffee machine simulator with multiple drinks, payment system, and resource management. Features espresso, latte, and cappuccino with realistic pricing.

### Day 16: Coffee Machine v2 (OOP) ☕

**Location**: `coffee-maker-v2/`

Enhanced OOP-based coffee machine simulator with modular design. Features separate classes for CoffeeMaker, Menu, and MoneyMachine.

### Day 17: Quiz Game 🧠

**Location**: `quiz-game/`

Command-line True/False quiz app with real-time score tracking. Features modular OOP design with separate classes for logic and data.

### Day 20: Snake Game 🐍

**Location**: `snake-game-v1/`

Classic Snake game using Python's Turtle graphics. Features smooth movement, directional control, and collision prevention.

### Day 21: Snake Game v2 (Enhanced) 🐍

**Location**: `snake-game-v2/`

Enhanced Snake game with food spawning, score tracking, and high score persistence. Built with modular OOP design separating game logic elements.

### Day 22: Pong Game 🏓

**Location**: `pong-game/`

Classic two-player Pong game using Turtle graphics. Features real-time gameplay, score tracking, and local multiplayer with collision detection.

### Day 23: Turtle Crossing Game 🐢

**Location**: `turtle-crossing-game/`

Frogger-inspired arcade game where players help a turtle cross a busy road. Features level progression, increasing difficulty, and collision detection.

### Day 25: India States Guessing Game 🗺️

**Location**: `states-guessing-game/`

Interactive geography game to guess Indian states on a map with visual feedback. Tracks scores and generates a CSV file of missed states for learning.

### Day 31: Flash Card App 🎴

**Location**: `flash-card/`

French-English flashcard app with Tkinter and spaced repetition. Demonstrates GUI development, Pandas CSV handling, and state management.

### Day 32: Birthday Wisher 🎂

**Location**: `birthday_wisher/`

Automated birthday email sender using CSV data and personalized templates. Features Gmail SMTP integration and secure environment variable management.

### Day 34: Quizzler App 🧠

**Location**: `quizzler-app/`

GUI-based True/False quiz app using Tkinter and Open Trivia Database API. Features real-time scoring, visual feedback, and OOP design.

### Day 36: Stock News Alert 📈

**Location**: `stock-news-alert/`

Automated stock monitor tracking TSLA prices to send SMS alerts via Twilio on significant changes. Uses Alpha Vantage and NewsAPI for data.

### Day 37: Habit Tracker 📊

**Location**: `habit-tracker/`

Habit tracking application using Pixela API to create visual activity graphs. Features user management, daily logging, and streak tracking.

### Day 38: Nutrition/Exercise Tracker 💪

**Location**: `nutritionix-api/`

Workout logger using Natural Language Processing to track exercises in Google Sheets. Input activities in plain text to auto-calculate calories and duration.

### Day 39: Flight Deals ✈️

**Location**: `flight-deals-finder/`

Flight deal tracker that monitors prices and sends alerts for low fares. Integrates Amadeus, Google Sheets, and Twilio.

### Day 40: Flight Club (Flight Deals v2) ✈️

**Location**: `flight-deals-finder-v2/`

An advanced flight tracker that handles stopovers and tracks user users. Features finding best deals and emailing all the users about the deals.


## 📁 Repository Structure

```
python-learning-projects/
├── README.md                    # This file
├── hangman-game/               # Day 7: Hangman Game
│   ├── app.py
│   ├── hangman_art.py
│   ├── hangman_words.py
│   └── README.md
├── ceaser-cipher/               # Day 8: Caesar Cipher
│   ├── ceaser-cipher.py
│   ├── art.py
│   └── README.md
├── blackjack-card-game/         # Day 10: Blackjack Card Game
│   ├── main.py
│   ├── art.py
│   └── README.md
├── coffee-maker-v1/             # Day 15: Coffee Machine
│   ├── coffee_machine.py
│   ├── menu.py
│   └── README.md
├── coffee-maker-v2/             # Day 16: Coffee Machine v2 (OOP)
│   ├── main.py
│   ├── coffee_maker.py
│   ├── menu.py
│   ├── money_machine.py
│   └── README.md
├── quiz-game/                   # Day 17: Quiz Game
│   ├── main.py
│   ├── data.py
│   ├── question_model.py
│   ├── quiz_brain.py
│   └── README.md
├── snake-game-v1/               # Day 20: Snake Game
│   ├── main.py
│   ├── snake.py
│   └── README.md
├── snake-game-v2/               # Day 21: Snake Game v2 (Enhanced)
│   ├── main.py
│   ├── snake.py
│   ├── food.py
│   ├── scoreboard.py
│   ├── high_score.txt
│   └── README.md
├── pong-game/                   # Day 22: Pong Game
│   ├── main.py
│   ├── ball.py
│   ├── paddle.py
│   ├── scoreboard.py
│   └── README.md
├── turtle-crossing-game/        # Day 23: Turtle Crossing Game
│   ├── main.py
│   ├── player.py
│   ├── car_manager.py
│   ├── scoreboard.py
│   └── README.md
├── states-guessing-game/        # Day 25: India States Guessing Game
│   ├── main.py
│   ├── states_uts.csv
│   ├── India.gif
│   ├── missed_states.csv
│   └── Readme.md
├── flash-card/                  # Day 31: Flash Card App
│   ├── main.py
│   ├── data/
│   │   ├── french_words.csv
│   │   ├── words_to_learn.csv
│   │   ├── images/
│   └── README.md
├── birthday_wisher/             # Day 32: Birthday Wisher
│   ├── main.py
│   ├── birthdays.csv
│   ├── .env
│   ├── letter_templates/
│   └── README.md
├── quizzler-app/                # Day 34: Quizzler App
│   ├── main.py
│   ├── data.py
│   ├── question_model.py
│   ├── quiz_brain.py
│   ├── ui.py
│   ├── images/
│   └── README.md
├── stock-news-alert/            # Day 36: Stock News Alert
│   ├── main.py
│   ├── .env
│   └── README.md
├── habit-tracker/               # Day 37: Habit Tracker
│   ├── main.py
│   ├── .env
│   ├── .gitignore
│   └── README.md
├── nutritionix-api/            # Day 38: Nutrition/Exercise Tracker
│   ├── main.py
│   ├── .env
│   ├── .gitignore
│   └── README.md
├── flight-deals-finder/         # Day 39: Flight Deals
│   ├── main.py
│   ├── data_manager.py
│   ├── flight_search.py
│   ├── flight_data.py
│   ├── notification_manager.py
│   └── README.md
├── flight-deals-finder-v2/      # Day 40: Flight Club
│   ├── main.py
│   ├── data_manager.py
│   ├── flight_search.py
│   ├── flight_data.py
│   ├── notification_manager.py
│   └── README.md
├── [future-project-folders]/   # Additional projects will be added here
└── .gitignore                 # Git ignore file
```

## 🤝 Contributing

This is a personal learning repository, but I welcome:

- Suggestions for improvements
- Bug reports
- Code review feedback
- Learning tips and resources

## 📝 License

This repository is for educational purposes as part of the 100 Days of Code course. All projects are created for learning and personal development.

---

**Happy Coding! 🚀**

_"The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie_
