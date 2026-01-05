from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

load_dotenv()

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 3)

driver.get("https://appbrewery.github.io/gym/")


def retry(func, retries=7, description="Login"):
    for attempt in range(retries):
        print(f"Trying {description}. Attempt: {attempt + 1}")
        try:
            return func()
        except TimeoutException:
            if attempt == retries - 1:
                raise
            time.sleep(1)


def login(email=os.getenv("EMAIL"), password=os.getenv("PASSWORD")):
    join_btn = wait.until(EC.presence_of_element_located((By.ID, "login-button")))
    join_btn.click()
    email_input = wait.until(EC.presence_of_element_located((By.ID, "email-input")))
    password_input = wait.until(EC.presence_of_element_located((By.ID, "password-input")))
    email_input.clear()
    email_input.send_keys(email)
    password_input.clear()
    password_input.send_keys(password)

    login_btn = driver.find_element(By.ID, "submit-button")
    login_btn.click()

    # Wait for schedule page to load
    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))


retry(login, description="Login")


# Function to book a class process that checks if the button text changed with retry
def book_class(booking_button):
    booking_button.click()
    # Wait for button state to change - will time out if booking failed
    wait.until(lambda d: booking_button.text == "Booked" or booking_button.text == "Waitlisted")


# classes counters
booking_counter = 0
waitlist_counter = 0
already_done_counter = 0

processed_classes = []

# Find all class cards
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
for card in class_cards:
    # Get the day title from the parent day group
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday or Thursday
    if "Tue" in day_title or "Thu" in day_title:
        # Check if this is a 6pm class
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            # Get the class name
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            # Find and click the book button
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            button_txt = button.text
            # Track the class details
            class_info = f"{class_name} on {day_title}"

            if button_txt == "Booked":
                already_done_counter += 1
                print(f"✓ Already booked: {class_info}")

            elif button_txt == "Waitlisted":
                already_done_counter += 1
                print(f"✓ Already on waitlist: {class_info}")

            elif button_txt == "Join Waitlist":
                print(f"✓ Joining waitlist for: {class_info}")
                retry(lambda: book_class(button), description="Waitlisting")
                waitlist_counter += 1
                print(f"✓ Joined waitlist for: {class_info}")
                processed_classes.append(f"[New Waitlist] {class_info}")
                time.sleep(1)
            else:
                print(f"✓ Booking: {class_info}")
                retry(lambda: book_class(button), description="Booking")
                booking_counter += 1
                print(f"✓ Booked: {class_info}")
                processed_classes.append(f"[New Booking] {class_info}")
                time.sleep(1)

# print(f"""
# --- BOOKING SUMMARY ---
# Classes booked: {booking_counter}
# Waitlists joined: {waitlist_counter}
# Already booked/waitlisted: {already_done_counter}
# Total Tuesday & Thursday 6pm classes: {booking_counter + waitlist_counter + already_done_counter}
# """)
#
# # Print detailed class list
# print("\n--- DETAILED CLASS LIST ---")
# for class_detail in processed_classes:
#     print(f" • {class_detail}")


# _____________________________________________verifying bookings ___________________________________________________
total_booked = booking_counter + waitlist_counter + already_done_counter
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

# Navigate to My Bookings page
# Function to navigate to my bookings with retry
def get_my_bookings():
    my_bookings_link = wait.until(EC.element_to_be_clickable((By.ID, "my-bookings-link")))
    my_bookings_link.click()
    # Wait for page to load - will time out if navigation failed
    wait.until(EC.presence_of_element_located((By.ID, "my-bookings-page")))

    cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

    # Ensure we actually found cards - if empty, the page might not have loaded
    if not cards:
        raise TimeoutException("No booking cards found - page may not have loaded")
    return cards


# Put navigation to the Bookings page and get cards in the retry wrapper
all_cards = retry(get_my_bookings, description="Get my bookings")


# Count all Tuesday/Thursday 6pm bookings
verified_count = 0

for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        # Check if it's a Tuesday or Thursday 6pm class
        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        # Skip if no "When:" text found (not a booking card)
        pass

# Simple comparison
print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")

retry(get_my_bookings, description="Verify Bookings")
