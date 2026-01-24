# Blog with Users - Flask Application

🌐 **[Live Demo](https://codeveer-log.onrender.com/)** - Check out the deployed application!

A full-featured Flask blog application with user authentication, role-based access control, and commenting functionality. This project demonstrates advanced Flask concepts including user management, database relationships, and secure authentication.

## Features

### User Authentication
- **User Registration**: New users can create accounts with email validation
- **Secure Login**: Password hashing using Werkzeug's security features (PBKDF2-SHA256)
- **Session Management**: Flask-Login integration for persistent user sessions
- **Logout Functionality**: Secure user logout with session cleanup

### Blog Management
- **View All Posts**: Public homepage displaying all blog posts
- **Individual Post Pages**: Detailed view for each blog post
- **Admin-Only Post Creation**: Only admin users (user ID 1) can create new posts
- **Admin-Only Post Editing**: Restricted editing capabilities for administrators
- **Admin-Only Post Deletion**: Secure deletion with admin-only access
- **Rich Text Editor**: CKEditor integration for formatted blog content

### Commenting System
- **User Comments**: Authenticated users can comment on blog posts
- **Gravatar Integration**: Automatic avatar generation using Flask-Avatars
- **Comment Display**: Comments shown with author information and avatars
- **Login Protection**: Non-authenticated users are redirected to login before commenting

### Security Features
- **Role-Based Access Control**: Custom `@admin_only` decorator for protected routes
- **Password Hashing**: Secure password storage with salt
- **CSRF Protection**: Flask-WTF form validation and protection
- **403 Error Handling**: Proper authorization error responses

## Technology Stack

- **Flask**: Web framework
- **Flask-SQLAlchemy**: Database ORM with SQLite
- **Flask-Login**: User session management
- **Flask-Bootstrap**: UI styling with Bootstrap 5
- **Flask-CKEditor**: Rich text editor for blog content
- **Flask-WTF**: Form handling and validation
- **Flask-Avatars**: Gravatar integration for user avatars
- **WTForms**: Form validation with custom validators
- **Werkzeug**: Password hashing and security utilities
- **Python-dotenv**: Environment variable management

## Database Schema

### User Table
- `id`: Primary key
- `full_name`: User's full name
- `email`: Unique email address
- `password`: Hashed password
- **Relationships**: One-to-many with BlogPost and Comment

### BlogPost Table
- `id`: Primary key
- `title`: Unique post title
- `subtitle`: Post subtitle
- `date`: Publication date
- `body`: Post content (rich text)
- `img_url`: Header image URL
- `author_id`: Foreign key to User
- **Relationships**: Many-to-one with User, one-to-many with Comment

### Comment Table
- `id`: Primary key
- `text`: Comment content
- `author_id`: Foreign key to User
- `post_id`: Foreign key to BlogPost
- **Relationships**: Many-to-one with User and BlogPost

## Installation

1. **Clone the repository**
   ```bash
   cd my_blog_flask
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`

4. **Install dependencies**
   ```bash
   pip install flask flask-sqlalchemy flask-login flask-bootstrap flask-ckeditor flask-wtf wtforms flask-avatars python-dotenv werkzeug
   ```

5. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```
   FLASK_APP_SECRET_KEY=your-secret-key-here
   ```

6. **Initialize the database**
   
   The database will be created automatically on first run. The SQLite database file will be located at `instance/posts.db`.

## Usage

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Access the application**
   
   Open your browser and navigate to `http://localhost:5002`

3. **Create an admin account**
   
   The first user to register (user ID 1) will automatically have admin privileges.

4. **Create blog posts**
   
   Log in as the admin user and click "Create New Post" to add blog content.

5. **Comment on posts**
   
   Register/login as any user to leave comments on blog posts.

## Routes

| Route | Method | Description | Authentication |
|-------|--------|-------------|----------------|
| `/` | GET | View all blog posts | Public |
| `/register` | GET, POST | User registration | Public |
| `/login` | GET, POST | User login | Public |
| `/logout` | GET | User logout | Required |
| `/post/<post_id>` | GET, POST | View post and submit comments | Public (comments require login) |
| `/new-post` | GET, POST | Create new blog post | Admin only |
| `/edit-post/<post_id>` | GET, POST | Edit existing post | Admin only |
| `/delete/<post_id>` | GET | Delete a post | Admin only |
| `/about` | GET | About page | Public |
| `/contact` | GET | Contact page | Public |

## Forms

- **RegisterForm**: Full name, email, password (min 8 characters)
- **LoginForm**: Email and password validation
- **CreatePostForm**: Title, subtitle, image URL, rich text body
- **CommentForm**: Rich text comment field

## Project Structure

```
my_blog_flask/
├── main.py                 # Main application file
├── forms.py                # WTForms form definitions
├── .env                    # Environment variables (not in git)
├── .gitignore              # Git ignore file
├── instance/
│   └── posts.db           # SQLite database
├── static/
│   ├── assets/            # Static assets
│   ├── css/               # Stylesheets
│   └── js/                # JavaScript files
└── templates/
    ├── header.html        # Navigation header
    ├── footer.html        # Page footer
    ├── index.html         # Homepage
    ├── post.html          # Individual post page
    ├── make-post.html     # Create/edit post form
    ├── register.html      # Registration page
    ├── login.html         # Login page
    ├── about.html         # About page
    └── contact.html       # Contact page
```

## Key Features Implementation

### Admin-Only Decorator
```python
def admin_only(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.id != 1:
            abort(403)
        return func(*args, **kwargs)
    return decorated_function
```

### Password Security
- Uses PBKDF2-SHA256 hashing algorithm
- 8-character salt for additional security
- Passwords never stored in plain text

### Gravatar Integration
- Automatic avatar generation based on user email
- Default "identicon" style for unique avatars
- Configurable avatar size (default: 100px)

## Learning Objectives

This project demonstrates:
- User authentication and authorization in Flask
- Database relationships (one-to-many, many-to-one)
- Role-based access control with custom decorators
- Form validation and CSRF protection
- Password hashing and security best practices
- Session management with Flask-Login
- Rich text editing with CKEditor
- Template inheritance and Jinja2 templating
- Flash messages for user feedback
- SQLAlchemy ORM with typed mappings

## Future Enhancements

- Password reset functionality
- Email verification for new users
- Multiple admin roles and permissions
- Comment editing and deletion
- Post categories and tags
- Search functionality
- Pagination for posts and comments
- User profile pages
- Social media sharing
- Comment moderation system

## License

This project is part of the Angela Yu 100 Days of Python course.
