# Habit Tracker 📊

A Python-based habit tracking application that uses the Pixela API to create visual graphs of your daily habits. Track your progress and build streaks by logging your activities each day.

## 📝 Description

This project is part of **Day 37** of Angela Yu's 100 Days of Python course. It demonstrates API integration with the Pixela service to create, update, and manage habit tracking graphs. The application allows you to visualize your habit consistency through beautiful pixel-based graphs.

## ✨ Features

- **User Management**: Create and manage Pixela user accounts
- **Graph Creation**: Set up custom graphs for different habits
- **Daily Logging**: Post daily habit data to your graphs
- **Data Updates**: Modify existing entries for specific dates
- **Graph Deletion**: Remove graphs when no longer needed
- **Visual Tracking**: View your habit streaks on Pixela's web interface

## 🛠️ Technologies Used

- **Python 3.x**
- **requests**: HTTP library for API calls
- **python-dotenv**: Environment variable management
- **datetime**: Date formatting and manipulation
- **Pixela API**: Habit tracking service

## 📋 Prerequisites

Before running this project, ensure you have:

- Python 3.x installed
- A Pixela account (created through the application)
- Required Python packages installed

## 🚀 Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd day-37-habit-tracker
   ```

2. **Install required dependencies**:
   ```bash
   pip install requests python-dotenv
   ```

3. **Set up environment variables**:
   Create a `.env` file in the project root with the following:
   ```
   pixela_api_token=your_secret_token_here
   ```

## 💻 Usage

The application provides several functions to interact with the Pixela API:

### Create a User
```python
create_user()
```
Creates a new Pixela user account with your credentials.

### Create a Graph
```python
create_graph()
```
Sets up a new habit tracking graph (e.g., coding hours).

### Post Daily Data
```python
post_to_graph()
```
Logs your daily habit data to the graph.

### Update Existing Data
```python
update_graph()
```
Modifies a specific date's entry.

### Delete a Graph
```python
delete_graph()
```
Removes a graph from your account.

## 🔧 Configuration

The application uses the following configuration:

- **Username**: `somveer` (can be customized)
- **Graph ID**: `graph1`
- **Graph Name**: `coding`
- **Unit**: `hour`
- **Type**: `float`
- **Color**: `shibafu` (green)

You can modify these values in `main.py` to track different habits.

## 📊 API Endpoints Used

- `POST /v1/users` - Create user
- `POST /v1/users/{username}/graphs` - Create graph
- `POST /v1/users/{username}/graphs/{graphID}` - Post pixel
- `PUT /v1/users/{username}/graphs/{graphID}/{date}` - Update pixel
- `DELETE /v1/users/{username}/graphs/{graphID}` - Delete graph

## 🔐 Security Notes

- Never commit your `.env` file to version control
- Keep your Pixela API token secret
- The `.gitignore` file is configured to exclude sensitive files

## 📚 Learning Outcomes

This project teaches:

- Working with RESTful APIs
- HTTP methods (GET, POST, PUT, DELETE)
- Authentication using custom headers
- Environment variable management
- Date formatting and manipulation
- API response handling

## 🌐 View Your Progress

After creating your graph, visit:
```
https://pixe.la/v1/users/{username}/graphs/{graphID}.html
```

Replace `{username}` and `{graphID}` with your values to see your habit tracking graph.

## 📖 Resources

- [Pixela API Documentation](https://docs.pixe.la/)
- [Angela Yu's 100 Days of Python](https://www.udemy.com/course/100-days-of-code/)

## 📄 License

This project is part of a learning course and is intended for educational purposes.

---

**Day 37** of 100 Days of Python 🐍
