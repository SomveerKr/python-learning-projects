# 📈 Stock News Alert System

A Python application that monitors stock price changes and sends SMS alerts with relevant news articles when significant price movements occur. Built as part of **Day 36** of Angela Yu's 100 Days of Python course.

## 🎯 Project Overview

This automated stock monitoring system tracks Tesla (TSLA) stock prices and sends SMS notifications via Twilio when the stock price changes by 3% or more between consecutive trading days. Each alert includes the percentage change and top news articles about the company.

## ✨ Features

- **Real-time Stock Monitoring**: Fetches daily stock data using Alpha Vantage API
- **Percentage Change Calculation**: Compares closing prices between the two most recent trading days
- **News Integration**: Retrieves top 3 relevant news articles using NewsAPI when significant price changes occur
- **SMS Notifications**: Sends formatted SMS alerts via Twilio with:
  - Stock symbol and percentage change (with ↑ or ↓ indicator)
  - Article headlines and descriptions
- **Environment Variable Security**: Uses `.env` file to protect sensitive API keys and credentials

## 🛠️ Technologies Used

- **Python 3.x**
- **APIs**:
  - [Alpha Vantage API](https://www.alphavantage.co/) - Stock market data
  - [NewsAPI](https://newsapi.org/) - News articles
  - [Twilio API](https://www.twilio.com/) - SMS messaging
- **Libraries**:
  - `requests` - HTTP requests
  - `twilio` - Twilio SMS integration
  - `python-dotenv` - Environment variable management

## 📋 Prerequisites

Before running this project, you need to obtain API keys from:

1. **Alpha Vantage**: [Get free API key](https://www.alphavantage.co/support/#api-key)
2. **NewsAPI**: [Get free API key](https://newsapi.org/register)
3. **Twilio**: [Sign up for account](https://www.twilio.com/try-twilio)
   - Account SID
   - Auth Token
   - Messaging Service SID
   - Twilio phone number

## 🚀 Setup Instructions

1. **Clone or navigate to the project directory**:
   ```bash
   cd day-36-stock-news-extrahard
   ```

2. **Install required dependencies**:
   ```bash
   pip install requests twilio python-dotenv
   ```

3. **Create a `.env` file** in the project root with the following variables:
   ```env
   ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key
   NEWSAPI_API_KEY=your_newsapi_api_key
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   TWILIO_MESSAGING_SERVICE_SID=your_twilio_messaging_service_sid
   ```

4. **Update phone numbers** in `main.py`:
   - Line 73: Replace `to` parameter with your phone number
   - Line 72: Update `from_` parameter with your Twilio phone number (if needed)

5. **Customize stock symbol** (optional):
   - Line 6: Change `STOCK = "TSLA"` to any stock symbol
   - Line 7: Update `COMPANY_NAME` accordingly

## 💻 Usage

Run the script:
```bash
python main.py
```

### Expected Output

The script will:
1. Fetch the latest stock data
2. Calculate the percentage change between the two most recent trading days
3. Display the closing prices and percentage change in the console
4. If the change is ≥3%, fetch news articles and send SMS alerts
5. If the change is <3%, display a message indicating no alert was sent

### Example Console Output

```
The closing price on 2024-01-15 was: $238.45
The closing price on 2024-01-16 was: $245.12
The percentage change is: 2.80%

Result: The stock price did not change by 5%.
```

### Example SMS Format

```
TSLA ↑5
Headline: Tesla Announces Record Quarterly Deliveries
Brief: Tesla Inc. reported record vehicle deliveries for Q4, exceeding analyst expectations...
```

## 📁 Project Structure

```
day-36-stock-news-extrahard/
│
├── main.py           # Main application script
├── .env              # Environment variables (not tracked by git)
├── .gitignore        # Git ignore file
└── README.md         # Project documentation
```

## 🔧 How It Works

1. **Fetch Stock Data**: Retrieves daily time series data from Alpha Vantage API
2. **Calculate Change**: Compares the closing prices of the two most recent trading days
3. **Check Threshold**: If absolute percentage change ≥ 3%:
   - Fetches top 3 news articles from NewsAPI
   - Formats articles with headline and description
   - Sends SMS via Twilio for each article
4. **Display Results**: Prints stock information and alert status to console

## 🎓 Learning Outcomes

This project demonstrates:
- Working with multiple REST APIs
- Environment variable management for security
- Data parsing and manipulation (JSON responses)
- Conditional logic and threshold-based automation
- SMS integration with Twilio
- List comprehensions and data formatting
- Error handling for API requests

## 🔒 Security Notes

- Never commit your `.env` file to version control
- The `.gitignore` file is configured to exclude `.env`
- Keep your API keys and Twilio credentials private
- Twilio free tier has limitations on the number of SMS messages

## 📝 Customization Ideas

- Monitor multiple stocks simultaneously
- Adjust the percentage threshold (currently 3%)
- Send emails instead of/in addition to SMS
- Add historical price tracking
- Implement a scheduling system to run automatically
- Create a web dashboard to display alerts
- Add more detailed stock analysis metrics

## 🐛 Troubleshooting

- **API Rate Limits**: Free tier APIs have request limits. Alpha Vantage allows 5 requests/minute
- **Twilio SMS Limit**: Free accounts can only send to verified numbers
- **Missing Data**: Ensure stock markets are open; no data on weekends/holidays
- **Import Errors**: Make sure all dependencies are installed via pip

## 📚 Resources

- [Alpha Vantage Documentation](https://www.alphavantage.co/documentation/)
- [NewsAPI Documentation](https://newsapi.org/docs)
- [Twilio Python SDK](https://www.twilio.com/docs/libraries/python)
- [Angela Yu's 100 Days of Code](https://www.udemy.com/course/100-days-of-code/)

## 📄 License

This project is part of a learning exercise from Angela Yu's 100 Days of Python course.

---

**Day 36 Challenge** - Stock Trading News Alert Project 🚀
