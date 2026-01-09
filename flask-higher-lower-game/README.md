# Flask Higher Lower Game 🎮

A simple number guessing game built with Flask where players try to guess a randomly generated number between 0 and 10. The application provides visual feedback with GIFs and color-coded messages based on the player's guess.

## 📋 Description

This is a web-based guessing game that demonstrates Flask routing and dynamic URL handling. The server generates a random number, and players navigate to different URLs to make their guesses. The game provides immediate feedback with fun GIF animations and colored text to indicate whether the guess is too high, too low, or correct.

## ✨ Features

- **Random Number Generation**: Server generates a random number between 0 and 10 at startup
- **Dynamic Routing**: Players guess by navigating to `/<number>` URLs
- **Visual Feedback**: Different GIFs and colored messages for each outcome:
  - 🟢 **Correct**: Green message with success GIF
  - 🔴 **Too Low**: Red message with "try again" GIF
  - 🟣 **Too High**: Purple message with "aim lower" GIF
- **Clean UI**: Simple HTML interface with embedded GIF animations

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Flask

### Installation

1. Install Flask if you haven't already:
```bash
pip install flask
```

2. Navigate to the project directory:
```bash
cd flask-higher-lower-game
```

### Running the Application

1. Run the Flask application:
```bash
python game.py
```

2. Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

3. You'll see the welcome page with instructions to guess a number between 0 and 10.

## 🎯 How to Play

1. Start the application and visit the home page
2. Make a guess by adding your number to the URL (e.g., `http://127.0.0.1:5000/5`)
3. The game will respond with:
   - A **green** message if you guessed correctly
   - A **red** message if your guess is too low
   - A **purple** message if your guess is too high
4. Keep guessing until you find the correct number!

## 📁 Project Structure

```
day-55-flask-higher-lower-game/
└── game.py          # Main Flask application with game logic
```

## 🛠️ Technical Details

### Routes

- **`/`**: Home page displaying game instructions and a welcome GIF
- **`/<int:guess_number>`**: Dynamic route that accepts integer guesses and returns feedback

### Key Functions

- **`hello_world()`**: Renders the home page with game instructions
- **`guess_number(guess_number)`**: Processes player guesses and returns appropriate feedback
- **`generate_message(message_text, message_color, message_image)`**: Helper function to generate HTML responses with styled messages and GIFs

## 🎨 Customization

You can customize the game by modifying:

- **Number Range**: Change the `random.randint(0, 10)` values to adjust difficulty
- **Messages**: Update `too_low_message`, `too_high_message`, and `correct_message` variables
- **GIFs**: Replace the Giphy URLs with your preferred animations
- **Colors**: Modify the color parameters in the `guess_number()` function

## 📚 Learning Objectives

This project demonstrates:

- Flask web framework basics
- Dynamic URL routing with variable rules
- Type conversion in URL parameters (`<int:guess_number>`)
- HTML generation from Python
- Random number generation
- Conditional logic and control flow

## 🔧 Development

The application runs in debug mode by default, which provides:

- Auto-reload on code changes
- Detailed error messages
- Interactive debugger

To disable debug mode for production, change:
```python
app.run(debug=False)
```

## 📝 Notes

- The random number is generated once when the server starts and remains the same until the server is restarted
- The number is printed to the console for debugging purposes
- Each guess requires navigating to a new URL

## 🤝 Contributing

This is a learning project from the Angela Yu 100 Days of Python course. Feel free to fork and experiment with your own variations!

## 📄 License

This project is part of a learning curriculum and is available for educational purposes.
