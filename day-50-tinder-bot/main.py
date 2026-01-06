from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver  = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 3)

driver.get("https://tinder.com/")


