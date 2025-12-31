import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()  
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWSAPI_API_KEY = os.getenv("NEWSAPI_API_KEY")


alpha_api_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK}&apikey={ALPHA_VANTAGE_API_KEY}"
stock_api_response = requests.get(alpha_api_url)
stock_data = stock_api_response.json()
daily_stocks_data = stock_data["Time Series (Daily)"]


# Get a list of all dates from the API response
data_dates = list(daily_stocks_data.keys())

# The first two dates in the list are the most recent trading days
latest_date = data_dates[0]
previous_date = data_dates[1]

# Get the closing prices for these dates (convert to float for calculation)
latest_close_price = float(daily_stocks_data[latest_date]["4. close"])
previous_close_price = float(daily_stocks_data[previous_date]["4. close"])

# Calculate the percentage change
percent_change = ((latest_close_price - previous_close_price) / previous_close_price) * 100

# Print the result for context
print(f"The closing price on {previous_date} was: ${previous_close_price:.2f}")
print(f"The closing price on {latest_date} was: ${latest_close_price:.2f}")
print(f"The percentage change is: {percent_change:.2f}%")

up_down = None
if percent_change > 0:
    up_down ="↑"
else:
    "↓"

if abs(percent_change) >= 3.0:
    newsapi_url = ("https://newsapi.org/v2/everything?"
       f"q={COMPANY_NAME}&"
       f"from={previous_date}&"
       "sortBy=popularity&"
       f"apiKey={NEWSAPI_API_KEY}")

    newsapi_response = requests.get(newsapi_url)
    newsapi_data=newsapi_response.json()
    #decreaed to one due to limit on twilio
    top_three_articles = newsapi_data["articles"][:3]
    #first article
    updated_articles= [
       {
        "title":article["title"],
        "description":article["description"]
        } for article in top_three_articles  
    ]
    
    # print(updated_articles)
    #
    messages_articles = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in updated_articles]
    print(messages_articles)
    absolute_percent_change =round(abs(percent_change))
    for message_article in messages_articles:
        client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        message = client.messages.create(
        messaging_service_sid=os.getenv("TWILIO_MESSAGING_SERVICE_SID"),
        body=f"{STOCK} {up_down}{absolute_percent_change}\n{message_article}",
        from_="+18568305804",
        to="+918287468611"
        )
        print(message.status)
else:
    print("\nResult: The stock price did not change by 5%.")



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

