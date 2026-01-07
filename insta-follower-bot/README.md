# Day 52: Instagram Follower Bot 🤖

An automated Instagram bot built with Selenium that logs into your Instagram account and follows users who follow a similar account of your choice. This project demonstrates web automation, browser interaction, and handling dynamic web elements.

## 📋 Features

- **Automated Login**: Securely logs into Instagram using credentials from environment variables
- **Follower Discovery**: Navigates to a target account and accesses their followers list
- **Smart Scrolling**: Automatically scrolls through the followers popup to load more users
- **Automated Following**: Follows users from the loaded followers list
- **Error Handling**: Handles click interceptions and stale element references gracefully
- **Environment Variables**: Keeps credentials secure using `.env` file

## 🛠️ Technologies Used

- **Python 3.x**
- **Selenium WebDriver**: For browser automation
- **Chrome WebDriver**: Chrome browser automation
- **python-dotenv**: For environment variable management

## 📦 Installation

1. **Clone the repository** (if not already done):
   ```bash
   cd insta-follower-bot
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install required packages**:
   ```bash
   pip install selenium python-dotenv
   ```

5. **Download ChromeDriver**:
   - Ensure you have Chrome browser installed
   - ChromeDriver should match your Chrome version
   - Selenium Manager will handle this automatically in newer versions

## ⚙️ Configuration

1. **Create a `.env` file** in the project root:
   ```env
   IG_USERNAME=your_instagram_username
   PASSWORD=your_instagram_password
   ```

2. **Update the target account** in `main.py`:
   ```python
   SIMILIAR_ACCOUNT = "piximperfect"  # Change to your target account
   ```

## 🚀 Usage

1. **Run the bot**:
   ```bash
   python main.py
   ```

2. **What happens**:
   - Chrome browser opens and navigates to Instagram login page
   - Bot logs in with your credentials
   - Waits 10 seconds (for manual 2FA if needed)
   - Navigates to the target account's followers page
   - Scrolls through the followers popup 7 times
   - Follows all loaded users (with 1.1 second delay between follows)

## 📝 Code Structure

```
InstaFollower Class:
├── login()           # Logs into Instagram
├── find_followers()  # Navigates to target account and scrolls followers list
└── follow()          # Follows all loaded users
```

## ⚠️ Important Notes

### Instagram Limits
- Instagram has rate limits on following users
- Following too many users too quickly may result in temporary action blocks
- The bot includes delays to mimic human behavior, but use responsibly

### Security
- Never commit your `.env` file to version control
- The `.gitignore` file is configured to exclude `.env`
- Use a test account if experimenting with the bot

### Manual Intervention
- The 10-second delay after login allows time for manual 2FA verification if enabled
- You may need to manually solve CAPTCHAs if Instagram detects automation

### CSS Selectors
- Instagram frequently updates their UI
- CSS selectors (like `.xz65tgg.x1rife3k`) may need updating if the bot stops working
- Check the browser's developer tools to find updated selectors

## 🐛 Troubleshooting

**Bot doesn't log in:**
- Verify credentials in `.env` file
- Check if 2FA is enabled (complete it during the 10-second wait)
- Ensure ChromeDriver version matches your Chrome browser

**Followers popup doesn't scroll:**
- Instagram may have changed the CSS classes
- Inspect the followers popup and update the selector in `find_followers()`

**Follow buttons not clicking:**
- Instagram may have changed button structure
- Update the XPath in the `follow()` method

**ElementClickInterceptedException:**
- This is normal when trying to follow someone you already follow
- The bot handles this by clicking the "Cancel" button

## 🎯 Learning Objectives

This project demonstrates:
- Web scraping with Selenium
- Handling dynamic web content
- Working with popups and scrollable elements
- Managing authentication and sessions
- Error handling in web automation
- Environment variable management for security

## 📜 License

This project is for educational purposes only. Use responsibly and in accordance with Instagram's Terms of Service.

## ⚠️ Disclaimer

This bot is created for learning purposes as part of the 100 Days of Code Python course. Automated actions on Instagram may violate their Terms of Service. Use at your own risk. The author is not responsible for any account restrictions or bans resulting from using this bot.

## 🔗 Related Projects

Part of the [100 Days of Python](https://www.udemy.com/course/100-days-of-code/) course by Angela Yu.
