import os
import re
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()

# Setup Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Scrape Zillow listings
URL = "https://appbrewery.github.io/Zillow-Clone/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
listings = soup.select("li.ListItem-c11n-8-84-3-StyledListCardWrapper")

# Extract data
addresses = []
prices = []
links = []

for card in listings:
    address = card.find("address").text.strip()
    addresses.append(address)

    price_text = card.find("span", class_="PropertyCardWrapper__StyledPriceLine").text
    price = re.search(r'\$[\d,]+', price_text).group()
    prices.append(price)

    link = card.find("a", class_="StyledPropertyCardDataArea-anchor")["href"]
    links.append(link)

# Submit to Google Form
wait = WebDriverWait(driver, 10)
driver.get(os.getenv("GOOGLE_FORM_LINK"))

for i in range(len(addresses)):
    # Fill form
    inputs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'input[type="text"]')))
    inputs[0].send_keys(addresses[i])
    inputs[1].send_keys(prices[i])
    inputs[2].send_keys(links[i])

    # Submit
    submit_btn = driver.find_element(By.CSS_SELECTOR, 'div[aria-label="Submit"]')
    submit_btn.click()

    # Next form (if not last)
    if i < len(addresses) - 1:
        next_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Submit another response")))
        next_link.click()

print(f"Submitted {len(addresses)} listings!")