# Quiz Application

A simple command-line quiz application built in Python that presents True/False questions to users and tracks their score.

## Description

This project is a quiz game that loads questions from a predefined dataset and presents them one by one to the user. The user answers each question with "True" or "False", and the application provides immediate feedback on whether their answer was correct. At the end of the quiz, the user's final score is displayed.

## Features

- Interactive command-line interface
- True/False question format
- Real-time score tracking
- Immediate feedback on answers
- Final score display
- Modular code structure with separate classes for different functionalities

## Project Structure

```
day-17/
├── main.py              # Main application entry point
├── data.py              # Quiz questions dataset
├── question_model.py    # Question class definition
├── quiz_brain.py        # Quiz logic and scoring system
└── README.md           # This file
```

## Files Description

### `main.py`
The main entry point of the application. It:
- Loads questions from the dataset
- Creates a question bank
- Initializes the quiz brain
- Runs the quiz loop
- Displays final results

### `data.py`
Contains a list of quiz questions in JSON format. Each question includes:
- Question text
- Correct answer (True/False)
- Category
- Difficulty level
- Type

### `question_model.py`
Defines the `Question` class with:
- `text`: The question text
- `answer`: The correct answer

### `quiz_brain.py`
Contains the `QuizBrain` class that manages:
- Question progression
- Score tracking
- Answer validation
- User interaction

## How to Run

1. Make sure you have Python installed on your system
2. Navigate to the project directory
3. Run the application:

```bash
python main.py
```

## How to Play

1. The application will present questions one by one
2. For each question, type either "True" or "False" (case-insensitive)
3. Press Enter to submit your answer
4. You'll receive immediate feedback on whether your answer was correct
5. Your current score will be displayed after each question
6. Continue until all questions are answered
7. Your final score will be displayed at the end

## Example Output

```
Q.1: In Terraria, you can craft the Cell Phone pre-hardmode. (True/False)?: True
You got it right.
Correct answers is: True
Your score is: 1/1

Q.2: In the periodic table, Potassium's symbol is the letter K. (True/False)?: False
You got it wrong.
Correct answers is: True
Your score is: 1/2

...

You have completed the quiz.
Your final score is 8/12
```

## Requirements

- Python 3.x
- No external dependencies required

## Customization

To add your own questions, modify the `question_data` list in `data.py`. Each question should follow this format:

```python
{
    "type": "boolean",
    "difficulty": "easy",
    "category": "Your Category",
    "question": "Your question text here?",
    "correct_answer": "True",  # or "False"
    "incorrect_answers": ["False"]  # or ["True"]
}
```

## Learning Objectives

This project demonstrates:
- Object-oriented programming concepts
- Class design and implementation
- Data structures (lists, dictionaries)
- User input handling
- Control flow and loops
- Modular code organization

## Author

This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp" course by Angela Yu.

## License

This project is for educational purposes.
