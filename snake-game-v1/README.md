# Snake Game

A classic Snake game implementation in Python using the Turtle graphics library. This project is part of the "100 Days of Code: Python" course by Angela Yu.

## 🎮 Game Description

The Snake Game is a classic arcade game where the player controls a snake that moves around the screen. The goal is to eat food to grow longer while avoiding collisions with walls or the snake's own body.

## ✨ Features

- **Smooth Movement**: The snake moves continuously in the direction specified by arrow keys
- **Directional Control**: Use arrow keys to change the snake's direction
- **Collision Prevention**: The snake cannot reverse direction instantly (prevents self-collision)
- **Visual Graphics**: Clean, black background with white snake segments
- **Responsive Controls**: Real-time keyboard input handling

## 🛠️ Technologies Used

- **Python 3.x**
- **Turtle Graphics Library** - For game graphics and screen management

## 📁 Project Structure

```
day-20-snake-game/
├── main.py          # Main game loop and screen setup
├── snake.py         # Snake class implementation
└── README.md        # Project documentation
```

## 🚀 Installation

1. **Clone or download** this project to your local machine
2. **Ensure Python 3.x** is installed on your system
3. **No additional dependencies** required - uses only Python's built-in turtle library

## 🎯 How to Play

1. **Run the game**:
   ```bash
   python main.py
   ```

2. **Game Controls**:
   - **↑ Up Arrow**: Move snake upward
   - **↓ Down Arrow**: Move snake downward
   - **← Left Arrow**: Move snake leftward
   - **→ Right Arrow**: Move snake rightward

3. **Game Rules**:
   - The snake moves continuously in the current direction
   - Use arrow keys to change direction
   - The snake cannot reverse direction instantly
   - Click on the game window to exit

## 📋 Code Overview

### `main.py`
- Sets up the game screen (600x600 pixels, black background)
- Creates a Snake instance
- Implements the main game loop
- Handles keyboard input and screen updates

### `snake.py`
- **Snake Class**: Manages the snake's behavior and appearance
- **Initial Setup**: Creates a 3-segment snake at starting positions
- **Movement Logic**: Implements smooth movement with proper segment following
- **Direction Control**: Handles directional changes with collision prevention

### Key Features:
- **STARTING_POSITIONS**: Defines initial snake segment positions
- **MOVE_DISTANCE**: Controls how far the snake moves each step
- **Direction Constants**: UP, DOWN, LEFT, RIGHT angles for movement
- **Collision Prevention**: Prevents the snake from reversing direction instantly

## 🎨 Game Mechanics

- **Movement**: The snake's head moves forward, and each segment follows the one in front of it
- **Direction Changes**: Arrow keys change the snake's heading
- **Smooth Animation**: Screen updates are controlled for smooth movement
- **Performance**: Screen tracer is disabled for better performance

## 🔧 Customization

You can easily modify the game by adjusting these constants in `snake.py`:
- `STARTING_POSITIONS`: Change initial snake position
- `MOVE_DISTANCE`: Adjust movement speed
- Screen dimensions in `main.py`
- Colors and visual elements

## 🎓 Learning Objectives

This project demonstrates:
- Object-oriented programming with Python classes
- Game loop implementation
- Event handling (keyboard input)
- Graphics programming with Turtle
- Animation and timing control

## 📝 Future Enhancements

Potential improvements for this snake game:
- Add food spawning and eating mechanics
- Implement score tracking
- Add game over conditions (wall/self collision)
- Include sound effects
- Add different difficulty levels
- Implement high score system

## 👨‍💻 Author

This project is part of the "100 Days of Code: Python" course by Angela Yu.

## 📄 License

This project is for educational purposes as part of the Python learning course.
