# ☕ Coffee & WiFi - Flask Application

A Flask web application that helps users discover and share information about cafes with WiFi and power outlets. Users can browse existing cafes and add new ones with ratings for coffee quality, WiFi strength, and power socket availability.

## 📋 Features

- **Browse Cafes**: View a comprehensive list of cafes with their amenities and ratings
- **Add New Cafes**: Submit new cafe entries through an interactive form
- **Rating System**: Rate cafes based on:
  - ☕ Coffee Quality (1-5 cups)
  - 💪 WiFi Strength (1-5 levels)
  - 🔌 Power Socket Availability (1-5 levels)
- **Location Links**: Direct Google Maps links to each cafe location
- **Responsive Design**: Bootstrap 5 integration for mobile-friendly interface
- **CSV Data Storage**: Simple and portable data storage using CSV files

## 🛠️ Technologies Used

- **Flask**: Web framework for Python
- **Flask-Bootstrap5**: Bootstrap 5 integration for Flask
- **Flask-WTF**: Form handling and validation
- **WTForms**: Form field definitions and validators
- **CSV**: Data persistence

## 📁 Project Structure

```
coffee-and-wifi/
├── main.py                 # Main Flask application
├── cafe-data.csv          # CSV database for cafe information
├── requirements.txt       # Python dependencies
├── static/
│   └── css/              # Custom stylesheets
└── templates/
    ├── base.html         # Base template with navigation
    ├── index.html        # Home page
    ├── add.html          # Add cafe form page
    └── cafes.html        # List all cafes page
```

## 🚀 Installation

1. **Clone or download this project**

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
   pip install flask flask-bootstrap flask-wtf
   ```

   Or update `requirements.txt` and install:
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

1. **Run the application**:
   ```bash
   python main.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

3. **Navigate through the app**:
   - **Home Page** (`/`): Welcome page with navigation
   - **View Cafes** (`/cafes`): Browse all registered cafes
   - **Add Cafe** (`/add`): Submit a new cafe with ratings

## 📝 How to Add a Cafe

1. Click on "Add a Cafe" or navigate to `/add`
2. Fill in the form with:
   - Cafe name
   - Google Maps location URL
   - Opening time (e.g., 9AM)
   - Closing time (e.g., 10:30PM)
   - Coffee rating (☕ to ☕☕☕☕☕)
   - WiFi rating (✘ or 💪 to 💪💪💪💪💪)
   - Power socket rating (🔌 to 🔌🔌🔌🔌🔌)
3. Click "Submit"
4. Your cafe will be added to the CSV database

## 🗃️ Data Storage

Cafe data is stored in `cafe-data.csv` with the following structure:

| Cafe Name | Location | Open | Close | Coffee | Wifi | Power |
|-----------|----------|------|-------|--------|------|-------|
| Example Cafe | Google Maps URL | 9AM | 5PM | ☕☕☕ | 💪💪 | 🔌🔌🔌 |

## 🎨 Customization

- **Secret Key**: Change the `SECRET_KEY` in `main.py` for production use
- **Styling**: Modify CSS files in the `static/css/` directory
- **Templates**: Customize HTML templates in the `templates/` directory
- **Form Fields**: Adjust form validators and choices in the `CafeForm` class

## 🔒 Security Notes

⚠️ **Important**: Before deploying to production:
- Change the `SECRET_KEY` to a secure, random value
- Use environment variables for sensitive configuration
- Implement proper error handling and input sanitization
- Consider using a database instead of CSV for better data integrity

## 📚 Learning Objectives

This project demonstrates:
- Flask web application development
- Form handling with Flask-WTF and WTForms
- Form validation (DataRequired, URL validators)
- CSV file operations (reading and writing)
- Bootstrap 5 integration with Flask
- Template inheritance with Jinja2
- Routing and view functions in Flask

## 🐛 Known Issues

- The `requirements.txt` file is currently empty and should be populated with:
  ```
  Flask
  Flask-Bootstrap
  Flask-WTF
  WTForms
  ```
- Unused import `dtfont` from `turtledemo.clock` in line 1 of `main.py`

## 🤝 Contributing

This is a learning project from the "100 Days of Code - Python" course. Feel free to fork and modify for your own learning purposes!

## 📄 License

This project is part of a learning exercise and is available for educational purposes.

## 🙏 Acknowledgments

- Part of Angela Yu's "100 Days of Code: The Complete Python Pro Bootcamp"
- Day 62: Coffee & WiFi Project
