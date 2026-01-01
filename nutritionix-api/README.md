# Day 38: Nutrition/Exercise Tracker 💪

## 📋 Project Overview
This project is part of **Day 38** of Angela Yu's **100 Days of Python** course. It's a workout tracking application that uses **natural language processing** to log exercises and their nutritional data to a Google Sheet. Users can input their physical activities in plain English, and the app automatically calculates calories burned and duration, then stores the data in a spreadsheet.

## 🌟 Features
- **Natural Language Processing**: Input exercises in plain English (e.g., "ran 3 miles" or "did 30 minutes of yoga")
- **Nutritionix API Integration**: Converts natural language to structured exercise data with calorie information
- **Automated Logging**: Automatically logs workouts to Google Sheets with date and time stamps
- **Sheety API Integration**: Uses Sheety to interact with Google Sheets as a database
- **Bearer Token Authentication**: Secure API authentication using bearer tokens
- **Environment Variables**: Secure credential management using `.env` file

## 🛠️ Technologies Used
- **Python 3.x**
- **Nutritionix API**: Natural language exercise tracking
- **Sheety API**: Google Sheets database interface
- **python-dotenv**: Environment variable management
- **requests**: HTTP library for API calls

## 📁 Project Structure
```
day-38-nutritionix-api/
│
├── main.py           # Main application file
├── .env              # Environment variables (not tracked in git)
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## 🔧 Setup Instructions

### Prerequisites
- Python 3.x installed
- Nutritionix API account ([Sign up here](https://www.nutritionix.com/business/api))
- Google Sheet set up with Sheety ([Sign up here](https://sheety.co/))

### Installation Steps

1. **Clone or navigate to this directory**:
   ```bash
   cd day-38-nutritionix-api
   ```

2. **Install required packages**:
   ```bash
   pip install requests python-dotenv
   ```

3. **Set up your `.env` file** with the following variables:
   ```env
   NUTRITIONIX_APP_ID=your_nutritionix_app_id
   NUTRITIONIX_API_KEY=your_nutritionix_api_key
   GOOGLE_SHEET_ENDPOINT=your_sheety_project_endpoint
   SHEETY_BEARER_TOKEN=your_sheety_bearer_token
   ```

4. **Set up your Google Sheet** with the following columns:
   - Date
   - Time
   - Exercise
   - Duration
   - Calories

## 🚀 Usage

Run the application:
```bash
python main.py
```

When prompted, enter your physical activity in natural language:
```
Enter your physical activity: ran 5 km and cycled for 20 minutes
```

The app will:
1. Process your input using Nutritionix API
2. Extract exercise details (name, duration, calories)
3. Log each exercise to your Google Sheet with current date and time

## 📊 Example Output

**Input**:
```
Enter your physical activity: walked 3 miles
```

**Google Sheet Entry**:
| Date       | Time     | Exercise | Duration | Calories |
|------------|----------|----------|----------|----------|
| 01/01/2026 | 22:52:44 | Walking  | 45       | 150      |

## 🔐 Security Notes
- Never commit your `.env` file to version control
- Keep your API keys and tokens private
- The `.gitignore` file is configured to exclude `.env`

## 🎓 Learning Outcomes
Through this project, I learned:
- How to work with **RESTful APIs** and HTTP requests
- **API authentication** using app IDs, API keys, and bearer tokens
- Processing **natural language inputs** with specialized APIs
- Managing **environment variables** securely
- Working with **Google Sheets as a database** through APIs
- Handling **JSON data** from API responses
- Using **list comprehensions** for data transformation

## 📝 Notes
- The Nutritionix API can recognize many different exercises and activities
- The app automatically calculates calories based on average values for your input
- You can track multiple exercises in a single input
- Bearer token authentication provides better security than basic auth

## 🔗 API Documentation
- [Nutritionix API Documentation](https://docs.nutritionix.com/)
- [Sheety API Documentation](https://sheety.co/docs)

## 📚 Part of 100 Days of Python
This project is part of my journey through Angela Yu's 100 Days of Python course, focusing on API authentication, natural language processing, and practical data logging applications.

---

**Day 38 Complete!** 🎉
