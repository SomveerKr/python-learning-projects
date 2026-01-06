
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
import os
from dotenv import load_dotenv

import time

load_dotenv()

PROMISED_DOWN = 200
PROMISED_UP = 200
X_EMAIL = os.getenv("X_EMAIL")
X_PASSWORD = os.getenv("X_PASSWORD")

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
wait = WebDriverWait(driver, 10)
class InternetSpeedXBot:
    def __init__(self, web_driver, up, down):
        self.driver = web_driver
        self.up = up
        self.down = down

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        test_button  = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "a.js-start-test")))
        test_button.click()
        time.sleep(40)
        result_container = wait.until(ec.presence_of_element_located((By.CLASS_NAME, "result-container-data")))
        download_speed = result_container.find_element(By.CSS_SELECTOR, "div.result-item-download div.result-data").text
        upload_speed = result_container.find_element(By.CSS_SELECTOR, "div.result-item-upload div.result-data").text

        print(f"down: {download_speed}\nup: {upload_speed}")

    def tweet_at_provider(self):
        self.driver.get("https://x.com/login")
        email_input = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')))
        email_input.send_keys(X_EMAIL)
        time.sleep(2)
        email_input.send_keys(Keys.ENTER)


internet_speed_x_bot = InternetSpeedXBot(web_driver=driver, down=PROMISED_DOWN, up=PROMISED_UP)

# internet_speed_x_bot.get_internet_speed()
internet_speed_x_bot.tweet_at_provider()





