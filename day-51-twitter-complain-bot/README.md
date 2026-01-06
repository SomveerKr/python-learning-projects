# Day 51: Internet Speed Twitter Complain Bot


> [!WARNING]
> **Project Status: Incomplete**
> The Selenium script is currently facing issues logging into x.com due to anti-bot measures or login page changes. Alternative methods to resolve this are being explored.

## Overview
This project is designed to automatically check your internet download and upload speeds using Speedtest.net. If the speeds are below the promised values, the bot logs into X (formerly Twitter) and tweets a complaint to the internet service provider.


## Features
-   **Speed Test:** Automated internet speed testing via [Speedtest.net](https://www.speedtest.net/).
-   **Twitter Bot:** (Intended) Automated tweeting mechanism using Selenium WebDriver.

## Prerequisites
-   Python 3.x
-   Selenium WebDriver
-   Google Chrome & Chromedriver
-   `python-dotenv` for environment variable management

## Setup
1.  Install dependencies:
    ```bash
    pip install selenium python-dotenv
    ```
2.  Set up environment variables in a `.env` file:
    ```
    PROMISED_DOWN=150
    PROMISED_UP=10
    X_EMAIL=your_email
    X_PASSWORD=your_password
    ```

## Usage
Run the script:
```bash
python main.py
```
