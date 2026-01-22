# Upgraded Blog - Flask Application

A full-featured blog application built with Flask that allows users to create, read, update, and delete blog posts. The application uses SQLAlchemy for database management, CKEditor for rich text editing, and Bootstrap for responsive design.

## Features

- **Create Blog Posts**: Add new blog posts with title, subtitle, author, rich text content, and image URL
- **View All Posts**: Browse all blog posts on the homepage with post previews
- **Read Individual Posts**: Click on any post to view its full content
- **Edit Posts**: Modify existing blog posts with pre-populated form data
- **Delete Posts**: Remove blog posts from the database with a single click
- **Rich Text Editor**: CKEditor integration for formatting blog content
- **Responsive Design**: Bootstrap-powered UI that works on all devices
- **SQLite Database**: Persistent storage for all blog posts

## Technologies Used

- **Flask**: Web framework for Python
- **Flask-SQLAlchemy**: ORM for database operations
- **Flask-WTF**: Form handling and validation
- **Flask-Bootstrap5**: Bootstrap integration for Flask
- **Flask-CKEditor**: Rich text editor integration
- **SQLite**: Lightweight database for storing blog posts
- **WTForms**: Form validation and rendering

## Project Structure

```
upgraded-blog-with-db/
├── instance/
│   └── posts.db              # SQLite database file
├── static/
│   ├── assets/               # Images and media files
│   ├── css/                  # Stylesheets
│   └── js/                   # JavaScript files
├── templates/
│   ├── about.html            # About page
│   ├── contact.html          # Contact page
│   ├── footer.html           # Footer component
│   ├── header.html           # Header/navigation component
│   ├── index.html            # Homepage with all posts
│   ├── make-post.html        # Form for creating/editing posts
│   └── post.html             # Individual post view
├── main.py                   # Main application file
└── requirements.txt          # Python dependencies
```

## Installation

1. **Clone the repository** (or navigate to the project directory):
   ```bash
   cd upgraded-blog-with-db
   ```

2. **Create a virtual environment**:
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
   - Open your browser and navigate to `http://127.0.0.1:5003`

3. **Create your first blog post**:
   - Click the "Create New Post" button on the homepage
   - Fill in the form with title, subtitle, author name, content, and image URL
   - Click "Post" to publish

4. **Manage posts**:
   - **View**: Click on any post title to read the full content
   - **Edit**: Click the edit button on a post to modify it
   - **Delete**: Click the ✘ icon next to a post to remove it

## Database Schema

### BlogPost Model

| Field    | Type         | Description                          |
|----------|--------------|--------------------------------------|
| id       | Integer      | Primary key (auto-generated)         |
| title    | String(250)  | Blog post title (unique)             |
| subtitle | String(250)  | Blog post subtitle                   |
| date     | String(250)  | Publication date                     |
| body     | Text         | Blog post content (rich text)        |
| author   | String(250)  | Author name                          |
| img_url  | String(250)  | URL for the post's header image      |

## Routes

| Route                        | Method    | Description                    |
|------------------------------|-----------|--------------------------------|
| `/`                          | GET       | Display all blog posts         |
| `/post/<int:post_id>`        | GET       | Display individual post        |
| `/new-post`                  | GET, POST | Create a new blog post         |
| `/edit-post/<int:post_id>`   | GET, POST | Edit an existing post          |
| `/delete-post/<int:post_id>` | GET       | Delete a blog post             |
| `/about`                     | GET       | Display about page             |
| `/contact`                   | GET       | Display contact page           |

## Configuration

The application uses the following configuration:
- **Secret Key**: `8BYkEfBA6O6donzWlSihBXox7C0sKR6b` (change in production)
- **Database**: SQLite (`sqlite:///posts.db`)
- **Debug Mode**: Enabled (disable in production)
- **Port**: 5003

> **Note**: For production deployment, update the secret key and disable debug mode.

## Form Validation

The blog post form includes the following validators:
- **Title**: Required field
- **Subtitle**: Required field
- **Author**: Required field
- **Body**: Required field (CKEditor)
- **Image URL**: Required field with URL validation

## Development Notes

- The database is automatically created when the application starts
- Posts are ordered by date on the homepage
- CKEditor provides a WYSIWYG interface for content creation
- Bootstrap 5 ensures responsive design across devices

## Future Enhancements

Potential improvements for this project:
- User authentication and authorization
- Comment system for blog posts
- Categories and tags for posts
- Search functionality
- Pagination for the homepage
- Image upload instead of URL input
- Draft/publish status for posts
- User profiles and avatars

## License

This project is part of the Angela Yu 100 Days of Python course.

## Author

Created as part of Day 67 of the 100 Days of Python course.
