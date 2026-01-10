# Day 57: Jinja Templating Blog

A simple blog application built with Flask and Jinja2 templating engine. This project demonstrates dynamic content rendering by fetching blog posts from an external API and displaying them using Jinja templates.

## Features

- **Dynamic Blog Posts**: Fetches blog posts from an external API (npoint.io)
- **Jinja2 Templating**: Uses Jinja2 for dynamic HTML rendering
- **Individual Post Pages**: Each blog post has its own dedicated page
- **Responsive Design**: Clean and simple UI with custom CSS styling
- **URL Routing**: Dynamic URL routing for individual blog posts

## Project Structure

```
day-57-jinja-templating-blog/
├── main.py                 # Main Flask application
├── post.py                 # Post class definition
├── templates/
│   ├── index.html         # Homepage template (lists all posts)
│   └── post.html          # Individual post template
└── static/
    └── css/
        └── styles.css     # Custom CSS styles
```

## Technologies Used

- **Flask**: Web framework for Python
- **Jinja2**: Template engine (comes with Flask)
- **Requests**: HTTP library for fetching blog posts from API
- **HTML/CSS**: Frontend structure and styling

## Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd jinja-templating-blog
   ```

2. **Install required dependencies**:
   ```bash
   pip install flask requests
   ```

## Usage

1. **Run the Flask application**:
   ```bash
   python main.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. **Browse the blog**:
   - The homepage displays all blog posts with titles and subtitles
   - Click "Read" on any post to view the full content
   - Individual posts are accessible at `/blog/<post_id>`

## How It Works

### Main Application (`main.py`)

- Fetches blog posts from the npoint.io API on startup
- Defines two routes:
  - `/` - Homepage that displays all blog posts
  - `/blog/<int:post_id>` - Individual post page

### Templates

- **`index.html`**: Uses Jinja2 `{% for %}` loop to iterate through all posts and display them as cards
- **`post.html`**: Displays individual post details (title, subtitle, and body)

### Jinja2 Features Demonstrated

- **Variable rendering**: `{{ post["title"] }}`
- **For loops**: `{% for post in posts: %}`
- **URL generation**: `{{ url_for('get_blog', post_id = post['id']) }}`

## API Data Source

The blog posts are fetched from:
```
https://api.npoint.io/c790b4d5cab58020d391
```

Each post contains:
- `id`: Unique identifier
- `title`: Post title
- `subtitle`: Post subtitle/summary
- `body`: Full post content

## Learning Objectives

This project demonstrates:
- Setting up a Flask web application
- Using Jinja2 templating for dynamic content
- Fetching data from external APIs
- Implementing URL routing with parameters
- Organizing Flask projects with templates and static files
- Passing data from Flask routes to templates

## Future Enhancements

- Add a database to store blog posts locally
- Implement post creation/editing functionality
- Add user authentication
- Include comments section
- Add pagination for blog posts
- Implement search functionality

## Notes

- This is part of the "100 Days of Code - Python" course by Angela Yu
- The project runs in debug mode for development purposes
- Blog data is fetched on application startup and stored in memory

## License

This project is for educational purposes as part of the Angela Yu Python course.
