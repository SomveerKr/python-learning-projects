# 🎂 Birthday Wisher - Automated Birthday Email Sender

A Python automation project that automatically sends personalized birthday wishes via email. Built as part of **Day 32** of Angela Yu's 100 Days of Python course.

## 📋 Project Overview

This project demonstrates email automation using Python's `smtplib` library. The program checks a CSV file of birthdays daily and automatically sends a personalized birthday email to anyone whose birthday matches the current date.

## ✨ Features

- **Automated Birthday Detection**: Checks current date against a CSV database of birthdays
- **Personalized Email Templates**: Randomly selects from 3 different letter templates
- **Dynamic Name Replacement**: Automatically replaces placeholder text with recipient's name
- **Secure Email Sending**: Uses Gmail SMTP with environment variables for credentials
- **CSV Data Management**: Easy-to-update birthday database

## 🛠️ Technologies Used

- **Python 3.x**
- **Libraries**:
  - `smtplib` - For sending emails via SMTP
  - `pandas` - For reading and managing CSV data
  - `datetime` - For date/time operations
  - `random` - For selecting random letter templates
  - `python-dotenv` - For managing environment variables

## 📁 Project Structure

```
day-32-Birthday+Wisher/
├── main.py                 # Main application script
├── birthdays.csv           # Database of birthdays
├── .env                    # Environment variables (email credentials)
├── letter_templates/       # Birthday letter templates
│   ├── letter_1.txt
│   ├── letter_2.txt
│   └── letter_3.txt
└── README.md              # Project documentation
```

## 🚀 How It Works

1. **Load Environment Variables**: Reads email credentials from `.env` file
2. **Check Current Date**: Gets today's date using `datetime`
3. **Read Birthday Data**: Loads birthdays from `birthdays.csv` using pandas
4. **Match Birthdays**: Compares current month/day with each entry
5. **Select Template**: Randomly chooses one of three letter templates
6. **Personalize Message**: Replaces `[NAME]` placeholder with recipient's name
7. **Send Email**: Sends the personalized birthday wish via Gmail SMTP

## 📝 Setup Instructions

### 1. Install Required Packages

```bash
pip install pandas python-dotenv
```

### 2. Configure Environment Variables

Create a `.env` file in the project directory:

```env
MY_EMAIL=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

> **Note**: For Gmail, you'll need to use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password.

### 3. Update Birthday Data

Edit `birthdays.csv` with your contacts:

```csv
name,email,year,month,day
John Doe,john@example.com,1990,12,25
Jane Smith,jane@example.com,1985,06,15
```

### 4. Customize Letter Templates

Modify the letter templates in `letter_templates/` folder. Use `[NAME]` as a placeholder for the recipient's name.

### 5. Run the Program

```bash
python main.py
```

## 🎯 Key Learning Outcomes

- Working with **SMTP protocol** for email automation
- Using **environment variables** for secure credential management
- **CSV file handling** with pandas
- **String manipulation** and template replacement
- **Date/time operations** in Python
- **Random selection** from multiple options

## 🔒 Security Considerations

- ✅ Email credentials stored in `.env` file (not committed to version control)
- ✅ Uses Gmail App Passwords for enhanced security
- ✅ `.env` file should be added to `.gitignore`

## 🎓 Course Context

This project is part of **Angela Yu's 100 Days of Python** course, specifically **Day 32**, which focuses on:
- Sending emails with Python
- Working with the `smtplib` module
- Managing dates and times
- Automating repetitive tasks

## 💡 Potential Enhancements

- [ ] Schedule the script to run daily using cron jobs or Task Scheduler
- [ ] Add support for multiple email providers (Outlook, Yahoo, etc.)
- [ ] Include HTML email templates for richer formatting
- [ ] Add logging to track sent emails
- [ ] Implement error handling for failed email deliveries
- [ ] Add timezone support for international contacts

## 📧 Email Template Example

```
Dear [NAME],

Happy birthday!

All the best for the year!

Your Name
```

## 🤝 Contributing

Feel free to fork this project and add your own improvements!

## 📄 License

This project is part of a learning exercise and is free to use for educational purposes.

---

**Built with ❤️ as part of the 100 Days of Python Challenge**
