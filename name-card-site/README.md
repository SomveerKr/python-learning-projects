# Day 56 - Personal Name Card Site

A simple, elegant personal portfolio website built with Flask and HTML5 UP's Identity template. This project serves as a digital business card showcasing personal information and social media links.

## 🌟 Features

- **Clean, Responsive Design**: Built using the HTML5 UP Identity template for a modern, professional look
- **Flask Backend**: Simple Flask server to serve the static site
- **Social Media Integration**: Links to Twitter, Instagram, and GitHub profiles
- **Fully Responsive**: Works seamlessly across desktop, tablet, and mobile devices

## 🛠️ Technologies Used

- **Python 3.x**
- **Flask**: Web framework for serving the application
- **HTML5**: Structure and content
- **CSS3**: Styling and responsive design
- **JavaScript**: Interactive elements and animations

## 📋 Prerequisites

- Python 3.x installed on your system
- Flask library

## 🚀 Installation & Setup

1. **Clone or navigate to the project directory**:
   ```bash
   cd name-card-site
   ```

2. **Install required dependencies**:
   ```bash
   pip install flask
   ```

3. **Run the application**:
   ```bash
   python server.py
   ```

4. **Access the website**:
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## 📁 Project Structure

```
day-56-name-card-site/
│
├── server.py                 # Flask application server
├── templates/
│   └── index.html           # Main HTML template
├── static/
│   ├── assets/              # CSS, JS, and other assets
│   │   ├── css/            # Stylesheets
│   │   └── js/             # JavaScript files
│   └── images/             # Image assets (avatar, etc.)
└── README.md               # Project documentation
```

## 🎨 Customization

To personalize this site for yourself:

1. **Update Personal Information**:
   - Edit `templates/index.html`
   - Change the name, title, and description in the header section

2. **Replace Avatar Image**:
   - Add your photo to `static/images/avatar.jpg`

3. **Update Social Media Links**:
   - Modify the links in the footer section of `index.html` (lines 73-75)

4. **Customize Styling**:
   - Edit CSS files in `static/assets/css/` to change colors, fonts, and layout

## 📝 Notes

- The template includes a commented-out contact form section that can be activated if needed
- The design is based on HTML5 UP's Identity template (free for personal and commercial use under CCA 3.0 license)
- Debug mode is enabled in `server.py` for development purposes

## 📄 License

- **Template**: HTML5 UP Identity template - [CCA 3.0 License](http://html5up.net/license)
- **Code**: Personal learning project

## 🔗 Social Links

- **Twitter**: [@Code_Veer](https://x.com/Code_Veer)
- **Instagram**: [@code.veer](https://www.instagram.com/code.veer/)
- **GitHub**: [SomveerKr](https://github.com/SomveerKr)

## 🎓 Learning Objectives

This project was created as part of Day 56 of the Angela Yu 100 Days of Python course, focusing on:
- Understanding Flask web framework basics
- Serving HTML templates with Flask
- Working with static files in Flask applications
- Creating a simple personal portfolio website

---

**Created by**: Somveer Kumar  
**Design Credit**: [HTML5 UP](http://html5up.net)
