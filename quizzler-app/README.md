# Quizzler App 🧠

A GUI-based quiz application built with Python's Tkinter library that fetches trivia questions from the Open Trivia Database API. This project was created as part of **Day 34** of Angela Yu's 100 Days of Python course.

## 📋 Description

Quizzler is an interactive True/False quiz game with a clean graphical user interface. The app fetches 10 computer science trivia questions from the Open Trivia Database API and presents them one at a time. Users can answer by clicking True (✓) or False (✗) buttons, and receive immediate visual feedback on their answers.

## ✨ Features

- **API Integration**: Fetches real-time trivia questions from the Open Trivia Database
- **GUI Interface**: Clean and intuitive Tkinter-based user interface
- **Visual Feedback**: Canvas changes color (green for correct, red for incorrect) after each answer
- **Score Tracking**: Real-time score display that updates as you progress
- **Question Management**: Object-oriented design with separate classes for questions, quiz logic, and UI

## 🛠️ Technologies Used

- **Python 3.x**
- **Tkinter** - GUI framework
- **Requests** - HTTP library for API calls
- **Open Trivia Database API** - Question source

## 📁 Project Structure

```
day-34-quizzler-app/
├── main.py              # Main application entry point
├── data.py              # API integration and data fetching
├── question_model.py    # Question class definition
├── quiz_brain.py        # Quiz logic and answer checking
├── ui.py                # GUI interface using Tkinter
└── images/
    ├── true.png         # True button image
    └── false.png        # False button image
```

## 🎮 How to Run

1. **Install required dependencies**:
   ```bash
   pip install requests
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

3. **Play the quiz**:
   - Read each question displayed on the screen
   - Click the ✓ button for True or ✗ button for False
   - Watch the background change color for instant feedback
   - Track your score in the top-right corner
   - Complete all 10 questions to see your final score

## 🎯 Learning Objectives

This project demonstrates:

- **API Integration**: Making HTTP requests and handling JSON responses
- **GUI Development**: Building interactive interfaces with Tkinter
- **Object-Oriented Programming**: Separating concerns into multiple classes
- **Event-Driven Programming**: Handling button clicks and user interactions
- **HTML Entity Handling**: Processing special characters in API responses
- **Error Handling**: Managing API requests with proper error checking

## 🔧 Customization

You can customize the quiz by modifying the parameters in `data.py`:

```python
parameters = {
    "amount": 10,        # Number of questions (1-50)
    "category": 18,      # Category ID (18 = Computer Science)
    "type": "boolean"    # Question type (boolean, multiple)
}
```

Visit [Open Trivia Database](https://opentdb.com/api_config.php) to explore different categories and difficulty levels.

## 📸 Features Breakdown

- **Question Display**: Questions are shown in an italic Arial font on a white canvas
- **Interactive Buttons**: Image-based buttons for True/False answers
- **Color Feedback**: Green background for correct answers, red for incorrect
- **Score Counter**: Updates automatically after each question
- **Completion Message**: Displays final score when all questions are answered

## 🎓 Course Context

This project is part of **Day 34** of the [100 Days of Python](https://www.udemy.com/course/100-days-of-code/) course by Angela Yu, focusing on API integration with GUI applications and building practical, interactive programs.

## 📝 Notes

- The app fetches questions from the Open Trivia Database, so an internet connection is required
- Questions are randomly selected from the Computer Science category
- The quiz consists of 10 True/False questions per session
- HTML entities in questions are properly decoded for display

---

**Location**: `till-40/day-34-quizzler-app/`
