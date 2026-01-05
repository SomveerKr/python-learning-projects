from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://ozh.github.io/cookieclicker/")
time.sleep(1)

select_eng_tag = driver.find_element(By.ID, "langSelect-EN")
select_eng_tag.click()

time.sleep(1)
cookie = driver.find_element(By.ID, "bigCookie")


def check_and_upgrade_store():
    # --- FIX 2: Use CSS Selectors for compound classes ---
    # We look for elements that have ALL three classes: product, unlocked, and enabled (affordable)
    upgrades = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

    # --- FIX 3: Check if list is empty ---
    if len(upgrades) > 0:
        # The last item in the list is usually the most expensive one currently affordable
        highest_upgrade = upgrades[-1]
        upgrade_name = highest_upgrade.text.split('\n')[0]  # Clean up text for printing
        print(f"Purchasing: {upgrade_name}")
        highest_upgrade.click()
    else:
        print("No upgrades affordable yet.")


# Time management
check_interval = 20  # Check for upgrades every 5 seconds
timeout = time.time() + check_interval
five_min = time.time() + 60 * 5  # Run for 5 minutes total
while True:
    cookie.click()
    # 2. Check for upgrades every 5 seconds
    if time.time() > timeout:
        check_and_upgrade_store()
    time.sleep(0.1)

    # 4. Stop after 5 minutes and print the result
    if time.time() > five_min:
        try:
            cps= driver.find_element(By.ID, "cookiesPerSecond")
            print(f"Time's up! Final Score: {cps.text}")
        except NoSuchElementException:
            print("Couldn't get final cookie count")
        break

time.sleep(2)
driver.quit()