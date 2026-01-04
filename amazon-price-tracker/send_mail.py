import smtplib
import os
from dotenv import load_dotenv

# 1. Load the variables from .env into the environment
load_dotenv()


class SendMail:
    def __init__(self):
        self.my_email = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_PASSWORD")

    def send_mail(self, receiver_email, current_price, product_title):
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                # 3. Secure the connection
                connection.starttls()

                # 4. Login
                connection.login(user=self.my_email, password=self.password)

                # 5. Send Mail
                # Note: The format is "Subject:...\n\nBody..."
                connection.sendmail(
                    from_addr=os.getenv("MY_EMAIL"),
                    to_addrs=receiver_email,
                    msg=f"Subject: {product_title}\n\nCurrent Price of product is INR {current_price}"
                )
                print("Email sent successfully!")

        except smtplib.SMTPAuthenticationError:
            print("Authentication failed. Check your email or App Password.")
        except Exception as e:
            print(f"Error: {e}")

