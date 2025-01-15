# Advanced Forms with Flask-WTF

A Flask web application demonstrating advanced form handling using Flask-WTF, WTForms validators, and Flask-Bootstrap for styling. This project showcases secure form validation, user authentication simulation, and responsive UI design.

## Features

- **Form Validation**: Server-side validation using WTForms validators
- **Email Validation**: Built-in email format validation
- **Password Requirements**: Minimum 8-character password enforcement
- **CSRF Protection**: Automatic CSRF token generation and validation via Flask-WTF
- **Bootstrap Integration**: Responsive UI using Flask-Bootstrap 5
- **User Authentication**: Simulated login system with success/denied pages

## Technologies Used

- **Flask**: Web framework for Python
- **Flask-WTF**: Flask extension for form handling with CSRF protection
- **WTForms**: Form validation and rendering library
- **Flask-Bootstrap**: Bootstrap 5 integration for Flask
- **Python 3.x**: Programming language

## Project Structure

```
flask-advanced-forms/
│
├── main.py                 # Main application file with routes and form definition
├── requirements.txt        # Project dependencies
└── templates/              # HTML templates
    ├── base.html          # Base template with Bootstrap setup
    ├── index.html         # Home page
    ├── login.html         # Login form page
    ├── success.html       # Successful login page
    └── denied.html        # Access denied page
```

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd "flask-advanced-forms"
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
   pip install Flask Flask-WTF Flask-Bootstrap email-validator
   ```

## Configuration

> [!WARNING]
> The application currently uses a hardcoded secret key. For production use, always store sensitive information in environment variables.

**Current credentials** (for testing):
- Email: `admin@email.com`
- Password: `admin@123`

To use environment variables (recommended):
```python
import os
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-secret-key')
```

## Usage

1. **Start the Flask development server**:
   ```bash
   python main.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. **Navigate to the login page** and test the form validation:
   - Try submitting with invalid email format
   - Try submitting with password less than 8 characters
   - Try submitting with correct credentials to see success page
   - Try submitting with incorrect credentials to see denied page

## Form Validation Rules

The `LoginForm` class implements the following validation rules:

| Field    | Validators                          | Description                                    |
|----------|-------------------------------------|------------------------------------------------|
| Email    | `DataRequired()`, `Email()`         | Required field, must be valid email format     |
| Password | `DataRequired()`, `Length(min=8)`   | Required field, minimum 8 characters           |

## Routes

| Route     | Methods      | Description                                      |
|-----------|--------------|--------------------------------------------------|
| `/`       | GET          | Home page                                        |
| `/login`  | GET, POST    | Login form page with validation                  |

## Key Concepts Demonstrated

1. **Flask-WTF Forms**: Creating form classes with validators
2. **CSRF Protection**: Automatic security token handling
3. **Form Validation**: Server-side validation with user-friendly error messages
4. **Template Inheritance**: Using Jinja2 template inheritance with `base.html`
5. **Bootstrap Integration**: Rendering forms with Bootstrap 5 styling
6. **Request Methods**: Handling both GET and POST requests

## Code Highlights

### Form Definition with Validators
```python
class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[
        DataRequired(),
        Length(min=8, message="Password must be at least 8 characters long")
    ])
    submit = SubmitField(label='Log In')
```

### Form Validation in Route
```python
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Process validated form data
        email = form.email.data
        password = form.password.data
        # Authentication logic here
    return render_template('login.html', form=form)
```

## Learning Objectives

This project is part of Day 61 of the "100 Days of Code - Python" course and covers:

- ✅ Creating forms with Flask-WTF
- ✅ Implementing form validators (DataRequired, Email, Length)
- ✅ Using Flask-Bootstrap for responsive design
- ✅ Handling form submissions and validation errors
- ✅ Implementing CSRF protection
- ✅ Creating a basic authentication flow

## Future Enhancements

- [ ] Integrate with a real database for user storage
- [ ] Implement password hashing (e.g., using `werkzeug.security`)
- [ ] Add user registration functionality
- [ ] Implement session management for logged-in users
- [ ] Add "Remember Me" functionality
- [ ] Implement password reset feature
- [ ] Add more form fields (username, confirm password, etc.)
- [ ] Move configuration to environment variables

## Security Notes

> [!CAUTION]
> This is a learning project and should NOT be used in production without the following modifications:

1. **Secret Key**: Store in environment variables, not hardcoded
2. **Password Storage**: Never store passwords in plain text; use hashing (bcrypt, argon2)
3. **Database**: Use a proper database instead of hardcoded credentials
4. **HTTPS**: Always use HTTPS in production
5. **Rate Limiting**: Implement rate limiting to prevent brute force attacks

## License

This project is created for educational purposes as part of the Angela Yu 100 Days of Python course.

## Acknowledgments

- **Angela Yu**: Course instructor for "100 Days of Code - The Complete Python Pro Bootcamp"
- **Flask Documentation**: For comprehensive framework documentation
- **WTForms Documentation**: For form validation guidance
