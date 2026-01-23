# Flask Authentication - User Registration & Login System

A secure Flask web application demonstrating user authentication with registration, login, and protected routes. This project implements password hashing, session management, and access control using Flask-Login and SQLAlchemy.

## Features

- **User Registration**: New users can create accounts with email, name, and password
- **Secure Password Storage**: Passwords are hashed using Werkzeug's `pbkdf2:sha256` algorithm
- **User Login**: Registered users can log in with email and password
- **Session Management**: Flask-Login handles user sessions and authentication state
- **Protected Routes**: Access control for authenticated users only
- **Flash Messages**: User feedback for login errors and registration issues
- **File Download**: Authenticated users can download protected files
- **Duplicate Email Prevention**: Checks for existing email addresses during registration

## Technologies Used

- **Flask**: Web framework
- **Flask-SQLAlchemy**: Database ORM
- **Flask-Login**: User session management
- **Werkzeug Security**: Password hashing and verification
- **SQLite**: Database for storing user information

## Project Structure

```
flask-auth/
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── instance/
│   └── users.db           # SQLite database (created automatically)
├── static/
│   ├── css/               # Stylesheets
│   └── files/             # Protected downloadable files
│       └── cheat_sheet.pdf
└── templates/
    ├── base.html          # Base template
    ├── index.html         # Home page
    ├── register.html      # Registration form
    ├── login.html         # Login form
    └── secrets.html       # Protected page for authenticated users
```

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd "flask-auth"
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

   Required packages:
   - Flask
   - Flask-SQLAlchemy
   - Flask-Login
   - Werkzeug

## Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:5000/`

3. **Register a new account**:
   - Click "Register" on the home page
   - Enter your name, email, and password
   - Submit the form to create your account

4. **Login**:
   - Click "Login" on the home page
   - Enter your registered email and password
   - Access the protected "Secrets" page upon successful login

5. **Download protected files**:
   - Once logged in, navigate to the Secrets page
   - Click "Download Your File" to access protected content

## Application Routes

| Route | Method | Description | Authentication Required |
|-------|--------|-------------|------------------------|
| `/` | GET | Home page | No |
| `/register` | GET, POST | User registration | No |
| `/login` | GET, POST | User login | No |
| `/secrets` | GET | Protected secrets page | Yes |
| `/logout` | GET | User logout | Yes |
| `/download` | GET | Download protected file | Yes |

## Database Schema

### User Table

| Column | Type | Constraints |
|--------|------|-------------|
| id | Integer | Primary Key |
| email | String(100) | Unique, Not Null |
| password | String(100) | Not Null (hashed) |
| name | String(1000) | Not Null |

## Security Features

1. **Password Hashing**: All passwords are hashed using `pbkdf2:sha256` with 8 iterations
2. **Session Management**: Flask-Login manages user sessions securely
3. **Protected Routes**: `@login_required` decorator prevents unauthorized access
4. **Duplicate Prevention**: Email uniqueness is enforced at both database and application levels
5. **Flash Messages**: Secure feedback without exposing sensitive information

## Key Implementation Details

### User Model
The `User` class inherits from both `UserMixin` (Flask-Login) and `db.Model` (SQLAlchemy), providing:
- Session management methods (`is_authenticated`, `is_active`, `get_id`)
- Database ORM functionality

### Password Security
```python
# Registration: Hash password
hashed_password = generate_password_hash(password, "pbkdf2:sha256", 8)

# Login: Verify password
check_password_hash(user.password, password)
```

### Login Manager
Flask-Login's `LoginManager` is configured with a user loader callback that retrieves users from the database by ID.

## Learning Objectives

This project demonstrates:
- User authentication implementation in Flask
- Password hashing and security best practices
- Database integration with SQLAlchemy
- Session management with Flask-Login
- Route protection and access control
- Form handling and validation
- Flash messaging for user feedback

## Future Enhancements

- Email verification for new registrations
- Password reset functionality
- Remember me functionality
- User profile management
- OAuth integration (Google, GitHub, etc.)
- Two-factor authentication (2FA)
- Password strength requirements
- Rate limiting for login attempts

## Notes

- The `SECRET_KEY` in the code should be changed to a secure random value in production
- The database is created automatically when the application first runs
- Flash messages provide user feedback for errors and successful operations
- The application uses SQLite for simplicity; consider PostgreSQL or MySQL for production

## License

This project is part of the Angela Yu 100 Days of Python course.
