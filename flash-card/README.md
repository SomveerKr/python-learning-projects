# Day 31: Flash Card App 🎴

A French-English flashcard application built with Python's Tkinter library as part of Angela Yu's 100 Days of Python course. This interactive learning tool helps users memorize French vocabulary through a spaced repetition approach.

## 📖 Project Overview

This flashcard application displays French words on the front of a card and automatically flips to show the English translation after 3 seconds. Users can mark words as "known" or "unknown," and the app intelligently tracks progress by saving words that still need to be learned.

## ✨ Features

- **Auto-Flip Cards**: Cards automatically flip from French to English after 3 seconds
- **Interactive Buttons**: 
  - ✅ Green checkmark: Mark word as known (removes from learning list)
  - ❌ Red cross: Mark word as unknown (keeps in learning list)
- **Progress Tracking**: Automatically saves words you still need to learn to `words_to_learn.csv`
- **Persistent Learning**: Resumes from where you left off by loading previously saved progress
- **Visual Design**: Clean, card-based UI with custom images for an engaging learning experience

## 🛠️ Technologies Used

- **Python 3.x**
- **Tkinter**: GUI framework for the flashcard interface
- **Pandas**: CSV file handling and data manipulation
- **Random**: Randomized word selection

## 📁 Project Structure

```
flash-card/
├── main.py                    # Main application file
├── data/
│   ├── french_words.csv       # Original dataset (101 French-English word pairs)
│   └── words_to_learn.csv     # Dynamically updated list of words to learn
└── images/
    ├── card_front.png         # Front card image (French side)
    ├── card_back.png          # Back card image (English side)
    ├── right.png              # "Known" button image
    └── wrong.png              # "Unknown" button image
```

## 🚀 How to Run

1. **Clone the repository** (if not already done):
   ```bash
   git clone <repository-url>
   cd day-31-flash-card
   ```

2. **Install required dependencies**:
   ```bash
   pip install pandas
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

## 🎮 How to Use

1. **Launch the app**: Run `main.py` to start the flashcard application
2. **View the French word**: A French word appears on the front of the card
3. **Wait for the flip**: After 3 seconds, the card automatically flips to show the English translation
4. **Mark your knowledge**:
   - Click the **green checkmark (✅)** if you knew the word
   - Click the **red cross (❌)** if you didn't know the word
5. **Track progress**: Words you mark as "known" are removed from your learning list
6. **Resume learning**: The app saves your progress automatically, so you can continue where you left off

## 🧠 Key Concepts Learned

This project reinforced several important Python concepts:

- **Tkinter GUI Development**: Creating windows, canvases, buttons, and handling events
- **File I/O with Pandas**: Reading and writing CSV files for data persistence
- **Exception Handling**: Using try-except blocks to handle missing files gracefully
- **Timers and Callbacks**: Using `window.after()` for delayed card flipping
- **Data Structures**: Working with dictionaries and lists for word management
- **State Management**: Tracking current card and managing global variables

## 📊 Dataset

The application includes 101 of the most common French words with their English translations. The dataset covers:
- Common verbs (chercher, donner, mettre)
- Nouns (ville, enfant, bureau)
- Adjectives (belle, vieux, nouvelle)
- Time expressions (aujourd'hui, matin, longtemps)

## 🔄 How Progress Tracking Works

1. **First Run**: Loads all 101 words from `french_words.csv`
2. **Marking Words as Known**: Removes the word from the learning list and saves to `words_to_learn.csv`
3. **Subsequent Runs**: Loads from `words_to_learn.csv` (if it exists) to continue where you left off
4. **Completion**: When all words are learned, the file will be empty or contain very few words

## 🎨 UI Components

- **Canvas**: 800x526px display area for flashcards
- **Background Color**: Soft mint green (#B1DDC6)
- **Fonts**: 
  - Title: Arial 40pt Italic
  - Word: Arial 60pt Bold
- **Card Flip Animation**: Smooth transition between front and back cards

## 🐛 Error Handling

The application includes robust error handling:
- **FileNotFoundError**: If `words_to_learn.csv` doesn't exist, it loads the original `french_words.csv`
- **Timer Management**: Cancels previous flip timers to prevent overlapping animations

## 📝 Future Enhancements

Potential improvements for this project:
- Add audio pronunciation for French words
- Implement different difficulty levels
- Add statistics dashboard (words learned, accuracy rate)
- Support for multiple languages
- Customizable flip delay time
- Keyboard shortcuts for faster interaction

## 📚 Course Information

This project is part of **Day 31** of [Angela Yu's 100 Days of Python](https://www.udemy.com/course/100-days-of-code/) course on Udemy.

**Topics Covered:**
- Tkinter GUI development
- Working with CSV files using Pandas
- Exception handling
- Event-driven programming

## 📄 License

This project is created for educational purposes as part of the 100 Days of Python course.

---

**Happy Learning! 🎓** Keep practicing and soon you'll master French vocabulary! 🇫🇷
