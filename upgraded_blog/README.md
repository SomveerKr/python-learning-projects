# Upgraded Blog - Codeveer Log

A modern, responsive blog application built with Flask that dynamically fetches and displays blog posts from an external API. This project demonstrates Flask templating with Jinja2, RESTful routing, and clean web design.

## 🌟 Features

- **Dynamic Content Loading**: Blog posts are fetched from an external API (npoint.io)
- **Responsive Design**: Clean, modern UI that works across all devices
- **Multiple Pages**: Home, About, Contact, and individual blog post pages
- **Template Inheritance**: Efficient use of Jinja2 templating with reusable header and footer components
- **RESTful Routing**: Clean URL structure for accessing individual blog posts
- **Professional Layout**: Bootstrap-based design with custom styling

## 📋 Prerequisites

- Python 3.x
- pip (Python package installer)

## 🚀 Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd upgraded_blog
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

4. **Install required dependencies**:
   ```bash
   pip install flask requests
   ```

## 💻 Usage

1. **Run the application**:
   ```bash
   python server.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. **Explore the blog**:
   - Browse blog posts on the home page
   - Click on any post to read the full content
   - Visit the About page to learn more
   - Check out the Contact page

## 📁 Project Structure

```
upgraded_blog/
├── server.py              # Main Flask application
├── templates/             # HTML templates
│   ├── header.html       # Reusable header component
│   ├── footer.html       # Reusable footer component
│   ├── index.html        # Home page with blog post listings
│   ├── post.html         # Individual blog post page
│   ├── about.html        # About page
│   └── contact.html      # Contact page
├── static/               # Static assets
│   ├── assets/          # Images and media files
│   ├── css/             # Stylesheets
│   └── js/              # JavaScript files
└── README.md            # Project documentation
```

## 🔧 How It Works

1. **Data Fetching**: The application fetches blog post data from `https://api.npoint.io/57303010b8ea0f9272e8` on startup
2. **Home Page**: Displays all blog posts with titles, subtitles, author, and date
3. **Individual Posts**: Each post is accessible via `/blog/<id>` route
4. **Template Rendering**: Jinja2 templates dynamically render content with data passed from Flask routes
5. **Static Pages**: About and Contact pages provide additional information

## 🛠️ Technologies Used

- **Flask**: Python web framework for backend
- **Jinja2**: Template engine for dynamic HTML rendering
- **Requests**: HTTP library for fetching blog data from API
- **Bootstrap**: Frontend framework for responsive design
- **HTML/CSS/JavaScript**: Frontend technologies

## 📝 Routes

| Route | Description |
|-------|-------------|
| `/` | Home page displaying all blog posts |
| `/blog/<int:id>` | Individual blog post page |
| `/about` | About page |
| `/contact` | Contact page |

## 🎨 Customization

- **Blog Data**: Modify the API endpoint in `server.py` (line 6) to use your own blog data source
- **Author Name**: Change the `author` variable in `server.py` (line 10)
- **Styling**: Update CSS files in the `static/css/` directory
- **Templates**: Modify HTML templates in the `templates/` directory

## 📚 Learning Outcomes

This project demonstrates:
- Flask application structure and routing
- Jinja2 template inheritance and rendering
- Working with external APIs using the `requests` library
- Dynamic content rendering
- RESTful URL design
- Separation of concerns (templates, static files, application logic)

## 🤝 Contributing

This is a learning project from the Angela Yu 100 Days of Python course. Feel free to fork and modify for your own learning purposes.

## 📄 License

This project is created for educational purposes as part of the 100 Days of Python course.

## 👨‍💻 Author

**Somveer Kumar**

---

*Part of the Angela Yu 100 Days of Python Course - Day 59*
