# Flight Deal Finder ✈️

A Python-based application that tracks flight prices and sends notifications when a low-price flight is found. This compilation is part of Day 39 of the 100 Days of Python course.

## 🚀 Features

*   **Flight Search**: Automatically searches for the cheapest flights from a specified origin (default: DEL) to various destinations within the next 6 months using the Amadeus API.
*   **Google Sheets Integration**: Reads destination data (City, IATA Code, Lowest Price threshold) from a Google Sheet and updates IATA codes if missing.
*   **Price Monitoring**: Compares current flight prices with the target price in your Google Sheet.
*   **Notifications**: Sends an SMS (and optionally WhatsApp) via Twilio when a flight is found that is cheaper than your target price.

## 🛠 Prerequisites

*   Python 3.x
*   A Google Sheet with columns: `City`, `IATA Code`, `Lowest Price` (via Sheety).
*   Amadeus API Account for flight data.
*   Twilio Account for sending SMS/WhatsApp notifications.

## ⚙️ Configuration

1.  **Clone the repository**.
2.  **Install dependencies**:
    ```bash
    pip install requests python-dotenv twilio
    ```
3.  **Set up Environment Variables**:
    Create a `.env` file in the root directory with the following keys:

    ```env
    # Sheety (Google Sheets)
    GOOGLE_SHEET_ID=your_sheet_id
    SHEETY_BEARER_TOKEN=your_sheety_token

    # Amadeus (Flight Search)
    AMADEUS_API_KEY=your_amadeus_api_key
    AMADEUS_API_SECRET=your_amadeus_api_secret

    # Twilio (Notifications)
    TWILIO_ACCOUNT_SID=your_twilio_sid
    TWILIO_AUTH_TOKEN=your_twilio_auth_token
    TWILIO_MESSAGING_SERVICE_SID=your_messaging_service_sid
    PHONE_NUMBER=your_destination_phone_number
    TWILIO_WHATSAPP_NUMBER=your_twilio_whatsapp_number   # Optional: For WhatsApp
    TWILIO_VERIFIED_NUMBER=your_verified_number           # Optional: For WhatsApp
    ```

## 🏃 Usage

Run the main script:

```bash
python main.py
```

The script will:
1.  Read your destination list from Google Sheets.
2.  Update any missing IATA codes in the sheet.
3.  Search for flights for each destination.
4.  Print results to the console.
5.  Send an SMS if a deal is found!

## 📂 Project Structure

*   `main.py`: The entry point. specific orchestrates data fetching, flight search, and notifications.
*   `data_manager.py`: Handles communication with the Google Sheet via Sheety.
*   `flight_search.py`: Interfaces with the Amadeus API to find airport codes and flight offers.
*   `flight_data.py`: Models flight data and finds the cheapest option.
*   `notification_manager.py`: Sends SMS/WhatsApp alerts using Twilio.
