# India States Guessing Game

This project is a Python-based interactive game where you guess the names of Indian states and union territories. When you guess correctly, the state name is displayed on a map of India using Turtle graphics. The game keeps track of your score and shows praise if you guess all states correctly. At the end, it also saves the states you missed to a CSV file.

## Features

- Interactive guessing of Indian states and union territories
- Visual feedback on a map using Turtle graphics
- Score tracking out of 36
- Case-insensitive input handling
- List of missed states saved to `missed_states.csv`
- Congratulatory message for perfect score

## Requirements

- Python 3.x
- pandas
- turtle

## How to Run

1. Clone or download this repository.
2. Ensure you have `states_uts.csv` and `India.gif` in the project directory.
3. Install required libraries (if not already installed):

   ```bash
   pip install pandas
   ```

4. Run the game:

   ```bash
   python main.py
   ```

## Files

- `main.py` : Main game script
- `states_uts.csv` : CSV file containing state names and their coordinates
- `India.gif` : Map image used as background
- `missed_states.csv` : Generated after the game, contains states not guessed

## How It Works

- The game prompts you to enter the name of a state or union territory.
- If correct, the name is displayed at its location on the map.
- Your score is updated for each correct guess.
- If you guess all 36 correctly, a congratulatory message appears.
- After the game, any missed states are saved to `missed_states.csv`.

## License

This project is for educational purposes.
