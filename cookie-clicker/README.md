# Cookie Clicker Bot 🍪

A Python automation script that plays the [Cookie Clicker](https://ozh.github.io/cookieclicker/) game using Selenium. This project was built as part of Day 48 of 100 Days of Code.

## 🚀 Features

*   **Auto-Clicking**: Continuously clicks the big cookie to generate cookies.
*   **Auto-Upgrade**: Checks the store every 5 seconds (approx) to purchase the most expensive affordable upgrade.
*   **Score Tracking**: Runs for 5 minutes and prints the final "Cookies Per Second" (CpS) score.

## 🛠️ specific Changes

*   Handles the language selection popup.
*   Uses `css_selector` to find available upgrades dynamically.

## 💻 Tech Stack

*   Python
*   Selenium Webdriver

## 📋 Prerequisites

*   Python 3.x installed
*   Chrome Browser installed

## 📦 Installation

1.  Clone the repository.
2.  Install the required packages:

    ```bash
    pip install selenium webdriver-manager
    ```

## 🎮 Usage

Run the script:

```bash
python cookie_clicker.py
```

The script will launch a Chrome browser, start the game, and run automatically for 5 minutes.
