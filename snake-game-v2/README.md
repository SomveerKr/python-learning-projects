# Snake Game 🐍

A classic Snake game implemented in Python using the `turtle` graphics library. This project is part of the 100 Days of Code: The Complete Python Pro Bootcamp by Dr. Angela Yu (Day 21).

## Features

- Classic snake gameplay: eat food, grow longer, avoid walls and your own tail
- Score tracking and game over display
- Responsive keyboard controls
- Simple, clean UI

## Object-Oriented Programming (OOP) Concepts

This project is designed to demonstrate OOP principles in Python, including:

- **Classes and Objects:** The game is structured using multiple classes (`Snake`, `Food`, `Scoreboard`), each encapsulating related data and behavior.
- **Class Inheritance:** Both `Food` and `Scoreboard` classes inherit from the `Turtle` class provided by the `turtle` module, showcasing how to extend and customize built-in classes.
- **Encapsulation:** Game logic and state are managed within class methods and attributes.

## File Structure

- `main.py` — Main game loop and event handling
- `snake.py` — Snake class (movement, growth, direction)
- `food.py` — Food class (random placement, inherits from Turtle)
- `scoreboard.py` — Scoreboard class (score display, inherits from Turtle)

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd snake-game
   ```

## How to Play

1. Run the game:
   ```bash
   python main.py
   ```
2. Use the arrow keys to control the snake:
   - Up: ↑
   - Down: ↓
   - Left: ←
   - Right: →
3. Eat the blue food to grow and increase your score. Avoid hitting the walls or your own tail!

## Screenshots

_Add your own screenshots here if desired._

## License

This project is for educational purposes as part of the 100 Days of Code Python Bootcamp.
