from twilio.rest import Client
import os
from smtplib import SMTP
from dotenv import load_dotenv
# This line loads the environment variables from the .env file
load_dotenv()
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])
        self.my_gmail =os.getenv("MY_EMAIL")
        self.gmail_pass =os.getenv("EMAIL_PASSWORD")

    def send_sms(self, message_body):  
        message = self.client.messages.create(
        messaging_service_sid=os.getenv("TWILIO_MESSAGING_SERVICE_SID"),
        body=message_body,
        to=os.getenv("PHONE_NUMBER")
        )
        # Prints if successfully sent.
        print(message.status)

    # Is SMS not working for you or prefer whatsapp? Connect to the WhatsApp Sandbox!
    # https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn
    def send_whatsapp(self, message_body):
        message = self.client.messages.create(
            from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
            body=message_body,
            to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
        )
        print(message.status)
    
    def send_emails(self, emails_list, email_body):
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_gmail, password=self.gmail_pass)
            for email in emails_list:
                connection.sendmail(
                    from_addr=self.my_gmail, 
                    to_addrs=email, 
                    msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode("utf-8")
                    )