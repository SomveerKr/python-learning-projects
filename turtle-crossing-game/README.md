# Turtle Crossing Game

A simple arcade-style game built with Python's Turtle graphics module. Inspired by the classic Frogger game, the player must help a turtle cross a busy road filled with moving cars. Each time the turtle reaches the top, the level increases and the cars move faster!

## Features

- Player-controlled turtle that moves up and down
- Randomly generated cars with increasing speed per level
- Scoreboard displaying the current level
- Game over detection on collision
- Simple, colorful graphics using the `turtle` module

## How to Play

- Use the **Up** and **Down** arrow keys to move the turtle
- Avoid the cars and reach the top of the screen to advance to the next level
- The game ends if the turtle collides with a car

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd turtle-crossing-game
   ```
2. **Install Python 3** (if not already installed):
   - Download from [python.org](https://www.python.org/downloads/)
3. **No external dependencies required!**
   - The game uses only Python's built-in `turtle` and `random` modules

## Running the Game

Run the following command in your terminal:

```bash
python main.py
```

A window will open. Use the arrow keys to play!

## File Structure

- `main.py` - Main game loop and setup
- `player.py` - Player turtle logic
- `car_manager.py` - Car creation, movement, and management
- `scoreboard.py` - Level display and game over logic

## Screenshots

_Add your own screenshots here!_

## Credits

- Developed as part of the "100 Days of Code: The Complete Python Pro Bootcamp" by Dr. Angela Yu
- Game concept inspired by the classic Frogger arcade game

## License

This project is open source and free to use for educational purposes.
