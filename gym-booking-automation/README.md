# Gym Booking Automation 🏋️‍♂️

An automated Python script using Selenium to book gym classes. It specifically targets classes on **Tuesdays and Thursdays at 6:00 PM**, handling both immediate bookings and waitlist joins.

## Features

- **Automated Login**: Logs into the gym portal automatically.
- **Smart Booking**: Scans for classes matching specific criteria (Tue/Thu @ 6PM).
- **Waitlist Handling**: Automatically joins the waitlist if a class is full.
- **Verification**: Verifies successful bookings by cross-referencing with the "My Bookings" page.
- **Robustness**: Includes retry logic for network requests and page loads.
- **Persistent Session**: Uses a local Chrome profile to maintain session data.

## Prerequisites

- Python 3.x
- Google Chrome Browser
- Chrome Driver (compatible with your Chrome version)

## Installation

1. Clone or download this repository.
2. Install the required Python packages:

   ```bash
   pip install selenium
   ```

## Usage

1. **Configure Credentials**: 
   Open `main.py` and update the `login` function arguments with your actual email and password if different from the defaults.
   
   ```python
   def login(email="your.email@example.com", password="your_password"):
   ```

2. **Run the Script**:
   
   ```bash
   python main.py
   ```

   The script will launch Chrome, log in, process available classes, and print a summary of actions taken.

## Note

The script stores a Chrome profile in the `chrome_profile` directory within the project folder to persist user sessions.
