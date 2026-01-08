# Day 53 - Rent Researcher

A Python automation tool that scrapes rental property listings from Zillow and automatically submits them to a Google Form for easy data collection and analysis.

## 📋 Description

This project automates the process of researching rental properties by:
1. Scraping property listings from a Zillow clone website
2. Extracting key information (address, price, listing link)
3. Automatically filling and submitting a Google Form with the collected data

This is particularly useful for tracking rental prices, comparing properties, and building a database of available rentals without manual data entry.

## ✨ Features

- **Web Scraping**: Extracts rental listings from Zillow using BeautifulSoup
- **Data Extraction**: Parses addresses, prices, and property links
- **Form Automation**: Uses Selenium to automatically fill and submit Google Forms
- **Batch Processing**: Handles multiple listings in a single run
- **Environment Variables**: Secure configuration using `.env` file

## 🛠️ Technologies Used

- **Python 3.x**
- **BeautifulSoup4**: HTML parsing and web scraping
- **Selenium**: Browser automation for form submission
- **Requests**: HTTP requests for fetching web pages
- **python-dotenv**: Environment variable management
- **Chrome WebDriver**: Browser automation driver

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd rent-researcher
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

4. **Install dependencies**:
   ```bash
   pip install requests beautifulsoup4 selenium python-dotenv
   ```

5. **Download Chrome WebDriver**:
   - Download the appropriate ChromeDriver for your Chrome version from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
   - Add it to your system PATH or place it in the project directory

## ⚙️ Configuration

1. **Create a `.env` file** in the project root:
   ```env
   GOOGLE_FORM_LINK=your_google_form_url_here
   ```

2. **Set up your Google Form**:
   - Create a Google Form with three text input fields:
     1. Address
     2. Price
     3. Link
   - Copy the form URL and add it to your `.env` file

## 🚀 Usage

1. **Ensure your virtual environment is activated**

2. **Run the script**:
   ```bash
   python main.py
   ```

3. **The script will**:
   - Scrape listings from the Zillow clone website
   - Open Chrome browser (in detached mode)
   - Navigate to your Google Form
   - Fill in each listing's details
   - Submit the form for each property
   - Print the total number of submissions

## 📝 How It Works

1. **Scraping Phase**:
   - Sends an HTTP request to the Zillow clone website
   - Parses the HTML using BeautifulSoup
   - Extracts property cards and their details
   - Uses regex to clean price data

2. **Automation Phase**:
   - Launches Chrome browser with Selenium
   - Navigates to the Google Form
   - For each listing:
     - Fills in the address, price, and link fields
     - Clicks the submit button
     - Clicks "Submit another response" (except for the last entry)

## 🔒 Security Notes

- The `.env` file is gitignored to protect sensitive information
- Never commit your Google Form link or any credentials to version control
- The `.env` file should contain only non-sensitive configuration or be kept private

## 📊 Output

The script will print:
```
Submitted X listings!
```
Where X is the number of properties successfully submitted to your Google Form.

## 🐛 Troubleshooting

- **ChromeDriver issues**: Ensure your ChromeDriver version matches your Chrome browser version
- **Element not found**: The website structure may have changed; update the CSS selectors in the code
- **Form submission fails**: Verify your Google Form URL and ensure the form has exactly three text input fields
- **Timeout errors**: Increase the WebDriverWait timeout value if you have a slow internet connection

## 📚 Learning Objectives

This project demonstrates:
- Web scraping with BeautifulSoup
- Browser automation with Selenium
- Working with environment variables
- Regular expressions for data cleaning
- Combining multiple automation techniques

## 🔮 Future Enhancements

- Add support for multiple rental websites
- Implement data validation and error handling
- Export data to CSV or Excel
- Add price filtering and sorting
- Create a GUI for easier configuration
- Schedule automatic daily scraping

## 📄 License

This project is for educational purposes as part of the 100 Days of Code Python course.

## 🙏 Acknowledgments

- Built as part of Day 53 of Angela Yu's 100 Days of Code: The Complete Python Pro Bootcamp
- Uses the App Brewery Zillow Clone for demonstration purposes
