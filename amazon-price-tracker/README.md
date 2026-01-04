# Amazon Price Tracker 📉

A Python script that tracks the price of a specific product on Amazon.in and sends an email alert 📧 if the price drops below a target threshold.
This project was build during Angela Yu's 100 Days of Python Challenge.

## Features
- **Scrapes Product Price:** Fetches the current price of a product from Amazon using `BeautifulSoup`.
- **Email Notification:** Sends an automatic email alert via SMTP if the price is lower than your set budget.
- **Environment Variables:** Securely manages email credentials using a `.env` file.

## Tech Stack
- **Python 3.x**
- **BeautifulSoup4** (Web Scraping)
- **Requests** (HTTP Requests)
- **smtplib** (Email Sending)
- **python-dotenv** (Environment Management)

## Setup & Usage

1.  **Clone the Repository:**
    ```bash
    git clone <repository-url>
    cd amazon-price-tracker
    ```

2.  **Install Dependencies:**
    ```bash
    pip install requests beautifulsoup4 python-dotenv
    ```

3.  **Environment Configuration:**
    Create a `.env` file in the project root and add your email credentials:
    ```ini
    MY_EMAIL=your_email@gmail.com
    MY_PASSWORD=your_app_password
    ```
    *Note: For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833) instead of your regular password.*

4.  **Run the Script:**
    ```bash
    python bot.py
    ```

## Customization
- **Product URL:** Update the `amazon_clone_url` variable in `bot.py` with the Amazon product you want to track.
- **Target Price:** Modify the price comparison logic (currently set to `< 80000`) in `bot.py` to match your budget.

## Disclaimer
This project is for educational purposes. Be mindful of Amazon's terms of service regarding web scraping.
