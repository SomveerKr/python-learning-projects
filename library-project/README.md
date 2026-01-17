# Library Management System - Flask Application

A simple yet functional library management web application built with Flask and SQLAlchemy. This application allows users to manage their personal book collection with features to add books, view their library, and edit book ratings.

## Features

- **View Library**: Display all books in your collection sorted alphabetically by title
- **Add Books**: Add new books with title, author, and rating information
- **Edit Ratings**: Update the rating of any book in your collection
- **SQLite Database**: Persistent storage using SQLAlchemy ORM
- **Clean Interface**: Simple and intuitive HTML templates

## Technologies Used

- **Flask**: Web framework for Python
- **Flask-SQLAlchemy**: SQL toolkit and ORM for database management
- **SQLite**: Lightweight database for storing book information
- **Jinja2**: Template engine (included with Flask)

## Project Structure

```
library-project/
│
├── main.py                 # Main application file with routes and database models
├── requirements.txt        # Project dependencies
├── instance/
│   └── books_rating.db    # SQLite database (created automatically)
└── templates/
    ├── index.html         # Home page displaying all books
    ├── add.html           # Form to add new books
    └── edit_rating.html   # Form to edit book ratings
```

## Database Schema

The application uses a single `Book` model with the following fields:

| Field  | Type   | Constraints                    |
|--------|--------|--------------------------------|
| id     | Integer| Primary Key                    |
| title  | String | Unique, Not Null (max 250 chars)|
| author | String | Not Null (max 250 chars)       |
| rating | Float  | Not Null                       |

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd "library-project"
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Access the application**:
   - Open your web browser and navigate to `http://127.0.0.1:5000/`

3. **Using the application**:
   - **Home Page**: View all books in your library
   - **Add Book**: Click "Add New Book" to add a new entry
   - **Edit Rating**: Click "Edit Rating" next to any book to update its rating

## Routes

| Route    | Methods    | Description                          |
|----------|------------|--------------------------------------|
| `/`      | GET        | Display all books in the library     |
| `/add`   | GET, POST  | Show add book form / Add new book    |
| `/edit`  | GET, POST  | Show edit form / Update book rating  |

## Key Features Explained

### Database Initialization
The database is automatically created when the application starts using SQLAlchemy's `create_all()` method within the application context.

### Book Ordering
Books are displayed in alphabetical order by title for easy browsing.

### Empty Library Handling
The home page displays a friendly message when no books are in the library.

### Rating System
Books are rated on a scale (typically 0-10), stored as floating-point numbers for precision.

## Development Notes

- The application runs in debug mode by default (`debug=True`)
- The SQLite database is stored in the `instance` folder
- Book titles must be unique in the database
- All fields (title, author, rating) are required when adding a book

## Future Enhancements

Potential improvements for this project:

- Add delete functionality for books
- Implement search and filter features
- Add book cover images
- Include additional fields (genre, publication year, ISBN)
- Add user authentication for multiple users
- Implement pagination for large libraries
- Add CSS styling for better UI/UX
- Add form validation and error handling

## Learning Objectives

This project demonstrates:

- Flask web framework fundamentals
- SQLAlchemy ORM usage with Flask-SQLAlchemy
- Database CRUD operations (Create, Read, Update)
- Flask routing and request handling
- Jinja2 template rendering
- Form data processing
- URL parameter handling

## License

This project is part of the Angela Yu 100 Days of Python course and is intended for educational purposes.

## Author

Created as part of Day 63 of the 100 Days of Python course by Angela Yu.
