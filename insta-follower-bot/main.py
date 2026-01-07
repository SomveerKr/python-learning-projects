from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from dotenv import load_dotenv
import time
import os

load_dotenv()

SIMILIAR_ACCOUNT= "piximperfect"
USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('useAutomationExtension', False)


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver=driver, timeout=20)

class InstaFollower:
    def __init__(self, driver):
        self.driver = driver

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        username_input = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'input[name="username"], input[name="email"]')))
        username_input.send_keys(USERNAME)
        pass_input = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"], input[name="pass"]')))
        pass_input.send_keys(PASSWORD)
        time.sleep(1)
        pass_input.send_keys(Keys.RETURN)


    def find_followers(self):
        similar_acc_url = f"https://www.instagram.com/{SIMILIAR_ACCOUNT}/"
        self.driver.get(similar_acc_url)
        time.sleep(5)
        # followers_page_link = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/piximperfect/followers/"')))
        followers_page_link = wait.until(
            ec.element_to_be_clickable((By.PARTIAL_LINK_TEXT, 'followers')))
        followers_page_link.click()
        #popup scrollable div ->change xpath value based on site changes
        # followers_popup = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".xz65tgg.x1rife3k")))
        # Scroll till Followers list is there
        for i in range(7):
            try:
                # Re-locate the element each time to avoid stale reference
                followers_popup = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".xz65tgg.x1rife3k")))
                self.driver.execute_script(
                    'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                    followers_popup
                )
                time.sleep(3)
            except Exception as e:
                print(f"Error during scrolling: {e}")
                break

    def follow(self):
        follow_buttons = self.driver.find_elements(By.XPATH, "//button[.//div//div[text()='Follow']]")
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


insta_followers = InstaFollower(driver)
insta_followers.login()
time.sleep(10)
insta_followers.find_followers()
insta_followers.follow()